import json
from pathlib import Path

import fitz
import pymupdf4llm


# ============================================================
# PATHS
# ============================================================

INPUT_PATH = Path("../dataset/raw/")
OUTPUT_PATH = Path("../dataset/processed_pymupdf/")


# ============================================================
# HELPERS
# ============================================================

def extract_document(pdf_path):
    """
    Extract one PDF into a normalized document structure.

    PyMuPDF:
        - PDF metadata
        - native PDF TOC/bookmarks

    PyMuPDF4LLM:
        - page-aware Markdown
        - TOC items associated with each page
    """

    print(f"\nProcessing: {pdf_path.name}")

    # --------------------------------------------------------
    # Open PDF
    # --------------------------------------------------------

    doc = fitz.open(pdf_path)

    print(f"  Pages: {len(doc)}")

    # --------------------------------------------------------
    # Native PDF TOC
    # --------------------------------------------------------

    native_toc = doc.get_toc()

    print(f"  Native TOC entries: {len(native_toc)}")

    # --------------------------------------------------------
    # PyMuPDF4LLM extraction
    # --------------------------------------------------------

    pages = pymupdf4llm.to_markdown(
        doc,
        page_chunks=True
    )

    print(f"  Extracted pages: {len(pages)}")

    # --------------------------------------------------------
    # Normalize pages
    # --------------------------------------------------------

    normalized_pages = []

    for i, page in enumerate(pages):

        normalized_pages.append({
            "page": i + 1,

            "text": page.get(
                "text",
                ""
            ),

            "toc_items": page.get(
                "toc_items",
                []
            )
        })

    # --------------------------------------------------------
    # Determine TOC source
    # --------------------------------------------------------

    if native_toc:
        toc_source = "native"
    else:
        toc_source = "none"

    # --------------------------------------------------------
    # Build normalized document
    # --------------------------------------------------------

    document = {
        "filename": pdf_path.name,

        "metadata": {
            "title": doc.metadata.get("title"),
            "author": doc.metadata.get("author"),
            "subject": doc.metadata.get("subject"),
            "keywords": doc.metadata.get("keywords"),
        },

        "page_count": len(doc),

        "toc_source": toc_source,

        "toc": [
            {
                "level": item[0],
                "title": item[1],
                "page": item[2]
            }
            for item in native_toc
        ],

        "pages": normalized_pages
    }

    doc.close()

    return document


# ============================================================
# MAIN
# ============================================================

def main():

    OUTPUT_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    pdf_files = sorted(
        INPUT_PATH.glob("*.pdf")
    )

    print("=" * 70)
    print("PDF EXTRACTION")
    print("=" * 70)

    print(f"Found {len(pdf_files)} PDFs.")

    if not pdf_files:
        print("No PDFs found.")
        return

    native_count = 0
    no_toc_count = 0

    # --------------------------------------------------------
    # Process documents
    # --------------------------------------------------------

    for pdf_path in pdf_files:

        document = extract_document(
            pdf_path
        )

        # ----------------------------------------------------
        # Statistics
        # ----------------------------------------------------

        if document["toc_source"] == "native":
            native_count += 1
        else:
            no_toc_count += 1

        # ----------------------------------------------------
        # Output filename
        # ----------------------------------------------------

        output_file = (
            OUTPUT_PATH /
            f"{pdf_path.stem}.json"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                document,
                f,
                indent=2,
                ensure_ascii=False
            )

        print(
            f"  Saved: {output_file.name}"
        )

    # ========================================================
    # SUMMARY
    # ========================================================

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"Documents processed : {len(pdf_files)}")
    print(f"Native TOC          : {native_count}")
    print(f"No native TOC       : {no_toc_count}")

    print()
    print(f"Output: {OUTPUT_PATH}")
    print("=" * 70)


if __name__ == "__main__":
    main()