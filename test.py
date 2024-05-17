import sys
found = False
n=1

file = open("names.txt", "a")
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
                print(search)
                while "--" not in line:
                    line = file.readline()
                    if line.find("--") == -1:
                        print(line)

                
            elif "eof" in line:
               break
classSelect()