"""Filter teacher QA pairs and build RAFT-style SFT data.

Each example = question + 5 passages from the same datasheet (the oracle
chunk + 4 hard negatives retrieved for that question, shuffled). In ~20% of
examples the oracle is removed and the target becomes NOT_FOUND, which
teaches the model to refuse instead of guessing.
Whole datasheets are held out for testing (TEST_DOCS).

Usage: python scripts/build_sft.py
Output: dataset/sft/{train,val,test}.jsonl, dataset/sft/stats.json
"""
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from chipdoc.generate import BASE_MODEL, NOT_FOUND, TOP_K, build_prompt  # noqa: E402
from chipdoc.index import Index  # noqa: E402

RAW_QA = ROOT / "dataset" / "qa" / "raw_qa.jsonl"
INDEX = ROOT / "dataset" / "index"
OUT = ROOT / "dataset" / "sft"
SEED = 13
NO_ORACLE_RATE = 0.2
VAL_RATE = 0.05
# One held-out datasheet per vendor family: the model never sees these in training.
TEST_DOCS = {"2_STM32F103C8", "13_LPC1768", "17_ESP8266EX", "20_ATmega32U4", "28_MSP430FR2433"}

BAD_QUESTION = re.compile(r"\b(excerpt|passage|this (table|section|figure|document)|the above|given text)\b", re.I)
NUMBER = re.compile(r"\d+(?:\.\d+)?")


def norm(s):
    s = re.sub(r"[*_`|#<>]|<br>|</?su[pb]>", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def supported(evidence, answer, text):
    """Evidence appears (near-)verbatim and every number in the answer is in the text."""
    t, e = norm(text), norm(evidence)
    if len(e) < 10:
        return False
    if e not in t:
        words = e.split()
        if sum(w in t for w in words) < 0.9 * len(words):
            return False
    numbers = set(NUMBER.findall(t))
    return all(n in numbers for n in NUMBER.findall(answer))


def keep(p):
    q, a = p.get("question", "").strip(), p.get("answer", "").strip()
    return 15 <= len(q) <= 300 and 2 <= len(a) <= 400 and q.endswith("?") and not BAD_QUESTION.search(q)


def main():
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(BASE_MODEL)
    rng = random.Random(SEED)
    stats = Counter()
    indexes = {}
    rows = {"train": [], "val": [], "test": []}
    seen = set()

    for line in RAW_QA.open(encoding="utf-8"):
        r = json.loads(line)
        if r["doc"] not in indexes:
            indexes[r["doc"]] = Index.load(INDEX / r["doc"])
        idx = indexes[r["doc"]]
        oracle = idx.chunks[r["chunk_id"]]
        for p in r["pairs"]:
            stats["generated"] += 1
            if not keep(p):
                stats["drop_format"] += 1
                continue
            if not supported(p["evidence"], p["answer"], oracle["text"]):
                stats["drop_unsupported"] += 1
                continue
            key = norm(p["question"])
            if key in seen:
                stats["drop_duplicate"] += 1
                continue
            seen.add(key)
            stats["kept"] += 1
            q, a = p["question"].strip(), p["answer"].strip()
            if r["doc"] in TEST_DOCS:
                rows["test"].append({"doc": r["doc"], "chunk_id": r["chunk_id"], "page": oracle["page"],
                                     "question": q, "answer": a, "evidence": p["evidence"]})
                continue

            hits = [h for h in idx.search(q, k=TOP_K + 3) if h["id"] != r["chunk_id"]]
            if rng.random() < NO_ORACLE_RATE and not any(supported(p["evidence"], a, h["text"]) for h in hits[:TOP_K]):
                context, target = hits[:TOP_K], NOT_FOUND
                stats["no_oracle"] += 1
            else:
                context = hits[:TOP_K - 1] + [{**oracle, "id": r["chunk_id"]}]
                rng.shuffle(context)
                target = f"{a.rstrip()} [p.{oracle['page']}]"
            split = "val" if rng.random() < VAL_RATE else "train"
            rows[split].append({"doc": r["doc"], "prompt": build_prompt(tok, q, context), "completion": target + tok.eos_token})

    OUT.mkdir(parents=True, exist_ok=True)
    for split, items in rows.items():
        with (OUT / f"{split}.jsonl").open("w", encoding="utf-8") as f:
            for it in items:
                f.write(json.dumps(it, ensure_ascii=False) + "\n")
        stats[split] = len(items)
    lengths = sorted(len(tok(x["prompt"] + x["completion"]).input_ids) for x in rows["train"])
    if lengths:
        stats["train_tokens_p50"], stats["train_tokens_p95"], stats["train_tokens_max"] = (
            lengths[len(lengths) // 2], lengths[int(len(lengths) * 0.95)], lengths[-1])
    (OUT / "stats.json").write_text(json.dumps(stats, indent=2))
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    assert supported("TIM2 is a 32-bit timer", "It is 32-bit.", "**TIM2** is a 32-bit timer with 4 channels")
    assert not supported("TIM2 is a 32-bit timer", "It is 16-bit.", "TIM2 is a 32-bit timer")
    main()
