import sys

repeat = True
while repeat == True:
    palinput = input("Enter a string to check if it is a palindrome: ")
    def isfloat(palinput):
        try:
            float(palinput)
            return "Please enter a string with no decimal places or numbers"
            repeat = True
        except ValueError:
            repeat = False
    print(isfloat(palinput))
    try:
        isfloat()
        num = palinput.isnumeric()
        if num == True:
            repeat = True
            print("Please enter a string with no numbers")
            
    except:
        repeat = False
        if palinput == palinput[::-1]:
            print(palinput,"is a palindrome!")
        else:
            print(palinput, "is not a palindrome.")
        