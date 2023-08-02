# while True:
#     print('enter your age:')
#     age = input()
#     try:
#         age = int(age)
#     except:
#         print('Please use numeric inputs')
#         continue
#
#     if age < 1:
#         print("Please enter a valid age.")
#         continue
#
#     break
#
# print(f'your age is {age}.')
#
import pyinputplus
##Using the PyInputPlus module to do automatic input validation.
import pyinputplus as pyin

# age = pyinputplus.inputNum(prompt="enter your age:")
# print(age)
# email = pyinputplus.inputEmail(blank=True)
# print(email)

##min,max, greater than,less than
# response = pyinputplus.inputNum('enter a number:', min=5,blank=True)
# response2 = pyinputplus.inputNum('enter a number:',greaterThan=10)
# comparing = pyin.inputNum('>',min=2,lessThan=10)

##working with the timelimit and timeout
# ans1 = pyin.inputNum('enter a number',limit=3,default="you have exceeded your chances.")
# print(ans1)
# ans2 = pyin.inputNum('enter a value',timeout=10,default="Duration timed out!")
# print(ans2)

##creating our own custom functions for validation
def addTen(numbers):
    numList = list(numbers)
    for i, digit in enumerate(numList):
        numList[i]=int(digit)
    if sum(numList) !=10    :
        raise Exception('The digits must add upto 10, not %s' %(sum(numList)))
        return int(numbers)

sumcheck = pyin.inputCustom(addTen)      ## higher order functions- functions whose argument is a function - lambda, map, filter, reduce, decorator, monkeypatching
print(sumcheck)