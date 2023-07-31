import RegularExpressions

txt = " Call me at 452-556-9896 today at 5 pm."

for i in range(len(txt)):
    y = txt[i:i+12]
    if RegularExpressions.isPhnNumber(y):
        print("Phone number found :" +y)

print("fetch successfully.")