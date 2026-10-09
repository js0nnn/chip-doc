"""PDF -> pages -> retrieval chunks.

Chunks never cross a page boundary, so every chunk cites exactly one page.
Section labels come from the Markdown headings pymupdf4llm emits (carried
across pages), falling back to the PDF bookmarks, so PDFs without a TOC work.
"""
import re
from pathlib import Path

MAX_PDF_BYTES = 100 * 2**20
MAX_PAGES = 2000
CHUNK_CHARS = 1200  # ~400-500 tokens of datasheet text: fits bge-small's 512-token window
OVERLAP_CHARS = 150

HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.M)


def validate_pdf(path):
    """Trust boundary: the CLI takes arbitrary user paths."""
    path = Path(path).expanduser().resolve()
    if not path.is_file():
        raise ValueError(f"Not a file: {path}")
    if path.stat().st_size > MAX_PDF_BYTES:
        raise ValueError(f"PDF larger than {MAX_PDF_BYTES // 2**20} MB")
    with open(path, "rb") as f:
        if f.read(5) != b"%PDF-":
            raise ValueError("File is not a PDF")
    return path


def extract(pdf_path):
    """Return {'filename', 'page_count', 'toc', 'pages': [{'page', 'text'}]}."""
    import pymupdf
    import pymupdf4llm

    with pymupdf.open(pdf_path) as doc:
        if len(doc) > MAX_PAGES:
            raise ValueError(f"PDF has more than {MAX_PAGES} pages")
        toc = [{"level": l, "title": t, "page": p} for l, t, p in doc.get_toc()]
        pages = pymupdf4llm.to_markdown(doc, page_chunks=True, show_progress=False)
        return {
            "filename": Path(pdf_path).name,
            "page_count": len(doc),
            "toc": toc,
            # Some PDFs decode to lone UTF-16 surrogates, which can't be written as UTF-8.
            "pages": [{"page": i + 1, "text": p.get("text", "").encode("utf-8", "replace").decode("utf-8")}
                      for i, p in enumerate(pages)],
        }


def clean(text):
    text = text.replace("\x00", "").replace("\xa0", " ").replace("\r\n", "\n")
    text = re.sub(r"<!--.*?-->", "", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def clean_heading(h):
    return re.sub(r"\s+", " ", h.replace("*", "").replace("_", " ")).strip()


def split_text(text, max_chars=CHUNK_CHARS, overlap=OVERLAP_CHARS):
    """Split at paragraph > line > sentence boundaries, with overlap."""
    text = text.strip()
    if len(text) <= max_chars:
        return [text] if text else []
    out, start = [], 0
    while start < len(text):
        end = min(start + max_chars, len(text))
        if end < len(text):
            for sep in ("\n\n", "\n", ". "):
                b = text.rfind(sep, start, end)
                if b > start + max_chars // 2:
                    end = b + len(sep)
                    break
        if piece := text[start:end].strip():
            out.append(piece)
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)
    return out


def furniture(pages):
    """Running headers/footers: short lines repeated on >=30% of pages."""
    from collections import Counter
    seen = Counter()
    for p in pages:
        # Table rows (|...|) repeat legitimately, e.g. separator lines.
        seen.update({s for ln in p["text"].splitlines() if 0 < len(s := ln.strip()) < 80 and not s.startswith("|")})
    floor = max(5, int(0.3 * len(pages)))
    return {ln for ln, n in seen.items() if n >= floor}


def chunk(doc):
    """Return a list of chunk dicts: document, page, section, text."""
    toc = sorted((t for t in doc.get("toc", []) if isinstance(t.get("page"), int)), key=lambda t: t["page"])
    drop = furniture(doc["pages"])
    section, chunks = "", []
    for page in doc["pages"]:
        text = clean("\n".join(ln for ln in page["text"].splitlines() if ln.strip() not in drop))
        if not text:
            continue
        toc_here = [t for t in toc if t["page"] <= page["page"]]
        if toc_here and not section:
            section = clean_heading(toc_here[-1]["title"])
        # Split the page at headings so each block carries its own section label.
        cuts = [m.start() for m in HEADING.finditer(text)]
        bounds = [0] + [c for c in cuts if c > 0] + [len(text)]
        for a, b in zip(bounds, bounds[1:]):
            block = text[a:b]
            m = HEADING.match(block)
            if m:
                section = clean_heading(m.group(1)) or section
            for piece in split_text(block):
                if len(piece) < 40:  # bare headings / page furniture
                    continue
                chunks.append({
                    "document": doc["filename"],
                    "page": page["page"],
                    "section": section,
                    "text": piece,
                })
    return chunks


if __name__ == "__main__":
    # Self-check: splitting respects the size cap and keeps all content.
    s = "\n\n".join(f"para {i} " + "x" * 300 for i in range(20))
    parts = split_text(s)
    assert all(len(p) <= CHUNK_CHARS for p in parts)
    assert parts[0].startswith("para 0") and parts[-1].endswith("x")
    doc = {"filename": "t.pdf", "toc": [], "pages": [
        {"page": 1, "text": "#### **3.1 Timers**\nTIM2 is a 32-bit general purpose timer with 4 channels."},
        {"page": 2, "text": "Continued text about TIM2 auto-reload and prescaler registers."},
    ]}
    c = chunk(doc)
    assert [x["section"] for x in c] == ["3.1 Timers", "3.1 Timers"] and c[1]["page"] == 2, c
    print("ingest OK")
