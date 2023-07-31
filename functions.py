#creating a simple calculator function
# def add(x,y):
#     return x+y
#
# def sub(x,y):
#     if y>x:
#         print("Please put a greater number first.")
#     else:
#         return x-y
#
# def mul(x,y):
#     return x*y
#
# def div(x,y):
#     if y == 0:
#         print("Cannot divide by zero.")
#     else:
#         return x/y

#call stack in functions
# def a():
#     print('a() starts')
#     b()
#     d()
#     print("a() returns")
#
# def b():
#     print('b() starts')
#     c()
#     print('b() returns')
#
# def c():
#     print('c() starts')
#     print('c() returns')
#
# def d():
#     print('d() starts')
#     print('d() returns')
#
# a()

#Local and Global Scope
# def func1():
#     global num1
#     num1 = 244
#
# func1()
# print(num1)

#exception handling

# try:
#     def func1(a,b):
#         try:
#             return a/b
#         except ZeroDivisionError:
#             print("cannot divide by zero.")
# except TypeError:
#         print("Please put a argument.")
#
# func1()

##Write a function that has one parameter named number.If number is even, function returns number//2 and return the value.
##If number is odd, it returns  3*number +1. Take this number as an input parameter.
def genfunc():
    yield 'this is line1'
    yield 'this is line2'
    yield 'this is line3'

obj1 = genfunc()
print(next(obj1))
print(next(obj1))
#generator function with the yield statement.