from PyPDF2 import PdfFileReader


def _setup_page_id_to_num(pdf, pages=None, _result=None, _num_pages=None):
    if _result is None:
        _result = {}
    if pages is None:
        _num_pages = []
        pages = pdf.trailer["/Root"].getObject()["/Pages"].getObject()
    t = pages["/Type"]
    if t == "/Pages":
        for page in pages["/Kids"]:
            _result[page.idnum] = len(_num_pages)
            _setup_page_id_to_num(pdf, page.getObject(), _result, _num_pages)
    elif t == "/Page":
        _num_pages.append(1)
    return _result
# main
f = open('testbook.pdf','rb')
p = PdfFileReader(f)
# map page ids to page numbers
pg_id_num_map = _setup_page_id_to_num(p)
o = p.getOutlines()
pg_num = pg_id_num_map[o[0].page.idnum] + 1
print(pg_num)