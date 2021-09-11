from django import template
import os
from ConversionTool.core import FileHTMLConversion, FileHTMLConvertedParts

register = template.Library()


@register.filter(name="document_load")
def gen_HTML(value):
    base_path = os.path.dirname(os.path.realpath("__file__"))
    proj_path = base_path + "/backend/storage/private/Curated_Files/"
    file_loc = proj_path + value
    html_payload = FileHTMLConversion(file_loc)
    return html_payload[0]
    # return ','.join(html_payload[0])


@register.filter(name="document_parts_load")
def gen_HTML_Parts(value):
    base_path = os.path.dirname(os.path.realpath("__file__"))
    proj_path = base_path + "/backend/storage/private/Curated_Files/"
    file_loc = proj_path + value
    html_payload = FileHTMLConvertedParts(file_loc)
    return html_payload[0]
