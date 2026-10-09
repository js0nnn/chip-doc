"""Per-document hybrid index: bge-small dense (FAISS) + BM25, fused with RRF.

Stored as chunks.json + dense.faiss. No pickle: cached indexes sit next to
user-supplied data, and unpickling untrusted files executes code.
"""
import hashlib
import json
import re
from functools import lru_cache
from pathlib import Path

import numpy as np

EMBED_MODEL = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
CACHE_DIR = Path.home() / ".cache" / "chipdoc"
RRF_K = 60
POOL = 50  # candidates taken from each retriever before fusion

TOKEN = re.compile(r"[a-z0-9][a-z0-9_.]*")


def tokenize(text):
    # Keeps register names (tim2_ccr1) and values (3.3) whole.
    return [t.rstrip(".") for t in TOKEN.findall(text.lower())]


@lru_cache(maxsize=1)
def embedder():
    import torch
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer(EMBED_MODEL, device="cuda" if torch.cuda.is_available() else "cpu")


def embed_text(c):
    return f"{c['document']} | {c['section']}\n{c['text']}"


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


class Index:
    def __init__(self, chunks, dense):
        from rank_bm25 import BM25Okapi
        self.chunks, self.dense = chunks, dense
        self.bm25 = BM25Okapi([tokenize(embed_text(c)) for c in chunks])

    @classmethod
    def build(cls, chunks):
        import faiss
        if not chunks:
            raise ValueError("No text could be extracted from this PDF (scanned image?)")
        vecs = embedder().encode([embed_text(c) for c in chunks], batch_size=64,
                                 normalize_embeddings=True, convert_to_numpy=True)
        dense = faiss.IndexFlatIP(vecs.shape[1])
        dense.add(np.asarray(vecs, dtype=np.float32))
        return cls(chunks, dense)

    def save(self, folder):
        import faiss
        folder = Path(folder)
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "chunks.json").write_text(json.dumps(self.chunks, ensure_ascii=False), encoding="utf-8")
        faiss.write_index(self.dense, str(folder / "dense.faiss"))

    @classmethod
    def load(cls, folder):
        import faiss
        folder = Path(folder)
        chunks = json.loads((folder / "chunks.json").read_text(encoding="utf-8"))
        dense = faiss.read_index(str(folder / "dense.faiss"))
        if dense.ntotal != len(chunks):
            raise ValueError(f"Corrupt index in {folder}")
        return cls(chunks, dense)

    def search(self, query, k=6, mode="hybrid"):
        """Return top-k chunks (dicts with an added 'score')."""
        ranked = []
        if mode in ("hybrid", "dense"):
            q = embedder().encode([QUERY_PREFIX + query], normalize_embeddings=True, convert_to_numpy=True)
            _, ids = self.dense.search(np.asarray(q, dtype=np.float32), min(POOL, len(self.chunks)))
            ranked.append([i for i in ids[0] if i >= 0])
        if mode in ("hybrid", "bm25"):
            scores = self.bm25.get_scores(tokenize(query))
            ranked.append(list(np.argsort(-scores)[:POOL]))
        fused = {}
        for ids in ranked:
            for rank, i in enumerate(ids):
                fused[int(i)] = fused.get(int(i), 0.0) + 1.0 / (RRF_K + rank + 1)
        best = sorted(fused, key=fused.get, reverse=True)[:k]
        return [{**self.chunks[i], "id": i, "score": fused[i]} for i in best]


def index_pdf(pdf_path, cache_dir=CACHE_DIR, log=print):
    """Validate, extract, chunk and index a PDF; cached by content hash."""
    from . import ingest
    pdf_path = ingest.validate_pdf(pdf_path)
    folder = Path(cache_dir) / file_sha256(pdf_path)[:16]
    if (folder / "dense.faiss").exists():
        log(f"Using cached index ({folder})")
        return Index.load(folder)
    log("Extracting text (first run for this PDF, can take a minute)...")
    doc = ingest.extract(pdf_path)
    chunks = ingest.chunk(doc)
    log(f"{doc['page_count']} pages -> {len(chunks)} chunks. Embedding...")
    idx = Index.build(chunks)
    idx.save(folder)
    return idx


if __name__ == "__main__":
    assert tokenize("Set TIM2_CCR1 to 3.3 V.") == ["set", "tim2_ccr1", "to", "3.3", "v"]
    chunks = [{"document": "t.pdf", "page": p, "section": s, "text": t} for p, s, t in [
        (1, "Timers", "TIM2 is a 32-bit timer with four capture/compare channels."),
        (2, "ADC", "Three 12-bit ADCs share up to 16 external channels."),
        (3, "GPIO", "GPIO pins toggle at up to 84 MHz."),
    ]]
    idx = Index.build(chunks)
    assert idx.search("How many bits is the ADC?", k=1)[0]["page"] == 2
    assert idx.search("TIM2", k=1, mode="bm25")[0]["page"] == 1
    print("index OK")
