from backend.ConversionTool.core import FileHTMLConversion

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


def process_file(file: str or bytes):
    if type(file) is str:
        with open(file, "rb+") as f:
            bytes_stream = f.read()
    else:
        bytes_stream = file
    html_payload = FileHTMLConversion(bytes_stream)
    return str(html_payload)
