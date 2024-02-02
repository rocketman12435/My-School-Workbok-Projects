import sys
import time

#price of items
cake = 2
soup = 2.5
tea = 1.5
coffee = 2
salad = 3
num = 0
total = 0
pensioner = 0
pension = input("Are you a pensioner? ")
if pension.upper() == "NO":
     print("You will get no discount as per the government rules for pensioners")
elif pension.upper() == "YES":
     print("You will get a 10"+'%',"discount")
else:
     print("Sorry, I don't understand.")#take input and run again
     sys.exit(0)
#Python list of options
choices = ["1.Cake - £2 per slice"," 2.Soup - £2.50 per bowl"," 3.Tea - £1.50 per cup"," 4.Coffee - £2 per cup"," 5.Salad - £3 per plate"]
repeat = True
#while loop for asking choice until the user proceeds to checkout
while repeat == True:
    print("num at the start is", num)
    if num == 5:
        print("You've had all your five choices. Proceeding to checkout...")
        repeat = False
        vat=total*0.2 #only for take away 
        total = total+vat
        print("The total is",round(total,2),"pounds") #generate bill 
        money = input("Card or Cash? ")
        if money.upper() == "CARD":
                    print("Card Transaction")
                    time.sleep(2)
                    print()
                    print("Checking Transaction...")
                    time.sleep(1.5)
                    print()
                    print("Authorised")
                    print()
                    print("Thank you for coming. See you again!")
        elif money.upper() == "CASH":
                    print("Paying with cash")
                    time.sleep(4)
                    print("Thank you for coming. See you again!")
    print("The choices are:")
    print(*choices,sep=",")
    choice = input("What do you want today? ")
    if choice.upper() == "CAKE":
            print("Cake\n")
            numitems = input("How many cakes do you want?\n ")
            try:
                int(numitems)
                numitems = int(numitems)
                if numitems == 0:
                      print("You need to have at least one item if you are buying something.") 
                      sys.exit(0)
                cake = cake*numitems
                total = total+cake
            except ValueError:
                  print("Sorry, I don't understand.")
                  sys.exit(0)
            checkout = input("Proceed to checkout? ")
            if checkout.upper() == "NO":
                repeat == True
            elif checkout.upper() == "YES":
                repeat = False
                vat=total*0.2
                total = total+vat
                print("The total is",round(total,2),"pounds")
                money = input("Card or Cash? ")
                if money.upper() == "CARD":
                    print("Card Transaction\n")
                    time.sleep(1)

                    print("Checking Transaction...")
                    time.sleep(1.5)
                    print()
                    print("Authorised")
                    print()
                    print("Thank you for coming. See you again!")
                elif money.upper() == "CASH":
                    print("Paying with cash")
                    time.sleep(4)
                    print("Thank you for coming. See you again!")

    elif choice.upper() == "SOUP":
            print("Soup")
            print()
            numitems = int(input("How many soup bowls do you want? "))
            try:
                int(numitems)
                numitems = int(numitems)
                if numitems == 0:
                      print("You need to have at least item if you are buying something.")
                      sys.exit(0)
                soup = soup*numitems
                total = total+soup
            except ValueError:
                  print("Sorry, I don't understand.")
                  sys.exit(0)
            
            print()
            checkout = input("Proceed to checkout? ")
            if checkout.upper() == "NO":
                repeat == True
            elif checkout.upper() == "YES":
                repeat = False
                vat=total*0.2
                total = total+vat
                print("The total is",round(total,2),"pounds")
                money = input("Card or Cash? ")
                if money.upper() == "CARD":
                    print("Card Transaction")
                    time.sleep(2)
                    print()
                    print("Checking Transaction...")
                    time.sleep(1.5)
                    print()
                    print("Authorised")
                    print()
                    print("Thank you for coming. See you again!")
                elif money.upper() == "CASH":
                    print("Paying with cash")
                    time.sleep(4)
                    print("Thank you for coming. See you again!")
    elif choice.upper() == "TEA":
            print("Tea")
            print()
            numitems = int(input("How many soup bowls do you want? "))
            try:
                int(numitems)
                numitems = int(numitems)
                if numitems == 0:
                      print("You need to have at least item if you are buying something.")
                      sys.exit(0)
                soup = soup*numitems
                total = total+soup
            except ValueError:
                  print("Sorry, I don't understand.")
                  sys.exit(0)
            
            print()
            checkout = input("Proceed to checkout? ")
            if checkout.upper() == "NO":
                repeat == True
            elif checkout.upper() == "YES":
                repeat = False
                vat=total*0.2
                total = total+vat
                print("The total is",round(total,2),"pounds")
                money = input("Card or Cash? ")
                if money.upper() == "CARD":
                    print("Card Transaction")
                    time.sleep(2)
                    print()
                    print("Checking Transaction...")
                    time.sleep(1.5)
                    print()
                    print("Authorised")
                    print()
                    print("Thank you for coming. See you again!")
                elif money.upper() == "CASH":
                    print("Paying with cash")
                    time.sleep(4)
                    print("Thank you for coming. See you again!")
    elif choice.upper() == "COFFEE":
            print("Coffee")
            print()
            numitems = int(input("How many coffee cups do you want? "))
            try:
                int(numitems)
                numitems = int(numitems)
                if numitems == 0:
                      print("You need to have at least item if you are buying something.")
                      sys.exit(0)
                coffee = coffee*numitems
                total = total+coffee
            except ValueError:
                  print("Sorry, I don't understand.")
                  sys.exit(0)
            print()
            checkout = input("Proceed to checkout? ")
            if checkout.upper() == "NO":
                repeat == True
            elif checkout.upper() == "YES":
                repeat = False
                vat=total*0.2
                total = total+vat
                print("The total is",round(total,2),"pounds")
                money = input("Card or Cash? ")
                if money.upper() == "CARD":
                    print("Card Transaction")
                    time.sleep(2)
                    print()
                    print("Checking Transaction...")
                    time.sleep(1.5)
                    print()
                    print("Authorised")
                    print()
                    print("Thank you for coming. See you again!")
                elif money.upper() == "CASH":
                    print("Paying with cash")
                    time.sleep(4)
                    print("Thank you for coming. See you again!")
    elif choice.upper() == "SALAD":
            print("Salad")
            print()
            numitems = int(input("How many plates of salad do you want? "))
            try:
                int(numitems)
                numitems = int(numitems)
                if numitems == 0:
                      print("You need to have at least item if you are buying something.")
                      sys.exit(0)
                salad = salad*numitems
                total = total+salad
            except ValueError:
                  print("Sorry, I don't understand.")
                  sys.exit(0)
            print()
            checkout = input("Proceed to checkout? ")
            if checkout.upper() == "NO":
                repeat == True
            elif checkout.upper() == "YES":
                repeat = False
                vat=total*0.2
                total = total+vat
                print("The total is",round(total,2),"pounds")
                money = input("Card or Cash? ")
                if money.upper() == "CARD":
                    print("Card Transaction")
                    time.sleep(2)
                    print()
                    print("Checking Transaction...")
                    time.sleep(1.5)
                    print()
                    print("Authorised")
                    print()
                    print("Thank you for coming. See you again!")
                elif money.upper() == "CASH":
                    print("Paying with cash")
                    time.sleep(4)
                    print("Thank you for coming. See you again!")
    else:
         print("Please enter the right option")
         sys.exit(0)
    
    print("num before increment is num",num)
    num=num+1
    print("num after increment is",num)