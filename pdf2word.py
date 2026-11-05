"""Convert a PDF into an editable Word document."""

import argparse
from pathlib import Path

from pdf2docx import Converter


def convert(source: Path, destination: Path) -> None:
    converter = Converter(str(source))
    try:
        converter.convert(str(destination))
    finally:
        converter.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to Word")
    parser.add_argument("pdf", type=Path, help="input PDF file")
    parser.add_argument("docx", type=Path, nargs="?", help="output Word file")
    args = parser.parse_args()
    convert(args.pdf, args.docx or args.pdf.with_suffix(".docx"))
