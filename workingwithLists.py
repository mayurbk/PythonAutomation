# mylist=[]
# for i in range(1,4):
#     print("enter value:")
#     x = input()
#     mylist.append(x)
#     print(mylist)




#tuple
# mytuple = ('rose','lotus',59,60,True)
# print(mytuple)   ##tuples are immutable
#
# #convert tuples into lists
# mylist=list(mytuple)
# print(type(mylist))
# mylist[3]='changes'
# mytuple=tuple(mylist)
# print(type(mytuple))
import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

reply = (messages[random.randint(0, len(messages) - 1)])
if reply == 'Yes definitely':
    print("please go ahead")
else:
    print(reply)

list1 = ['cat','elephant','zebra','ant','dogs']
list1.sort()
print(list1)


##write a program to check if each number in a list is a prime. Return true if it is.
num1 = int(input("enter number"))
if num1 > 1:
    for i in range (2,int(num1/2)+1): ## 1, 2, 3, 5, 7, 11, 19, 23, 29, 31
        if(num1%i)== 0:
            print(num1, "is not a prime number.")
            break
    else:
        print(num1,"is a prime number.")
else:
    print(num1,"is not a prime number.")