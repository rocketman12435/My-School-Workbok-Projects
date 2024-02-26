import sys
import string
repeat = True
while repeat == True:
    palinput = input("Enter a string to check if it is a palindrome: ")
    palinput = palinput.translate(str.maketrans('', '', string.whitespace))
    palinput = palinput.translate(str.maketrans('', '', string.punctuation))
    palinput = palinput.lower()
    def isfloat(palinput):
        try:
            float(palinput)
            print("Please enter a string with no decimal places or numbers")
            repeat = True
        except ValueError:
            repeat = False
    try:
        isfloat()
        num = palinput.isnumeric()
        if num == True:
            repeat = True
            print("Please enter a string with no numbers")
            
    except:
        repeat = False
        if palinput == palinput[::-1]:
            print("Your word is a palindrome!")
        else:
            print("Your word is not a palindrome.")
        