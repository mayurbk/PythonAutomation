#os module, pathlib
#creating a new folder
import os ,pathlib
# os.makedirs('D:\\Koenig\\koenig-python courses\\Python Automation Bootcamp\\WorkingFiles\\Testing') ##absolute path
# print('Folder created Successfully. Please check Path.')
# os.makedirs("WorkingFiles")    ##relative path
# print('Folder created Successfully. Please check Path.')
path = pathlib.Path('D:\\Koenig\\koenig-python courses\\Python Automation Bootcamp')
# print(path.anchor)
# print(path.name)
# print(path.drive)
# size = os.path.getsize('D:\\Koenig\\koenig-python courses\\Python Automation Bootcamp\\Course content.pdf')
# print("Size of the file is" ,size ,"bytes")
print(os.listdir("D:\\Koenig\\koenig-python courses\\Python Automation Bootcamp"))
print(list(path.glob('*.pptx')))