#one1.py
from PyPDF2 import PdfFileReader
import PyPDF2
from pdfrw import PdfReader, PdfWriter

def get_info():
    with open("Data_Mining.pdf", 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()

    Title = info.title
    print(Title)

x=get_info()