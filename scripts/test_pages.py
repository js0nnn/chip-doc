import pymupdf
import pymupdf4llm


PDF = "../dataset/raw/1_STM32F407VG.pdf"


print("=" * 80)
print("PyMuPDF4LLM VERSION")
print("=" * 80)

print(pymupdf4llm.__version__ if hasattr(pymupdf4llm, "__version__") else "unknown")


doc = pymupdf.open(PDF)

print("\nPages:", len(doc))
print("PDF TOC entries:", len(doc.get_toc()))


# ============================================================
# PAGE CHUNKS
# ============================================================

print("\nExtracting page chunks...")

pages = pymupdf4llm.to_markdown(
    doc,
    page_chunks=True
)

print("Returned pages:", len(pages))


# ============================================================
# FIRST PAGE
# ============================================================

print("\n" + "=" * 80)
print("FIRST PAGE")
print("=" * 80)

page = pages[0]

print("\nKEYS:")
print(page.keys())

print("\nMETADATA:")
print(page["metadata"])

print("\nTOC ITEMS:")
print(page["toc_items"])

print("\nTEXT:")
print(page["text"][:2000])


# ============================================================
# FIND PAGES WITH TOC ITEMS
# ============================================================

print("\n" + "=" * 80)
print("PAGES WITH TOC ITEMS")
print("=" * 80)

count = 0

for page in pages:

    toc_items = page.get("toc_items", [])

    if toc_items:

        print(
            f"\nPDF PAGE {page['metadata']['page_number']}"
        )

        for item in toc_items:

            print("   ", item)

        count += 1

        if count >= 30:
            break


# ============================================================
# SAVE RAW PAGE CHUNKS
# ============================================================

import json

with open(
    "../dataset/pymupdf_pages.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        pages,
        f,
        indent=2,
        ensure_ascii=False,
        default=str
    )

print("\nSaved:")
print("../dataset/pymupdf_pages.json")