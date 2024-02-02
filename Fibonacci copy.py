#This program is designed to print out the Fibonacci series till a term the user has entered.
#It takes the input, then processes the data, and lastly outputs the result.
import sys
#Declaring variables
fibList = [0,1]
repeat = True
#Repeats the program till the user wants to exit
while repeat==True:
    firstStep = 0 #first term of the Fibonacci series
    secondStep = 1 #second term of the Fibonacci series
    num = input("Please enter the term you want to print the Fibonacci series to: ")
    #checks if the user has entered erroneous data and tells them to try again if this is the case
    try:
        int(num)
        num=int(num)
        if int(num) <= 0:
            print("The number has to be greater than 0!")
    except ValueError:
        print("Invalid input: please enter a suitable value (positive integer)")
        repeat = True
    #Keeps calculting numbers till the loop reaches the term
    for x in range(2,num):
        firstStep,secondStep = secondStep,firstStep+secondStep
        fibList.append(secondStep)
    print("Calculating...")
    print("The Fibonacci sequence till term",num,"is:\n")
    print(*fibList,sep=",")
    again = input("Want to go again? Please enter either 'yes' or 'no' ")
    if again.upper() == "YES":
        repeat = True
    elif again.upper() == "NO":
        repeat = False
        print("Thank you!")
        sys.exit(0)
    else:
        print("Invalid input: please enter either 'yes' or 'no'")
        repeat = True