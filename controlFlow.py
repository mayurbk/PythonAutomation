## Blocks of code
# Age = int(input("Enter age:"))
# if Age <= 18 :
#     print("You are under age.")
# elif Age <= 28:
#     print("You are eligible for work but not for migration.")
#
# else:
#     print('You are eligible for all.')

Name = input("Enter name:")
Psw = input("enter password:")

if Name == "admin" and Psw == "Pa$$w0rd":
    print("change password")

elif Psw == 'Pa$$w0rd':
    print("Access granted !")

else:
    print("Access Denied.")