"""Terminal app: python -m chipdoc path/to/datasheet.pdf

Everything runs locally; neither the PDF nor the questions leave the machine.
"""
import argparse
import os
import re
import sys
import time
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .generate import NOT_FOUND, TOP_K
from .index import index_pdf


def tidy(text):
    """Passage text for display: drop Markdown/HTML markup and blank lines."""
    text = re.sub(r"</?(u|sup|sub|b|i)>|\*\*|`|(?m:^#+ *)", "", text).replace("<br>", " ")
    return "\n".join(line.strip() for line in text.splitlines() if line.strip())


HELP = "Ask a question about the datasheet.  /sources  show passages used   /quit  exit"


def main(argv=None):
    ap = argparse.ArgumentParser(prog="chipdoc", description="Ask questions about a datasheet PDF.")
    ap.add_argument("pdf", help="path to a datasheet PDF")
    ap.add_argument("-k", type=int, default=TOP_K, help=f"passages per answer (default {TOP_K})")
    ap.add_argument("--base", action="store_true", help="use the base model without the fine-tuned adapter")
    ap.add_argument("-q", "--question", help="answer one question and exit")
    args = ap.parse_args(argv)

    console = Console()
    os.environ.setdefault("TQDM_DISABLE", "1")  # library progress bars clutter the REPL
    t0 = time.perf_counter()
    try:
        with console.status("Indexing PDF..."):
            idx = index_pdf(args.pdf, log=lambda m: console.print(f"[dim]{m}[/dim]"))
    except ValueError as e:
        console.print(f"[red]Error:[/red] {e}")
        return 1
    console.print(f"[green]✓[/green] Index ready: {len(idx.chunks)} passages [dim]({time.perf_counter() - t0:.1f} s)[/dim]")

    t0 = time.perf_counter()
    with console.status("Loading Qwen3-0.6B" + ("" if args.base else " + ChipDoc LoRA adapter") + "..."):
        from huggingface_hub.utils import disable_progress_bars, logging as hub_logging
        from transformers.utils import logging as hf_logging
        disable_progress_bars(), hub_logging.set_verbosity_error()
        hf_logging.disable_progress_bar(), hf_logging.set_verbosity_error()
        from .generate import Generator
        gen = Generator(adapter=None) if args.base else Generator()
    model_name = "fine-tuned" if gen.finetuned else "base"
    console.print(f"[green]✓[/green] Model ready: Qwen3-0.6B ({model_name}) on {gen.model.device.type.upper()} "
                  f"[dim]({time.perf_counter() - t0:.1f} s)[/dim]\n")
    console.print(Panel(f"[bold]{Path(args.pdf).name}[/bold]  {len(idx.chunks)} passages  |  "
                        f"Qwen3-0.6B ({model_name})\n{HELP}", title="ChipDoc", border_style="cyan"))

    def ask(question):
        hits = idx.search(question, k=args.k)
        console.print("[bold green]Answer:[/bold green] ", end="")
        text = gen.answer(question, hits, on_token=lambda t: console.print(t, end="", markup=False, highlight=False))
        console.print()
        if text != NOT_FOUND:
            pages = ", ".join(dict.fromkeys(f"p.{h['page']}" for h in hits))
            console.print(f"[dim]Searched: {pages}[/dim]")
        return hits

    if args.question:
        ask(args.question)
        return 0

    from prompt_toolkit import PromptSession
    session, last = PromptSession(), []
    while True:
        try:
            q = session.prompt("\n❯ ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not q:
            continue
        if q in ("/quit", "/exit", "/q"):
            break
        if q == "/help":
            console.print(HELP)
        elif q == "/sources":
            for i, h in enumerate(last, 1):
                console.print(Panel(Text(tidy(h["text"])), title=f"[{i}] p.{h['page']} | {h['section']}", border_style="dim"))
        else:
            last = ask(q)
    return 0


if __name__ == "__main__":
    sys.exit(main())
