import io

import mammoth
from mammoth import transforms

"""
This app is intended to convert existing .docx files into HTML files.  These
functions should extract section and heading data from document files and
convert them to HTML with ease.  Existing files must be formatted correctly
for python-mammoth to effectively parse the files.

Right now, only .docx files are working
"""


def _file_type_conv(
    file_stream: bytes, trans_ele=None, type_name: str = "html"
):
    stream = io.BytesIO(file_stream)
    transform_document = transforms.paragraph(trans_ele) if trans_ele else None
    func_name = f"convert_to_{type_name}"
    result = getattr(mammoth, func_name)(
        stream, transform_document=transform_document
    )
    content = result.value
    if result.messages:
        print(result.messages)
    if type_name == "html":
        split_content = [f"<h1>{ele}" for ele in content.split("<h1>") if ele]
    else:
        split_content = content.split("\n")
    return split_content


def file_html_conversion(stream: bytes, type_name: str = "html"):
    content_parts = _file_type_conv(stream, type_name=type_name)
    payload = ",".join(content_parts)
    return payload
