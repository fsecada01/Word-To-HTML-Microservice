"""
This app is intended to convert existing .docx files into HTML files.  These
functions should extract section and heading data from document files and
convert them to HTML with ease.  Existing files must be formatted correctly
for python-mammoth to effectively parse the files.

Right now, only .docx files are working
"""

import io
from typing import Literal

import mammoth
from mammoth import transforms


def _file_type_conv(
    file_stream: bytes, trans_ele: str or None = None, type_name: str = "html"
):
    stream = io.BytesIO(file_stream)
    return convert_to_format(
        content=stream,
        trans_ele=trans_ele,
        type_name=type_name,
    )


def convert_to_format(
    content: bytes | str | io.BytesIO,
    trans_ele: str | None = None,
    type_name: str = "html",
):
    transform_document = transforms.paragraph(trans_ele) if trans_ele else None
    func_name = f"convert_to_{type_name}"
    result = getattr(mammoth, func_name)(
        content, transform_document=transform_document
    )
    content = result.value
    if result.messages:
        print(result.messages)
    if type_name == "html":
        split_content = [f"<h1>{ele}" for ele in content.split("<h1>") if ele]
    else:
        split_content = content.split("\\")
    return split_content


def file_html_conversion(
    stream: bytes, type_name: Literal["html", "markdown", "text"] = "html"
):
    content_parts = _file_type_conv(stream, type_name=type_name)
    join_str = "," if type_name == "html" else ""
    payload = join_str.join(content_parts)
    return payload
