from PyPDF2 import PdfFileReader
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

fp = open('testbook.pdf', 'rb')
parser = PDFParser(fp)
pdf = PdfFileReader(fp)
document = PDFDocument(parser)
# Get the outlines of the document.
outlines = document.get_outlines()
y=[]
for(level,title,dest,a,se) in outlines:
    i=0
    x= (' '.join(title.split(' ')[0:]))
    y.append(x)
    i+=1

print(y)
