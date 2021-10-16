import PyPDF2
import csv
from tika import parser


def createCsv(data):
    with open('export.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(data)):
            spamwriter.writerow([i, data[i]])


def handleRaw(raw):
    # creates list of strings separated by new lines
    output_list = raw.splitlines()
    # removes all empty lines and white spaces items
    output_list = [it for it in output_list if it.strip()]
    return output_list


def readPDFTika(filePath):
    raw = parser.from_file(filePath)
    print
    print(raw['content'])
    print('-------------------')
    print(raw['metadata'])
    return raw['content']


def readPDFTikaXml(filePath):
    raw = parser.from_file(filePath, xmlContent=True)
    print
    print(raw['content'])
    print('-------------------')
    print(raw['metadata'])
    return raw


def readPDF(filePath):
    # creating a pdf file object
    pdfFileObj = open(filePath, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    # creating a page object
    pageObj = pdfReader.getPage(0)
    # extracting text from page
    print(pageObj.extractText())
    # closing the pdf file object
    pdfFileObj.close()


def doMe(filePath):
    print('hello ' + filePath)


if __name__ == '__main__':
    filePath = input("PDF File Path: ") or "resource/statement2.pdf"
    doReadPDF = input("read pdf? y/n ") or "y"
    if doReadPDF == "y":
        # result = readPDF(filePath)
        raw = readPDFTika(filePath)
        # result = readPDFTikaXml(filePath)
        data = handleRaw(raw)
        createCsv(data)

    else:
        doMe(filePath)
    print('done')
