#copying files
# import shutil,os
# from pathlib import Path
# p = Path("D:\\Koenig\\koenig-python courses\\Python Automation Bootcamp")
# print(p)
# shutil.copy(p/'Python.txt',p/'WorkingFiles',)

#working with ZIP files
import zipfile,os
from pathlib import Path
p = Path("D:\\Koenig\\koenig-python courses\\Python Automation Bootcamp")
myFileZip = zipfile.ZipFile(p/'myFile.zip')
print(myFileZip.namelist())

