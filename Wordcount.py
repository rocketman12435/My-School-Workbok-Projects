import sys
passage = input("Please enter a passage: ")
if passage.isdigit() == True:
    print("Invalid input. Restart the program")
    sys.exit(0)
print("This contains",passage.count(" ")+1,"words.")
