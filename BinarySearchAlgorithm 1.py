import sys
values = ["kettle","minimize", "funny", "publisher", "relinquish", "slide", "profile", "will", "administration", "publish", "house", "senior"]
values.sort()
print(values)
searchfor = input("Enter a word to search for: ")
l=0
h=len(values)-1
mid = (l+h)//2
while l<=h:
    mid = (l+h)//2
    if searchfor.lower() == values[mid]:
        print(values[mid], "found at position", mid+1)
        break
    elif l==h and values[mid]!=searchfor.lower():
        print("Word not found")
        break
    elif searchfor.lower()<values[mid]:
        #print("elif",values[mid])
        h=mid-1
    else:
        #print("else",values[mid])
        l=mid+1
