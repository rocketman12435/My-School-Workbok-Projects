import sys
import time
choice = input("What do you want to do? ")
if choice == "":
    print("Invalid input: no choice entered")
    sys.exit(0)
num1 = float(input("Enter a number: "))
if num1 == "":
    print("Invalid input: no number entered")
    sys.exit(0)
if num1 == 0 and choice.upper() == "DIVIDE":
    print("Can't divide by zero!")
    sys.exit(0)
num2 = float(input("Enter another number: "))
if num2 == "":
    print("Invalid input: no number entered")
    sys.exit(0)
if num2 == 0 and choice.upper() == "DIVIDE":
    print("Can't divide by zero!")
    sys.exit(0)
if choice.upper() == "SUBTRACT" or choice.upper() == "DIVIDE":
    order = input("What order do you want to perform your calculation in? If you want your first number, the operation, then the second number, please enter 1, and if you want the second number, the operation, then the first number, please enter 2: ")



def add():
        calc = num1+num2
        return calc
def subtract():
    if order == "1":
        calc = num1-num2
        return calc
    if order == "2":
        calc = num2-num1
        return calc
def multiply():
        calc = num1*num2
        return calc
def divide():
    if order == "1":
        calc = num1/num2
        return calc
    if order == "2":
        calc = num2/num1
        return calc
if choice.upper() == "ADD":
    print(num1,"+",num2,"=",add())

if choice.upper() == "SUBTRACT":
    if order == "1":
        print(num1,"-",num2,"=",subtract())
    if order == "2":
        print(num2,"-",num1,"=",subtract())

if choice.upper() == "MULTIPLY":
    print(num1,"x",num2,"=",multiply())

if choice.upper() == "DIVIDE":
        if order == "1":
            print(num1,"-",num2,"=",divide())
        if order == "2":
            print(num2,"-",num1,"=",divide())
