import sys
from array import *
details = [["","","","","","","","","",""],["","","","","","","","","",""],["","","","","","","","","",""],
           ["","","","","","","","","",""],["","","","","","","","","",""]]
repeat = True
average = 0
print(details[0][0])
while repeat == True:
    print("You can enter up to 10 students' names\n")
    numChildren = int(input("How many students are in your class? "))
    if numChildren>10:
        repeat = True
        print("You can only have maximium 10 inputs. Please try again")
    else:
        repeat = False
for x in range(numChildren):
    print(x,"is x")
    childName = input("Please enter a student's name: \n")
    details[0][x] = childName
    if x==10:
        print("Going to results enterer...\n")
        repeat = False

for y in range(numChildren):
    for z in range (1,4):
        print("Please enter",details[0][x]+"'s","result for test",z)
        print()
        testScore = float(input("The test score is out of 30: "))
        testScore = testScore+"        "
        testScore = details[z][y]
for a in range(1,numChildren+1):
    avg =  (details[1][x]+details[2][x]+details[2][x])//3
print(details)