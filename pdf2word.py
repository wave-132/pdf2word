"""Convert a PDF into an editable Word document."""

import argparse
import io
from pathlib import Path

import pymupdf
from docx import Document
from docx.enum.section import WD_SECTION
from docx.shared import Pt
from pdf2docx import Converter


def convert(source: Path, destination: Path, mode: str = "editable", dpi: int = 150) -> None:
    if source.resolve() == destination.resolve():
        raise ValueError("Input and output must be different files")
    if mode == "appearance":
        convert_appearance(source, destination, dpi)
        return
    converter = Converter(str(source))
    try:
        converter.convert(str(destination))
    finally:
        converter.close()


def convert_appearance(source: Path, destination: Path, dpi: int) -> None:
    """Place each rendered PDF page on a Word page of the same size."""
    document = Document()
    with pymupdf.open(source) as pdf:
        for index, page in enumerate(pdf):
            section = document.sections[0] if index == 0 else document.add_section(WD_SECTION.NEW_PAGE)
            section.page_width, section.page_height = Pt(page.rect.width), Pt(page.rect.height)
            section.left_margin = section.right_margin = Pt(0)
            section.top_margin = section.bottom_margin = Pt(0)
            section.header_distance = section.footer_distance = Pt(0)
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.space_before = Pt(0)
            paragraph.paragraph_format.space_after = Pt(0)
            paragraph.paragraph_format.line_spacing = 1
            image = io.BytesIO(page.get_pixmap(dpi=dpi, alpha=False).tobytes("png"))
            paragraph.add_run().add_picture(image, width=section.page_width, height=section.page_height)
    document.save(destination)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to Word")
    parser.add_argument("pdf", type=Path, help="input PDF file")
    parser.add_argument("docx", type=Path, nargs="?", help="output Word file")
    parser.add_argument("--mode", choices=("editable", "appearance"), default="editable",
                        help="editable text (default) or page images for closer appearance")
    parser.add_argument("--dpi", type=int, choices=range(72, 301), default=150, metavar="72-300",
                        help="image resolution for appearance mode (default: 150)")
    args = parser.parse_args()
    convert(args.pdf, args.docx or args.pdf.with_suffix(".docx"), args.mode, args.dpi)
