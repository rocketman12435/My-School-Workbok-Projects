import sys
code = []
txt= input("Please enter a string: ").lower()
for x in txt:
    codenum = ord(x)-96
    code.append(codenum)
    print()
print("The code is:",*code)
