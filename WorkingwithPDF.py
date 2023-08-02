#reading from pdf / extracting text from pdf
import PyPDF2

# pdfObject = open('C:\\Users\\mayur\\Downloads\\Automate_the_Boring_Stuff_onlinematerials\\automate_online-materials\\meetingminutes.pdf','rb')
# pdfReader = PyPDF2.PdfReader(pdfObject)
# print(len(pdfReader.pages))
#
from PyPDF2 import PdfReader
# pdfObject1 = PdfReader('C:\\Users\\mayur\\Downloads\\Automate_the_Boring_Stuff_onlinematerials\\automate_online-materials\\meetingminutes.pdf','rb')
# page =  pdfObject1.pages[0]
# print(page.extract_text())

#decrypting and encrypting
pdffile = PyPDF2.PdfReader(open('encrypted.pdf','rb'))
print(pdffile.is_encrypted)

print(pdffile.decrypt('rosebud'))
pageobj = pdffile.pages[0]
print(pageobj.extract_text())