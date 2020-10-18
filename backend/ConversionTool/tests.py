import os
import docx
from secretary import Renderer
from backend.apps.ConversionTool import iter_doc_parts, iterate_document_sections

# Create your tests here.

# map to test file location
file_name = 'ISP.docx'
new_file_name = 'ISP.odt'
file_path = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))
file_path += '/storage/private/test_files/TBI_ISP_Forms'
file_loc = os.path.join(file_path, file_name)
new_file_loc = os.path.join(file_path, new_file_name)


def renderer_test(file_loc):
    renderer_test = Renderer().render(new_file_loc, data={})
    return renderer_test


def docx_section_test(file_loc):
    test_doc = docx.Document(file_loc)
    test_sections = iterate_document_sections(test_doc)
    test_sections = list(test_sections)

    for s in test_sections:
        for p in s:
            return [ele.strip() for ele in p.text.split(
                ',') if ele != '' and ele is not None]


def docx_headers_test(file_doc):
    headers = iter_doc_parts(file_doc, 'Heading')
    return headers
