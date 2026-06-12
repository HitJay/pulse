#!/usr/bin/env python3
"""Render a Markdown resume to a clean, professional A4 PDF via headless Chromium."""
import sys
import pathlib
import markdown
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
CSS = (HERE.parent / "assets" / "resume.css").read_text(encoding="utf-8")

FOOTER = (
    '<div style="font-size:8px;color:#9aa0a6;width:100%;text-align:center;'
    'font-family:Arial,sans-serif;">'
    '<span class="pageNumber"></span> / <span class="totalPages"></span></div>'
)


def convert(md_path: pathlib.Path, pdf_path: pathlib.Path) -> None:
    body = markdown.markdown(
        md_path.read_text(encoding="utf-8"),
        extensions=["extra", "sane_lists", "smarty"],
    )
    html = (
        '<!DOCTYPE html><html lang="zh"><head><meta charset="utf-8">'
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page()
        page.set_content(html, wait_until="networkidle")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=FOOTER,
            margin={"top": "12mm", "bottom": "9mm", "left": "15mm", "right": "15mm"},
        )
        browser.close()
    print(f"OK  {md_path.name}  ->  {pdf_path.name}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: md_to_pdf.py <input.md> <output.pdf>")
    convert(pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]))
