#! python3
# combinePdfs.py - Combines all the PDFs in the current
# working directory into a single PDF.

import PyPDF2, os

# Get all the PDF filenames in directory.
pdfFiles = [] # empty list

for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Loop through all the pages(except the 1st) and add them
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)


# Save the resulting PDF into a file
pdfOutput = open('allminutes4.pdf','wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
