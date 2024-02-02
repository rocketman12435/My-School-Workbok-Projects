import sys
repeat = True
while repeat == True:
    strinput = input("Please enter a string to be reversed: ")
    if strinput.isdigit() == True:
        repeat = True
        print("Invalid input. Please try again")
    else:
        repeat = False
    print("Reversed string:",strinput[::-1])