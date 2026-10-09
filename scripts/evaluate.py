"""Evaluate retrieval and answers on the held-out datasheets.

  python scripts/evaluate.py retrieval          # Recall@k / MRR for dense, bm25, hybrid
  python scripts/evaluate.py answers --system ft|base|teacher [--n 150]
  python scripts/evaluate.py report             # markdown table of all saved results

Answerable: hybrid top-5 from the question's datasheet (the real pipeline).
Unanswerable: same question, but every passage that contains the evidence is
removed, so the right output is NOT_FOUND.
"""
import argparse
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from chipdoc.generate import NOT_FOUND, TOP_K, build_messages  # noqa: E402
from chipdoc.index import Index  # noqa: E402
from build_sft import NUMBER, norm, supported  # noqa: E402

TEST = ROOT / "dataset" / "sft" / "test.jsonl"
INDEX = ROOT / "dataset" / "index"
RESULTS = ROOT / "results"
SEED = 13
CITE = re.compile(r"\[p\.?\s*(\d+)\]")


def load_test(n=None):
    items = [json.loads(line) for line in TEST.open(encoding="utf-8")]
    random.Random(SEED).shuffle(items)
    return items[:n] if n else items


def hit_rank(item, hits):
    for rank, h in enumerate(hits, 1):
        if h["id"] == item["chunk_id"] or supported(item["evidence"], item["answer"], h["text"]):
            return rank
    return None


def retrieval(args):
    items, indexes, out = load_test(), {}, {}
    for mode in ("dense", "bm25", "hybrid"):
        ranks = []
        for it in items:
            idx = indexes.setdefault(it["doc"], Index.load(INDEX / it["doc"]))
            ranks.append(hit_rank(it, idx.search(it["question"], k=10, mode=mode)))
        n = len(ranks)
        out[mode] = {"n": n, **{f"recall@{k}": sum(r is not None and r <= k for r in ranks) / n for k in (1, 3, 5, 10)},
                     "mrr@10": sum(1 / r for r in ranks if r) / n}
        print(mode, json.dumps(out[mode]))
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "retrieval.json").write_text(json.dumps(out, indent=2))


def f1(pred, gold):
    p, g = norm(pred).split(), norm(gold).split()
    common = sum((Counter(p) & Counter(g)).values())
    if not common:
        return 0.0
    prec, rec = common / len(p), common / len(g)
    return 2 * prec * rec / (prec + rec)


def make_answerer(system):
    if system == "teacher":
        import requests

        def ans(q, chunks):
            r = requests.post("http://localhost:11434/api/chat", timeout=300, json={
                "model": "qwen3:4b", "stream": False, "think": False,
                "options": {"temperature": 0, "num_ctx": 6144, "num_predict": 256},
                "messages": build_messages(q, chunks)})
            r.raise_for_status()
            return re.sub(r"<think>.*?</think>", "", r.json()["message"]["content"], flags=re.S).strip()
        return ans
    from chipdoc.generate import Generator
    gen = Generator(adapter=None) if system == "base" else Generator()
    if system == "ft" and not gen.finetuned:
        raise SystemExit("No adapter found; train first.")
    return gen.answer


def answers(args):
    items, indexes = load_test(args.n), {}
    ans = make_answerer(args.system)
    preds = []
    for i, it in enumerate(items, 1):
        idx = indexes.setdefault(it["doc"], Index.load(INDEX / it["doc"]))
        hits = idx.search(it["question"], k=TOP_K + 10)
        answerable = hits[:TOP_K]
        unanswerable = [h for h in hits if hit_rank(it, [h]) is None][:TOP_K]
        for kind, ctx in (("answerable", answerable), ("unanswerable", unanswerable)):
            pred = ans(it["question"], ctx)
            preds.append({"kind": kind, "doc": it["doc"], "question": it["question"], "gold": it["answer"],
                          "gold_page": it["page"], "retrieved": hit_rank(it, ctx) is not None, "pred": pred})
        if i % 10 == 0:
            print(f"[{i}/{len(items)}] {preds[-2]['pred'][:100]!r}", flush=True)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / f"preds_{args.system}.json").write_text(json.dumps(preds, indent=2, ensure_ascii=False))
    print(json.dumps(score(preds), indent=2))


def score(preds):
    refused = lambda p: NOT_FOUND.lower().rstrip(".") in p["pred"].lower()  # noqa: E731
    ans = [p for p in preds if p["kind"] == "answerable"]
    una = [p for p in preds if p["kind"] == "unanswerable"]
    got = [p for p in ans if p["retrieved"]]  # judge the generator only where retrieval found the evidence
    nums = [p for p in got if NUMBER.search(p["gold"])]
    cited = [p for p in got if not refused(p)]
    return {
        "answerable_n": len(ans),
        "evidence_retrieved": len(got) / max(1, len(ans)),
        "token_f1": sum(f1(CITE.sub("", p["pred"]), p["gold"]) for p in got) / max(1, len(got)),
        "numbers_correct": sum(all(n in p["pred"] for n in NUMBER.findall(p["gold"])) for p in nums) / max(1, len(nums)),
        "citation_correct": sum(str(p["gold_page"]) in CITE.findall(p["pred"]) for p in cited) / max(1, len(cited)),
        "false_refusal": sum(map(refused, got)) / max(1, len(got)),
        "unanswerable_n": len(una),
        "refusal_accuracy": sum(map(refused, una)) / max(1, len(una)),
    }


def report(args):
    names = {"base": "Qwen3-0.6B base", "ft": "Qwen3-0.6B + ChipDoc LoRA", "teacher": "qwen3:4b (teacher)"}
    rows = []
    for sys_ in names:
        f = RESULTS / f"preds_{sys_}.json"
        if f.exists():
            s = score(json.loads(f.read_text()))
            (RESULTS / f"scores_{sys_}.json").write_text(json.dumps(s, indent=2))
            rows.append((names[sys_], s))
    keys = ["token_f1", "numbers_correct", "citation_correct", "false_refusal", "refusal_accuracy"]
    print("| System | " + " | ".join(keys) + " |")
    print("|---" * (len(keys) + 1) + "|")
    for name, s in rows:
        print(f"| {name} | " + " | ".join(f"{s[k]:.2f}" for k in keys) + " |")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["retrieval", "answers", "report"])
    ap.add_argument("--system", choices=["ft", "base", "teacher"], default="ft")
    ap.add_argument("--n", type=int, default=150)
    a = ap.parse_args()
    {"retrieval": retrieval, "answers": answers, "report": report}[a.cmd](a)
