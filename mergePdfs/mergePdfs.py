#! /usr/bin/python3

import glob, PyPDF2

''' Script which merges all the PDF files in the current directory into 
a single PDF file
Usage: on the terminal run the following- python3 mergePdfs.py
A new file combinedPDF.pdf will be created which contains the contents of all the pdfs
'''

# Getting the names of all the pdfs in current directory
pdflist = [pdf for pdf in glob.glob('*.pdf')]

# Creating a writer object
writer = PyPDF2.PdfFileWriter()

# Looping through all the pdfs
for fileName in pdflist:
	
	# Opening pdf and creating a reader file
	pdfFile = open(fileName, 'rb')
	reader = PyPDF2.PdfFileReader(pdfFile)
	
	# Looping through all the pages and adding in writer object
	for pageNo in range(reader.numPages):
		page = reader.getPage(pageNo)
		writer.addPage(page)
	
# Creating a combined pdf file
combined = open('combinedPDF.pdf', 'wb')
writer.write(combined)
combined.close()
