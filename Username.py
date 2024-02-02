import sys
repeat = True
while repeat == True:
    fname = input("Please enter your first name: ")
    if fname == "":
         repeat = True
         print("Nothing entered. Please try again")
    elif fname.isdigit() == True:
        repeat = True
        print("Please enter a valid input. Try again")
    else:
            repeat = False
            print("Hi",fname)
            sname = input("Please enter your surname: ")
            if sname == "":
                repeat = True
                print("Nothing entered. Please try again")
            elif sname.isdigit() == True:
                repeat = True
                print("Please enter a valid input. Try again")
            else:
                print("Your username is:",sname+"."+fname)