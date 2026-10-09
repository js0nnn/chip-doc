"""LoRA fine-tune of Qwen3-0.6B on the RAFT-style SFT data (loss on answers only).

Stop Ollama's model first, it holds VRAM:
    curl -s localhost:11434/api/generate -d '{"model":"qwen3:4b","keep_alive":0}'
Usage: python scripts/train_lora.py [--epochs 2]
Output: models/chipdoc-qwen3-0.6b-lora/ (adapter + training log)
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from chipdoc.generate import ADAPTER, BASE_MODEL  # noqa: E402

SFT = ROOT / "dataset" / "sft"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--epochs", type=float, default=2)
    ap.add_argument("--lr", type=float, default=2e-4)
    ap.add_argument("--max-length", type=int, default=2560)
    args = ap.parse_args()

    import torch
    from datasets import load_dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import SFTConfig, SFTTrainer

    data = load_dataset("json", data_files={s: str(SFT / f"{s}.jsonl") for s in ("train", "val")})
    data = data.remove_columns(["doc"])
    tok = AutoTokenizer.from_pretrained(BASE_MODEL)
    model = AutoModelForCausalLM.from_pretrained(BASE_MODEL, dtype=torch.bfloat16)

    cfg = SFTConfig(
        output_dir=str(ADAPTER),
        num_train_epochs=args.epochs,
        learning_rate=args.lr,
        lr_scheduler_type="cosine",
        warmup_ratio=0.03,
        # Batch 1: Qwen's 151k vocab makes logits for a 2.5k-token sequence ~1.5 GB.
        per_device_train_batch_size=1,
        per_device_eval_batch_size=1,
        gradient_accumulation_steps=16,
        gradient_checkpointing=True,
        bf16=True,
        max_length=args.max_length,
        completion_only_loss=True,
        logging_steps=10,
        eval_strategy="epoch",
        save_strategy="no",
        report_to="none",
        seed=13,
    )
    lora = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, task_type="CAUSAL_LM",
                      target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"])
    trainer = SFTTrainer(model=model, args=cfg, train_dataset=data["train"], eval_dataset=data["val"],
                         processing_class=tok, peft_config=lora)
    trainer.model.print_trainable_parameters()
    trainer.train()
    trainer.save_model(str(ADAPTER))
    (ADAPTER / "log_history.json").write_text(json.dumps(trainer.state.log_history, indent=2))
    print(f"adapter saved to {ADAPTER}")


if __name__ == "__main__":
    main()
