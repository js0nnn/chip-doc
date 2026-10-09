"""Grounded answer generation with Qwen3-0.6B (+ optional LoRA adapter).

build_prompt() is shared by training (scripts/build_sft.py) and inference, so
the fine-tuned model always sees exactly the format it was trained on.
"""
from pathlib import Path

BASE_MODEL = "Qwen/Qwen3-0.6B"
ADAPTER = Path(__file__).resolve().parents[1] / "models" / "chipdoc-qwen3-0.6b-lora"
NOT_FOUND = "Not found in the provided datasheet."
TOP_K = 5
MAX_NEW_TOKENS = 256

SYSTEM = (
    "You are ChipDoc, an assistant that answers questions about a microcontroller datasheet. "
    "Use ONLY the numbered context passages. Answer briefly and precisely, copy values and units exactly, "
    "and cite the page of each fact like [p.12]. "
    f"If the passages do not contain the answer, reply exactly: {NOT_FOUND}"
)


def format_context(chunks):
    return "\n\n".join(
        f"[{i}] page {c['page']} | {c['section']}\n{c['text']}" for i, c in enumerate(chunks, 1)
    )


def build_messages(question, chunks):
    return [
        {"role": "system", "content": SYSTEM},
        {"role": "user", "content": f"Context:\n{format_context(chunks)}\n\nQuestion: {question}"},
    ]


def build_prompt(tokenizer, question, chunks):
    return tokenizer.apply_chat_template(build_messages(question, chunks), tokenize=False,
                                         add_generation_prompt=True, enable_thinking=False)


class Generator:
    def __init__(self, adapter=ADAPTER, base=BASE_MODEL):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.tok = AutoTokenizer.from_pretrained(base)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        dtype = torch.bfloat16 if device == "cuda" else torch.float32
        model = AutoModelForCausalLM.from_pretrained(base, dtype=dtype).to(device)
        self.finetuned = bool(adapter) and Path(adapter).exists()
        if self.finetuned:
            from peft import PeftModel
            model = PeftModel.from_pretrained(model, str(adapter)).merge_and_unload()
        self.model = model.eval()

    def answer(self, question, chunks, on_token=None):
        """Greedy decode. on_token(str) streams text pieces as they are produced."""
        import threading
        import torch
        from transformers import TextIteratorStreamer
        prompt = build_prompt(self.tok, question, chunks)
        inputs = self.tok(prompt, return_tensors="pt").to(self.model.device)
        kwargs = dict(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False,
                      repetition_penalty=1.05, pad_token_id=self.tok.eos_token_id)
        if on_token is None:
            with torch.inference_mode():
                out = self.model.generate(**kwargs)
            return self.tok.decode(out[0, inputs["input_ids"].shape[1]:], skip_special_tokens=True).strip()
        streamer = TextIteratorStreamer(self.tok, skip_prompt=True, skip_special_tokens=True)
        t = threading.Thread(target=lambda: torch.inference_mode()(self.model.generate)(**kwargs, streamer=streamer))
        t.start()
        text = ""
        for piece in streamer:
            text += piece
            on_token(piece)
        t.join()
        return text.strip()
