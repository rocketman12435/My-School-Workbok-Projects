import sys
childNames = []
repeat = True
average = 0
n=0
file = open("StudentAverage.txt","w")
file.write("NAME        TEST 1       TEST 2         TEST 3       AVERAGE        PERCENTAGE\n")
while repeat == True:
    print("You can enter up to 10 students' names\n")
    numChildren = int(input("How many children are in your class? "))
    if numChildren>10:
        repeat = True
        print("You can only have maximium 10 inputs. Please try again")
    else:
        repeat = False
for x in range(numChildren):
    if x==10:
        print("Going to results enterer...\n")
        repeat = False
    childName = input("Please enter a student's name: \n")
    childNames.append(childName)

for y in range(len(childNames)):
    file.write(childNames[y])
    for z in range (1,4):
        print("Please enter",childNames[y]+"'s","result for test",z)
        print()
        testScore = float(input("The test score is out of 30: "))
        average = average+testScore
        file.write("             "+str(testScore))
    average=average//3
    file.write("        "+str(average))
    percent = average/30
    percent = percent*100
    file.write("         "+str(percent))


    file.write("\n")
    average = 0
    percent = 0
file.close()
file = open("StudentAverage.txt","r")
print(file.read())
