import re

def pswvalid(psw):
    validation = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pattern = re.compile(validation)

    check = re.search(pattern,psw)

    if check:
        print(psw+" Password is valid")
    else:
        print(psw+" password invalid")

listpsw = ['Ab@3','ABDc@3344',"aCb#23$","DDDD9990"]

for i in listpsw:
    pswvalid(i)