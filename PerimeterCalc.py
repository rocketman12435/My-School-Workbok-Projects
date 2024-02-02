import sys

import time

repeat = True

unit = ""

def perimeter():

    while repeat == True:

        length = float(input("Enter the length: "))
        if length == 0:
            print("This can't be 0!")
            sys.exit(0)

        width = float(input("Enter the width: "))
        if width == 0 :
            print("This can't be 0!")
            sys.exit(0)



        if width < 0 or length < 0:

            print("Invalid input: Negative number entered")

            sys.exit(0)
        if width == 0 or length == 0:
            print("This can't be 0!")
            sys.exit(0)

        perimeter = (length*2) + (width*2)

        print(perimeter,"is the perimeter.")

        repeatq = input("Want to repeat? Enter y for yes and n for no: ")

        if repeatq.upper() == "Y":

            repeat == True

        if repeatq.upper() == "N":

            repeat == False

            print("Exiting...")

            time.sleep(1.5)

            sys.exit(0)
        else:
            print("Sorry, I didn't understand")
            print("Exiting...")
            time.sleep(1.5)
            sys.exit(0)

perimeter()
