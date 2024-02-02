import time
import sys

number = input("Enter a number: ")



try:
        int(number)
        number = int(number)

        if number<0:
            print("The number must be positive!")
            sys.exit(0)

        elif number == 0:
            print("Please enter a bigger number!")
            sys.exit(0)
except ValueError:
        print("Please enter an integer!")
        sys.exit(0)

for x in range(1,13):
    ans = number*x
    print(number,"x",x,"=",ans)
