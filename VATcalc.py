import sys

price = input("Enter the item's price: ")

if price == "":

    print("No price entered!")

    sys.exit(0)

currency = input("Enter the currency: ") 

if currency == "":

    print("No currency entered!")

    sys.exit(0)



vat = 0.2





price = float(price)

total = price+(price*vat)

vatamount = price*vat

print("The total price is",total,currency,"including" ,vatamount,currency ,"of VAT")
