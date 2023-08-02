# ## while keyword, a condition, block of statement, else block
# num = 0
# while num < 10:
#     num = num+1
#     if num == 5:
#         pass
#         print("This is a pass statement.")
#     print("This is not a while loop", num)
# print("This is enough.")
#
# while True:
#     print("who are you?")
#     name = input()
#     if name != "John":
#         continue
#     print("Hello John. Give the password.")
#     password = input()
#     if password == 'pa$$w0rd':
#             break
# print("Access granted.")
#For Loop, range() for a value in range
for i in range(3):
    print("Python")

total = 0
for num in range(50):
    total = total + num
print(total)

name = "python"
for i in name:
    if i == 'h':
        break
    print(i)
#random