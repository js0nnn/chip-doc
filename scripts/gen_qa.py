"""Teacher QA generation: qwen3:4b (Ollama) writes grounded QA pairs per chunk.

Resumable: re-running skips chunks already in the output file.
Usage: python scripts/gen_qa.py [--per-doc 40] [--limit N]
Output: dataset/qa/raw_qa.jsonl
"""
import argparse
import json
import random
import re
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "dataset" / "index"
OUT = ROOT / "dataset" / "qa" / "raw_qa.jsonl"
OLLAMA = "http://localhost:11434/api/chat"
TEACHER = "qwen3:4b"
SEED = 13

SKIP_SECTION = re.compile(r"revision|ordering|contents|disclaimer|notice|trademark|important|errata|"
                          r"package (information|marking)|marking|history|legal|contact|references|\brev\b", re.I)

PROMPT = """You write exam questions about a microcontroller datasheet excerpt.

Datasheet: {document}
Section: {section}
Excerpt (page {page}):
\"\"\"
{text}
\"\"\"

Write {n} question-answer pairs a firmware engineer would ask that this excerpt answers.
Rules:
- Every fact in the answer must be stated in the excerpt. Copy numbers and units exactly.
- Questions must stand alone: name the peripheral, pin, register or parameter. Never say "this table" or "the excerpt".
- Prefer concrete facts: values with units, limits, counts, register/bit names, pin functions, modes.
- Answers: one or two short sentences.
- "evidence": copy a short span (5-30 words) verbatim from the excerpt that supports the answer.
/no_think"""

SCHEMA = {
    "type": "object",
    "properties": {"pairs": {"type": "array", "items": {
        "type": "object",
        "properties": {"question": {"type": "string"}, "answer": {"type": "string"}, "evidence": {"type": "string"}},
        "required": ["question", "answer", "evidence"]}}},
    "required": ["pairs"],
}


def useful(c):
    t = c["text"]
    if len(t) < 500 or SKIP_SECTION.search(c["section"]) or not re.search(r"\d", t) or t.count("Updated") >= 3:
        return False
    lines = [ln for ln in t.splitlines() if ln.strip()]
    toc_like = sum(bool(re.search(r"\.{4,}|\s\d+\s*$", ln)) for ln in lines)
    return toc_like < 0.5 * len(lines)


def sample(per_doc):
    picked = []
    for folder in sorted(INDEX.iterdir()):
        if not (folder / "dense.faiss").exists():
            continue
        rng = random.Random(f"{SEED}-{folder.name}")  # per-doc: adding datasheets later keeps earlier picks
        chunks = json.loads((folder / "chunks.json").read_text(encoding="utf-8"))
        ids = [i for i, c in enumerate(chunks) if useful(c)]
        for i in rng.sample(ids, min(per_doc, len(ids))):
            picked.append((folder.name, i, chunks[i]))
    random.Random(SEED).shuffle(picked)  # interleave docs so a partial run still covers all of them
    return picked


def ask(c, n=2):
    r = requests.post(OLLAMA, timeout=300, json={
        "model": TEACHER, "stream": False, "think": False, "format": SCHEMA,
        "options": {"temperature": 0.3, "num_ctx": 4096, "num_predict": 600},
        "messages": [{"role": "user", "content": PROMPT.format(n=n, **c)}],
    })
    r.raise_for_status()
    return json.loads(r.json()["message"]["content"]).get("pairs", [])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-doc", type=int, default=40)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    done = set()
    if OUT.exists():
        for line in OUT.open(encoding="utf-8"):
            r = json.loads(line)
            done.add((r["doc"], r["chunk_id"]))
    todo = [x for x in sample(args.per_doc) if (x[0], x[1]) not in done][: args.limit]
    print(f"{len(done)} chunks done, {len(todo)} to go")

    with OUT.open("a", encoding="utf-8") as f:
        for k, (doc, cid, c) in enumerate(todo, 1):
            try:
                pairs = ask(c)
            except Exception as e:  # one bad generation must not kill an overnight run
                print(f"[{k}/{len(todo)}] {doc}#{cid} error: {e}")
                continue
            # One line per chunk (even with 0 pairs) so resume skips it.
            f.write(json.dumps({"doc": doc, "chunk_id": cid, "page": c["page"], "section": c["section"],
                                "pairs": pairs}, ensure_ascii=False) + "\n")
            f.flush()
            if k % 25 == 0:
                print(f"[{k}/{len(todo)}] last: {pairs[0]['question'] if pairs else '-'}", flush=True)


if __name__ == "__main__":
    main()
