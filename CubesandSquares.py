import time
import sys
numbers = []
def cube():
    number = input("Enter the number you want to go to: ")
    if number == "0":
        print("Please enter a bigger number!")
    try:
        int(number)
        number = int(number)
        if number<0:
            print("Please enter a positive number!")
            sys.exit(0)
    except ValueError:
        print("Please enter a valid input (positive integer)!")
        sys.exit(0)
    for x in range(1,number+1):
        ans = x*x*x
        numbers.append(ans)
    print(*numbers,sep=", ")

def square():
    number = input("Enter the number you want to go to: ")
    if number == "0":
        print("Please enter a bigger number!")
    try:
        int(number)
        number = int(number)
        if number<0:
            print("Please enter a positive number!")
            sys.exit(0)
    except ValueError:
        print("Please enter a valid input (positive integer)!")
        sys.exit(0)
    for x in range(1,number+1):
        ans = x*x
        numbers.append(ans)
    print(*numbers,sep=", ")

choice = input("Do you want the numbers squared or cubed? ")
if choice.upper() == "CUBED":
    cube()
elif choice.upper() == "SQUARED":
    square()
else:
    print("Sorry, I don't understand.")
    sys.exit(0)
