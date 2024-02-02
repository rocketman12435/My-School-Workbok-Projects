h = float(input("Enter the height: "))

w = float(input("Enter the width: "))

l = float(input("Enter the length: "))

unit = input("Enter the unit for all 3 lengths: ")

def surfacearea():

    calc1 = 2*(h*w)

    calc2 = 2*(h*l)

    calc3 = 2*(w*l)

    total = calc1+calc2+calc3

    print("The surface area is",total,unit+"^2")

def volume():

    total = h*w*l

    print("The volume is",total,unit+"^3")

choice = input("Press 1 to calculate surface area and 2 to calculate volume")

if choice == "1":

    surfacearea()

if choice == "2":

    volume()
