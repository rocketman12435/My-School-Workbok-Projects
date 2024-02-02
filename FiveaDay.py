import time
import sys
numbers = []
minusplus = 0
number = input("Enter a number: ")



try:
        int(number)
        number = int(number)
        if number<0:
            minusplus = -1
        elif number > 0:
            minusplus = 1
except ValueError:
        print("Please enter an integer!")
        sys.exit(0)

for x in range(1,number+1,minusplus):
    if x%5 ==0 and x!=0:
        #print(x,"is divisible by 5")
        numbers.append(x)
if len(numbers) == 0:
    print("Your number is too small!")
    sys.exit(0)
print("The numbers divisible by 5, up till",number,"inclusive are: \n")
print(*numbers,sep = ",")
