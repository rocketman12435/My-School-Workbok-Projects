import sys
found = False
n=1
repeat = True
repeat2 = True
file = open("names.txt", "a")
file.truncate(0)
   
def classSelect():
    classInput = input("Which class do you want to select? ")
    search = "Class"+" "+classInput
    with open("names.txt","r") as file:
    
        while True:
            line = file.readline()
            #print(search)
            #print(line)
            if line.find(search) != -1:
                #print("found")
                print()
                print("This is",search)
                while "--" not in line:
                    line = file.readline()
                    if line.find("--") == -1:
                        print(line)

                
            elif "eof" in line:
               break  


while repeat2:
    classno = "Class"+" "+str(n)
    print()
    print("Class",n,"added")
    print()
    file.write(classno)
    file.write("\n")
    while repeat:
        newBoy = input("Please enter a new boy's name: ")
        file.write(newBoy)
        print("Added")
        again = input("Do you want to add another name? (y/n): ")
        if again.upper() == "N":
            newClass = input("Do you want to add a new class? (y/n): ")
            if newClass.upper() == "N":
                file.write("\n")
                file.write("--")
                file.write("\neof")
                file.close()
                classSelect()
                sys.exit(0)
              
                            
            elif newClass.upper() == "Y":
                file.write("\n")
                file.write("--")
                file.write("\n")
                n+=1
                break
        elif again.upper() == "Y":
            file.write("\n")


        