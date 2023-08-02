# #use of metacharacters
import re
#
# PipeChar = re.compile(r"Java|Python") # OR , returns the first matcch found.
# Pobj = PipeChar.search("I like the programming of Python.I can also work on Java.But Python is my favorite")
# print(Pobj.group())
#
# Pobj = PipeChar.findall("I like the programming of Python.I can also work on Java.But Python is my favorite")
# print(Pobj)  #findall returns a list value of all the matching strings.
#
# # working with ? the optional character in any pattern
# woChar = re.compile(r'(im)?possible')
# woObj = woChar.search("This is quite an impossible task.")
# woObj2 = woChar.search("This is very much possible.")
# print(woObj.group())
# print(woObj2.group()) # matching salutation for name inputs.
#
# #working with asterisk(*). Matches zero or more value
# asteriskChr = re.compile(r'(im)*possible')
# astrkObj  = asteriskChr.findall("This is  of doing the  in  way.")
# print(astrkObj)
#
#matching one or more value with +(plus)


# plusReg = re.compile(r'Mission(im)+possible')
# plusObj = plusReg.search('The adventures of Missionimpossible')
# print(plusObj.group())
# plusObj1  = plusReg.search('the adventures of Missionpossible')

#specific repetations with braces

haRegex = re.compile(r'(ha){1}')
haObj = haRegex.search("he is laughing hahaha")
print(haObj.group())
