from PyPDF2 import PdfFileWriter, PdfFileReader
import csv

csvreader = csv.reader(open("./nombres.csv", 'r'))

inputpdf = PdfFileReader(open("Participantes_02.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    name = next(csvreader)[0]
    with open("Constancias//%s.pdf" % name, "wb") as outputStream:
        output.write(outputStream)