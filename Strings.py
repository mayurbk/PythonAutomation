## This is Bob's cat.
print("This is Bob\'s cat")  #escape character
## Multiple strings
print('''
Hi this is bob's cat. he is good .

All good.
Thanking you
Your's sincerely
Bob.

''')
myword = 'I like python'
print(myword[3])

#in and not operator

Myline = "This is my favorite programming language"
print('.' not in Myline)

lang = "     python"
print("My favorite language is %s" %(lang))

#Methods of strings.
print(lang.upper())
print(lang.split('o'))
print(lang.isalnum())
print(lang)
print(lang.strip())
#Join
x = '*'.join(['a','b','c'])

print(ord('B'))
print(chr(66))

import pyperclip
pyperclip.copy('Hello')
print(pyperclip.paste())

## write a program to validate the input for setting a password. password should contain atleast a character, a numeric, a upper case character
# not special character.Minimum letters should be 8.
print("password".split(' '))
