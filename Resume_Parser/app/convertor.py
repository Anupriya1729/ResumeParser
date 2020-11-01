from io import StringIO
from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import HTMLConverter, TextConverter, XMLConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
import io
import os
import sys
import getopt



def convert(fname, pages=None):
        if not pages:
                pagenums = set()
        else:
                pagenums = set(pages)
        manager = PDFResourceManager()
        codec = 'utf-8'
        caching = True
        output = io.StringIO()
        converter = TextConverter(
            manager, output, codec=codec, laparams=LAParams())

        interpreter = PDFPageInterpreter(manager, converter)
        infile = open(fname, 'rb')

        for page in PDFPage.get_pages(infile, pagenums, caching=caching, check_extractable=True):
          interpreter.process_page(page)

        convertedPDF = output.getvalue()

        infile.close()
        converter.close()
        output.close()
        return convertedPDF


def convert_pdf_to_txt(path_to_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    co = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=co,laparams=laparams)
    path_=os.getcwd()+path_to_file
    print(path_)
    fp = open(path_, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
          interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parentdir = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    mediadir = os.path.join(BASE_DIR, "media")
    txtdir = os.path.join(mediadir, "textfiles")
    
    base= os.path.basename(path_to_file)
    fileNAME = os.path.splitext(base)[0]
    fileTXT = fileNAME+'.txt'
    filePDF = fileNAME+'.pdf'
    filetxtpath =  os.path.join(txtdir, fileTXT)
    filePDF = os.path.join(mediadir, filePDF)

    print(filePDF)
    convertedPDF = convert(filePDF, pages=None)
    fileConverted = open(filetxtpath, 'w+', encoding="utf-8")
  ######## EITHER
    fileConverted.write(convertedPDF)
    fileConverted.close()
    return text
    #print(convertedPDF)

  ######## OR
  #convertedPDF=convert_pdf_to_txt(filePDF)
  #fileConverted = open(fileTXT, "w", encoding="utf-8")
  #fileConverted.write(convertedPDF)
  #fileConverted.close()


