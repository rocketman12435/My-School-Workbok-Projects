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
vat = 0
dis = 0
addVAT = False
pensionerval = False
bill = []
repeat = True

def isUserPensioner():
     r = True
     pensionerval = True
     while r == True:
        pension = input("Are you a pensioner? Please enter 'y' for 'yes' or 'n' for 'no'")
        if pension.upper() == "N":
            print("You will get no discount as per the government rules for pensioners")
            r=False
            pensionerval = False
            return pensionerval
        elif pension.upper() == "Y":
            print("You will get a 10"+'%',"discount")
            r=False
            return pensionerval
        else:
            print("Sorry, I don't understand.Please enter 'y' for 'yes' or 'n' for 'no'")

def takeOut():
     r = True
     a = True
     while r == True:
        t = input("Will you dine here, or will you take-out? Please enter '1' for 'dine here' or '2' for 'take-out' ")
        if t == "1":
            print("No VAT applied")
            r=False
            a=False
            return a
        elif t == "2":
            print("20"+'%',"VAT applied")
            r=False
            return a
        else:
            print("Sorry, I don't understand.Please enter '1' for 'dine here' or '2' for 'take-out'")  

def generateBill():
        global total
        global vat
        global dis
        global addVAT
        global pensionerval
        p = True
        print("The total is",total)          
        print("The addVAT is",addVAT)
        print("The pensionerval is",pensionerval)
        if addVAT == True:
            vat=total*0.2
        print("The vat is",vat)  
        print("The total before VAT addition is",total)  
        total = total+vat
        print("The total after VAT addition is",total)  
        if pensionerval == True:
            dis=total*0.1                  
        print("The discount is",dis)  
        print("The total before considering discount is",total)  
        total = total- dis
        print("The total after considering discountis",total)          
        print("The grand total is",round(total,2),"pounds") #generate bill
        print("Your bill is: \n ---------------------------------------------------------------")        
        bill.append("\n")
        
        #bill.append(total) 
        print(*bill,sep="\t") 
        print(" ---------------------------------------------------------------")        
        print("Your total amount is: ",total,"pounds")        
        print("---------------------------------------------------------------")        
        while p == True:        
            money = input("Card or Cash? ")
            if money.upper() == "CARD":
                        p=False
                        print("Card Transaction")
                        time.sleep(2)
                        print()
                        print("Checking Transaction...")
                        time.sleep(1.5)
                        print()
                        print("Authorised")
                        print()
                        print("Thank you for coming. See you again!")
                        sys.exit(0)   
            elif money.upper() == "CASH":
                        p=False

                        print("Paying with cash")
                        time.sleep(4)
                        print("Thank you for coming. See you again!")
                        sys.exit(0)    
            else:
                print("Sorry, I don't understand.Please enter 'card' or  'cash'")  
        
def askUserForCheckout():
    b=True
    global repeat
    while b == True: 
        checkout = input("Proceed to checkout? Please enter 'yes' or 'no' ")
        if checkout.upper() == "NO":
            repeat == True
            b=False
            print(total)
        elif checkout.upper() == "YES":
            repeat = False
            b=False
            generateBill()
        else:
            print("Sorry, I don't understand.Please enter 'yes' or 'no'")   

pensionerval = isUserPensioner()
addVAT= takeOut()
#print("The addVAT is",addVAT)
#print("The pensionerval is",pensionerval)                                  
print("You will only be able to take 5 different items. Please enter the item's name, price and quantity from the the list below.")
#Python list of options
choices = ["1.Cake - £2 per slice"," 2.Soup - £2.50 per bowl"," 3.Tea - £1.50 per cup"," 4.Coffee - £2 per cup"," 5.Salad - £3 per plate"]

bill.append(" ")
bill.append("Item name")
bill.append("   ")
bill.append("Number of items ")
bill.append("Item price")
bill.append("\n")

#while loop for asking choice until the user proceeds to checkout
while repeat == True:
    #print("num at the start is", num)
    if num == 5:
        print("You've had all your five choices. Proceeding to checkout...")
        repeat = False
        generateBill()
    print("The choices are:")
    print(*choices,sep=",")
    choice = input("What do you want today? ")
    if choice.upper() == "CAKE":
            print("Cake\n")
            price = input("Enter the price \n ")
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

            bill.append(choice)
            bill.append("\t")
            bill.append(numitems)
            bill.append("\t")
            bill.append(price)
            bill.append("\n")

            askUserForCheckout()  

    elif choice.upper() == "SOUP":
            print("Soup")
            price = input("Enter the price \n ")
  
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
            bill.append(choice)
            bill.append("\t")
            bill.append(numitems)
            bill.append("\t")
            bill.append(price)
            bill.append("\n")            

            print()
            askUserForCheckout()
    elif choice.upper() == "TEA":
            print("Tea")
            price = input("Enter the price \n ")

            numitems = int(input("How many cups of tea do you want? "))
            try:
                int(numitems)
                numitems = int(numitems)
                if numitems == 0:
                      print("You need to have at least item if you are buying something.")
                      sys.exit(0)
                tea = tea*numitems
                total = total+tea
            except ValueError:
                  print("Sorry, I don't understand.")
                  sys.exit(0)
            bill.append(choice)
            bill.append("\t")
            bill.append(numitems)
            bill.append("\t")
            bill.append(price)
            bill.append("\n")            
   
            print()
            askUserForCheckout()
    elif choice.upper() == "COFFEE":
            print("Coffee")
            price = input("Enter the price \n ")

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
            bill.append(choice)
            bill.append("\t")
            bill.append(numitems)
            bill.append("\t")
            bill.append(price)
            bill.append("\n")            
   
            askUserForCheckout()
    elif choice.upper() == "SALAD":
            print("Salad")
            price = input("Enter the price \n ")

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
            bill.append(choice)
            bill.append("\t")
            bill.append(numitems)
            bill.append("\t")
            bill.append(price)
            bill.append("\n")            
     
            askUserForCheckout()
    else:
         print("Please enter the right option")
         sys.exit(0)
    
    #print("num before increment is num",num)
    num=num+1
    #print("num after increment is",num)
