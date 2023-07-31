#234-444-3224 #\d\d\d-\d\d\d-\d\d\d\d

# def isPhnNumber(x):
#     if len(x) != 12:
#         return False
#     for i in range(0,3):
#         if not x[i].isdecimal():
#             return False
#     if x[3] != '-':
#         return False
#     for i in range(4,7):
#         if not x[i].isdecimal():
#             return False
#     if x[7] !='-':
#         return False
#     for i in range(8,12):
#         if not x[i].isdecimal():
#             return False
#
#     return True
#
# print('enter a phone number')
# phnno = input()
# print(isPhnNumber(phnno))

##Creating a regex object
import re
# phonenumber = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #search #(\d\d\d)-(\d\d\d)-(\d\d\d\d)
# testvalue = phonenumber.search("Call me at 452-556-9896 today at 5 pm.") ##getting stored in a match object.
# print("Phone number is:"+testvalue.group()) #match object has a group method it returns actual matched value/text

phNo = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
tValue = phNo.search("Call me at 452-556-9896 today at 5 pm.")
print(tValue.groups())  ## gives us a tuple value of the matched object.
area = tValue.group(1)
#areaCode, Number = tValue.groups()
print(area)

