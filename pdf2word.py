"""Extract PDF text into an editable Word document."""

import argparse
from pathlib import Path

import fitz
from docx import Document


def convert(source: Path, destination: Path) -> None:
    document = Document()
    with fitz.open(source) as pdf:
        for index, page in enumerate(pdf):
            if index:
                document.add_page_break()
            for block in page.get_text("blocks", sort=True):
                text = block[4].strip()
                if text:
                    document.add_paragraph(text)
    document.save(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF text to Word")
    parser.add_argument("pdf", type=Path, help="input PDF file")
    parser.add_argument("docx", type=Path, nargs="?", help="output Word file")
    args = parser.parse_args()
    convert(args.pdf, args.docx or args.pdf.with_suffix(".docx"))
