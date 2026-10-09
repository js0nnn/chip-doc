"""Extract (cached), chunk and index every PDF in dataset/raw.

Usage: python scripts/build_corpus.py [--force]
Outputs: dataset/processed_pymupdf/<name>.json, dataset/index/<name>/{chunks.json,dense.faiss}
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from chipdoc import ingest  # noqa: E402
from chipdoc.index import Index  # noqa: E402

RAW = ROOT / "dataset" / "raw"
PROCESSED = ROOT / "dataset" / "processed_pymupdf"
INDEX = ROOT / "dataset" / "index"


def main(force=False):
    PROCESSED.mkdir(parents=True, exist_ok=True)
    total = 0
    for pdf in sorted(RAW.glob("*.pdf"), key=lambda p: int(p.name.split("_")[0])):
        out = INDEX / pdf.stem
        if (out / "dense.faiss").exists() and not force:
            print(f"{pdf.name:32} cached")
            continue
        cache = PROCESSED / f"{pdf.stem}.json"
        if cache.exists():
            doc = json.loads(cache.read_text(encoding="utf-8"))
        else:
            doc = ingest.extract(ingest.validate_pdf(pdf))
            cache.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        chunks = ingest.chunk(doc)
        Index.build(chunks).save(out)
        total += len(chunks)
        print(f"{pdf.name:32} {doc['page_count']:5} pages {len(chunks):6} chunks")
    print(f"done, {total} new chunks")


if __name__ == "__main__":
    main(force="--force" in sys.argv)
