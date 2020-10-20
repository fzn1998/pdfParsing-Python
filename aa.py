from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from PyPDF2 import PdfFileReader


def text_extractor(path,Toc):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        total_pageno=pdf.getNumPages()
        for i in range(0,total_pageno):
            page = pdf.getPage(i)
            text = page.extractText()


            #print(text)
            for single_content in Toc:
                if single_content in text:
                        print(text)
if __name__ == '__main__':

    fp = open('Data_Mining.pdf', 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    # Get the outlines of the document.
    outlines = document.get_outlines()
    Toc = [] #Table Of content
    for (level, title, dest, a, se) in outlines:
        i = 0
        x = (' '.join(title.split(' ')[0:]))
        Toc.append(x)
        i += 1
    path = 'Data_Mining.pdf'
    text_extractor(path, Toc)
