import sys
nums = []
for x in range(5):
    floatinput = input("Please enter a number: ")
    try:
        float(floatinput)
        intinput = float(floatinput)
        nums.append(floatinput)
    except:
        print("Please enter a number")
        sys.exit(0)
print("Original input: \n")
print(*nums,sep=",")
nums.reverse()
print("\nReversed input: \n")
print(*nums,sep=",")