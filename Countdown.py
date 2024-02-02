import time
import sys
numbers = []

number = input("Enter a number: ")



try:
        float(number)
        number = float(number)
        fornum = round(number)
        number = int(number)
        if number<0:
            print("The number must be positive to count down!")
            sys.exit(0)

        elif number == 0:
            print("Please enter a bigger number!")
            sys.exit(0)
except ValueError:
        print("Please enter a number!")
        sys.exit(0)

for x in range(number,-1,-1):
        numbers.append(x)

print(*numbers,sep = ",")
