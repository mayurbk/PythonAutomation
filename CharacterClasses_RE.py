#making character classes
import re

vowelRegex  = re.compile(r'[aeiouAEIOU]')
ObjVowel = vowelRegex.findall("This is a very warm Day in the Month .")
print(ObjVowel)

#caret(^) and dollar($)
beginChr = re.compile(r"^welcome.*class$")  #must always be used with double quotes.
beginObj = beginChr.search("welcome to the class")
print(beginObj)

txt = "Hello and welcome to the python course"
x = re.search("^Hello.*course$",txt)
if x:
      print("yes")
else:
      print("no")

#wildcard character(.)
alReg  = re.compile(r'.al')
alObj = alReg.findall("There is a call to be done to all ")
print(alObj)

