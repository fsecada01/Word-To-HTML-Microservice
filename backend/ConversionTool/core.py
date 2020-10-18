import mammoth
from mammoth import transforms
import io

"""
This app is intended to convert existing .docx files into HTML files.  These
functions should extract section and heading data from document files and
convert them to HTML with ease.  Existing files must be formatted correctly
for python-mammoth to effectively parse the files.

Right now, only .docx files are working
"""


def _file_html_conv(file_stream: bytes, trans_ele=None):
    stream = io.BytesIO(file_stream)
    transform_document = transforms.paragraph(trans_ele) if trans_ele else None
    result = mammoth.convert_to_html(
        stream, transform_document=transform_document
    )
    html = result.value
    if result.messages:
        print(result.messages)
    split_html = [f"<h1>{ele}" for ele in html.split("<h1>") if ele != ""]

    return split_html


def FileHTMLConversion(stream: bytes):
    html_parts = _file_html_conv(stream)
    payload = ",".join(html_parts)
    return payload
