repeat = True
file = open("names.txt", "a")
while repeat:
    newBoy = input("Please enter a new boy's name: ")
    file.write(newBoy)
    print("Added")
    again = input("Do you want to add another name? (y/n): ")
    if again.upper() == "N":
        file.close()
        break
    elif again.upper() == "Y":
        file.write("\n")
file = open("names.txt","r")
print(file.read())
file = open("names.txt","a")
file.write("\n")
file.close()
        