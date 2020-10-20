import PyPDF2
pdf1File = open('Data_Mining.pdf', 'rb')
pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(0,1):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutputFile = open('Bookc.pdf', 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdf1File.close()