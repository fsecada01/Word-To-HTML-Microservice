from typing import Literal

import html2text

from backend.ConversionTool.core import file_html_conversion

tokens = [
    # tokens as static list; intended to avoid the need for DB management
    "this_is_a_token",
    "secondary_token",
    "random_token",
]


def iter_doc_parts(document, style_name):
    paragraphs = document.paragraphs
    headers = [
        p.style.name
        for p in paragraphs
        if p.style.name.startswith(style_name) is True
    ]
    return headers


def iterate_document_sections(document):
    paragraphs = [document.paragraphs[0]]
    for p in document.paragraphs[1:]:
        if p.style.name.startswith("Heading") is True:
            yield paragraphs
            paragraphs = [p]
            continue
        paragraphs.append(p)
    yield paragraphs


def transform_paragraph(element):
    if element.alignment == "center" and not element.style_id:
        return element.copy(style_id="Heading2")
    else:
        return element


def process_file(
    file: str or bytes, type_name: Literal["html", "markdown", "text"] = "html"
):
    if isinstance(file, str):
        with open(file, "rb+") as f:
            bytes_stream = f.read()
    else:
        bytes_stream = file
    html_payload = file_html_conversion(bytes_stream, type_name=type_name)
    return str(html_payload)


def str_conversion(
    content: str, type_name: Literal["html", "markdown", "text"] = "html"
):
    converter = html2text.HTML2Text()
    converter.ignore_links = True

    content = converter.handle(content)

    return content
