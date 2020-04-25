from os import listdir
from os.path import isfile, join

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

merger = PdfFileMerger()
files_folder = 'files/'
with open('merged.pdf', 'wb') as f:
    files = [f for f in listdir(files_folder) if isfile(join(files_folder, f)) and 'watermark' not in f]
    for file in files:
        with open(f'{files_folder}{file}', 'rb') as pdf_file:
            merger.append(PdfFileReader(f'{files_folder}{file}'))
    merger.write(f)

merger.close()
watermark_file = PdfFileReader(f'{files_folder}watermark.pdf')
merged_file = PdfFileReader('merged.pdf')

with open('watermark.pdf', 'wb') as f:
    output = PdfFileWriter()
    for page in range(merged_file.getNumPages()):
        merged_page = merged_file.getPage(page)
        merged_page.mergePage(watermark_file.getPage(0))
        output.addPage(merged_page)
    output.write(f)
