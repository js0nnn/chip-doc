import json
import re
from pathlib import Path


# ============================================================
# CONFIG
# ============================================================

INPUT_DIR = Path("../dataset/processed_pymupdf")
OUTPUT_DIR = Path("../dataset/chunks")
OUTPUT_FILE = OUTPUT_DIR / "chunks.json"

# Maximum characters per chunk
MAX_CHARS = 8000

# Overlap between split chunks
OVERLAP_CHARS = 500


# ============================================================
# TEXT HELPERS
# ============================================================

def clean_title(title):
    """Normalize TOC titles."""

    if not title:
        return ""

    title = title.replace("\xa0", " ")
    title = re.sub(r"\s+", " ", title)

    return title.strip()


def normalize_text(text):
    """Light cleanup without destroying document structure."""

    if not text:
        return ""

    text = text.replace("\x00", "")
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Remove excessive blank lines
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text.strip()


# ============================================================
# HIERARCHY
# ============================================================

def build_hierarchy(toc, index):
    """
    Build hierarchy using native TOC levels.

    Example:

        8. AVR Memories
            8.3 SRAM Data Memory
                8.3.1 Data Memory Access Times

    becomes:

        [
            "8. AVR Memories",
            "8.3 SRAM Data Memory",
            "8.3.1 Data Memory Access Times"
        ]
    """

    if index < 0 or index >= len(toc):
        return []

    current = toc[index]

    current_level = current.get("level", 1)

    hierarchy = [
        clean_title(current.get("title", ""))
    ]

    wanted_level = current_level - 1

    # Walk backwards looking for the closest parent
    # at each level.
    for j in range(index - 1, -1, -1):

        item = toc[j]

        item_level = item.get("level", 1)

        if item_level == wanted_level:

            title = clean_title(item.get("title", ""))

            if title:
                hierarchy.append(title)

            wanted_level -= 1

            if wanted_level < 1:
                break

    hierarchy.reverse()

    return hierarchy


# ============================================================
# TEXT SPLITTING
# ============================================================

def split_text(
    text,
    max_chars=MAX_CHARS,
    overlap=OVERLAP_CHARS
):
    """
    Split large text into overlapping chunks.

    Priority:

        1. Paragraph boundary
        2. Line boundary
        3. Sentence-ish boundary
        4. Hard character boundary

    If the section is already <= max_chars,
    return it unchanged.
    """

    text = text.strip()

    if not text:
        return []

    if len(text) <= max_chars:
        return [text]

    chunks = []

    start = 0
    text_length = len(text)

    while start < text_length:

        end = min(
            start + max_chars,
            text_length
        )

        # ----------------------------------------------------
        # Try to find a good boundary
        # ----------------------------------------------------

        if end < text_length:

            # Paragraph boundary
            boundary = text.rfind(
                "\n\n",
                start,
                end
            )

            # Line boundary
            if boundary == -1:
                boundary = text.rfind(
                    "\n",
                    start,
                    end
                )

            # Sentence-ish boundary
            if boundary == -1:
                boundary = text.rfind(
                    ". ",
                    start,
                    end
                )

            # Only accept boundary if it doesn't make
            # the chunk ridiculously small.
            if boundary > start + max_chars * 0.5:

                if text[boundary:boundary + 2] == "\n\n":
                    end = boundary + 2
                else:
                    end = boundary + 1

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        # ----------------------------------------------------
        # Overlap
        # ----------------------------------------------------

        new_start = end - overlap

        # Safety
        if new_start <= start:
            new_start = end

        start = new_start

    return chunks


# ============================================================
# PAGE HELPERS
# ============================================================

def page_map(doc):
    """
    Return:

        page_number -> page object
    """

    result = {}

    for page in doc.get("pages", []):

        page_number = page.get("page")

        if isinstance(page_number, int):
            result[page_number] = page

    return result


def collect_pages(
    page_lookup,
    start_page,
    end_page
):
    """
    Collect page text from start_page through end_page.
    """

    texts = []

    for page_num in range(
        start_page,
        end_page + 1
    ):

        page = page_lookup.get(page_num)

        if not page:
            continue

        text = page.get("text", "")

        if not text:
            continue

        text = normalize_text(text)

        if not text:
            continue

        texts.append(
            f"[Page {page_num}]\n{text}"
        )

    return "\n\n".join(texts)


# ============================================================
# NATIVE TOC SECTION BUILDING
# ============================================================

def build_sections(doc):
    """
    Convert native TOC entries directly into semantic sections.

    IMPORTANT:

    We intentionally create EXACTLY ONE section per valid
    native TOC entry.

    We do NOT create additional sections based on hierarchy.

    This prevents:

        494 TOC entries -> 1050 sections
        1200 TOC entries -> 3997 sections

    Each TOC entry becomes one section.

    Large sections are split later into multiple chunks.
    """

    toc = doc.get("toc", [])

    if not toc:
        return []

    page_count = doc.get(
        "page_count",
        len(doc.get("pages", []))
    )

    sections = []

    # --------------------------------------------------------
    # First collect valid native TOC entries
    # --------------------------------------------------------

    valid_entries = []

    for index, item in enumerate(toc):

        page = item.get("page")

        # Ignore invalid TOC page anchors
        if not isinstance(page, int):
            continue

        if page < 1:
            continue

        title = clean_title(
            item.get("title", "")
        )

        if not title:
            continue

        level = item.get(
            "level",
            1
        )

        valid_entries.append(
            {
                "toc_index": index,
                "title": title,
                "level": level,
                "page": page,
            }
        )

    # --------------------------------------------------------
    # One section per valid TOC entry
    # --------------------------------------------------------

    for i, entry in enumerate(valid_entries):

        start_page = entry["page"]

        # Find the next TOC entry that starts on a
        # DIFFERENT later page.
        #
        # This is important because many child sections
        # share the same page.
        next_page = None

        for j in range(
            i + 1,
            len(valid_entries)
        ):

            candidate_page = valid_entries[j]["page"]

            if candidate_page > start_page:
                next_page = candidate_page
                break

        if next_page is None:

            end_page = page_count

        else:

            end_page = next_page - 1

        # Safety
        if end_page < start_page:
            end_page = start_page

        hierarchy = build_hierarchy(
            toc,
            entry["toc_index"]
        )

        sections.append(
            {
                "toc_index": entry["toc_index"],
                "title": entry["title"],
                "level": entry["level"],
                "start_page": start_page,
                "end_page": end_page,
                "hierarchy": hierarchy,
            }
        )

    return sections


# ============================================================
# DOCUMENT PROCESSING
# ============================================================

def process_document(doc):
    """
    Process one document.

    Returns:

        sections
        chunks
    """

    filename = doc.get(
        "filename",
        "unknown.pdf"
    )

    pages = page_map(doc)

    sections = build_sections(doc)

    chunks = []

    # --------------------------------------------------------
    # Process each semantic section
    # --------------------------------------------------------

    for section in sections:

        text = collect_pages(
            pages,
            section["start_page"],
            section["end_page"]
        )

        if not text:
            continue

        # ----------------------------------------------------
        # Split ONLY if necessary
        # ----------------------------------------------------

        parts = split_text(
            text,
            MAX_CHARS,
            OVERLAP_CHARS
        )

        total_parts = len(parts)

        # ----------------------------------------------------
        # Create chunks
        # ----------------------------------------------------

        for part_index, part_text in enumerate(parts):

            chunk = {
                "document": filename,

                "title": section["title"],

                "hierarchy": section["hierarchy"],

                "level": section["level"],

                "start_page": section["start_page"],

                "end_page": section["end_page"],

                "text": part_text,

                "part": part_index,

                "total_parts": total_parts,

                "toc_index": section["toc_index"],
            }

            chunks.append(chunk)

    return sections, chunks


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("NATIVE TOC SEMANTIC CHUNKING")
    print("=" * 70)

    print(
        f"Input directory : {INPUT_DIR}"
    )

    files = sorted(
        INPUT_DIR.glob("*.json")
    )

    print(
        f"Documents found : {len(files)}"
    )

    print()

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    all_chunks = []

    total_sections = 0

    total_chunks = 0

    # ========================================================
    # PROCESS DOCUMENTS
    # ========================================================

    for path in files:

        print(
            f"Processing: {path.name}"
        )

        try:

            with open(
                path,
                "r",
                encoding="utf-8"
            ) as f:

                doc = json.load(f)

            native_toc_count = len(
                doc.get("toc", [])
            )

            sections, chunks = process_document(
                doc
            )

            print(
                f"  Native TOC entries : "
                f"{native_toc_count}"
            )

            print(
                f"  Semantic sections   : "
                f"{len(sections)}"
            )

            print(
                f"  Chunks created      : "
                f"{len(chunks)}"
            )

            # ------------------------------------------------
            # Sanity check
            # ------------------------------------------------

            if len(sections) > native_toc_count:

                print(
                    "  WARNING: semantic section "
                    "count exceeds native TOC count!"
                )

            print()

            total_sections += len(sections)

            total_chunks += len(chunks)

            all_chunks.extend(chunks)

        except Exception as e:

            print(
                f"  ERROR: {e}"
            )

            print()

    # ========================================================
    # OUTPUT
    # ========================================================

    output = {

        "metadata": {

            "chunking_method":
                "native_toc_semantic",

            "max_chars":
                MAX_CHARS,

            "overlap_chars":
                OVERLAP_CHARS,

            "documents":
                len(files),

            "semantic_sections":
                total_sections,

            "total_chunks":
                total_chunks,
        },

        "data":
            all_chunks,
    }

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            output,
            f,
            ensure_ascii=False,
            indent=2
        )

    # ========================================================
    # SUMMARY
    # ========================================================

    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(
        f"Documents processed : "
        f"{len(files)}"
    )

    print(
        f"Semantic sections   : "
        f"{total_sections}"
    )

    print(
        f"Total chunks        : "
        f"{total_chunks}"
    )

    print(
        f"Output              : "
        f"{OUTPUT_FILE}"
    )

    print("=" * 70)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()