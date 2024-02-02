a=0
e=0
i=0
o=0
u=0
import sys
txt = input("Please enter a string: ")
for x in range(len(txt)):
    if txt[x].lower() == "a":
        a+=1
    elif txt[x].lower() == "e": 
        e+=1
    elif txt[x].lower() == "i":
        i+=1
    elif txt[x].lower() == "o":
        o+=1
    elif txt[x].lower() == "u":
        u+=1
    

print("A:",a)
print("E:",e)
print("I:",i)
print("O:",o)
print("U:",u)
