import PyPDF2
original = PdfReader("mypdf.pdf")
output = PdfWriter()
# duplicate all pages
for page in original.pages:
   output.addpage(page)
   output.addpage(page)
output.write("new_file.pdf")