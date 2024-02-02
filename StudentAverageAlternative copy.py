import sys
from array import *
details = [["","","","","","","","","",""],[],[],[],[]]
repeat = True
average = 0
print(details[0][0])
while repeat == True:
    print("You can enter up to 10 students' names\n")
    numChildren = int(input("How many students are in your class? "))
for x in range(numChildren):
    childName = input("Please enter a student's name: ")
    childName = details[0]