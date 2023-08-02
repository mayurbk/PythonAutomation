import ezsheets
# ss = ezsheets.Spreadsheet('1GfrsbLBiwlvUrgXZ0Oo8dOY1l-iFEFxdiH-eziNRkEc')
# print(ss.title)
#
# #create a google spreadsheet
# newss = ezsheets.createSpreadsheet('python automation')
# print("Your google spreadsheet got created with the name " ,newss.title)

#to upload an existing file

# uploadss = ezsheets.upload('MyExcelFile.xlsx')
# print(uploadss.title)

#download a spreadsheet  gets downloaded in the project folder.
# ssdownload = ezsheets.Spreadsheet('1cEJLSUZg0yZDpJoYDuJrYEehaP37y0Nr4n1HYNV8l7s')
# print(ssdownload.title)
# print(ssdownload.downloadAsExcel)

#reading and writing data
sswrite = ezsheets.Spreadsheet('1cEJLSUZg0yZDpJoYDuJrYEehaP37y0Nr4n1HYNV8l7s')
sheet = sswrite[0]
print(sheet.title)
sheet['A1'] = 'Name'
sheet['B1'] = 'Course'
sheet['C1'] = 'Duration'
sheet['A2'] = 'John'
sheet['B2'] = 'Python'
sheet['C2'] = '20 hours'