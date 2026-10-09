import pymupdf
import pymupdf4llm


PDF = "../dataset/raw/1_STM32F407VG.pdf"


doc = pymupdf.open(PDF)

print("=" * 80)
print("DOCUMENT")
print("=" * 80)

print("Pages:", len(doc))
print("TOC entries:", len(doc.get_toc()))

print("\nFIRST 30 TOC ENTRIES")
print("=" * 80)

for entry in doc.get_toc()[:30]:
    level, title, page = entry

    print(
        f"{level:<3} "
        f"{title:<70} "
        f"PDF page {page}"
    )


print("\n\nEXTRACTING WITH PyMuPDF4LLM...")
print("=" * 80)

# TocHeaders uses the PDF's actual internal TOC
# to determine Markdown heading levels.
pymupdf4llm.use_layout(False)

headers = pymupdf4llm.TocHeaders(doc)

md = pymupdf4llm.to_markdown(
    doc,
    hdr_info=headers
)

with open(
    "../dataset/test_stm32f407.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(md)

print("Saved:")
print("../dataset/test_stm32f407.md")

print("\nFIRST 5000 CHARACTERS")
print("=" * 80)
print(md[:5000])