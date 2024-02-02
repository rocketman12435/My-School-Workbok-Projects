import sys
numbers = []
for x in range(3):
    numinput = input("Enter a postive integer: ")

    if numinput.isdigit() == False:
            print("Invalid input.")
            print()
            print("Exiting...")
            sys.exit(0)
    elif numinput.isdigit() == True:
        numinput = int(numinput)
    numbers.append(numinput)

numbers.sort()

print(numbers[2],"is the biggest number.")

#with the code above, we can use the built-in function 'sort()' to find the biggest number
#but I have also implemented the logic to find the biggest number without using the built-in function 'sort()'
#biggest=numbers[0]
#for x in range (0,len(numbers)-1):
#    if biggest<numbers[x+1]:
#        biggest = numbers[x+1]
#print(biggest,"is the biggest number")
