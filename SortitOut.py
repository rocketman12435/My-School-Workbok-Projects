import sys
alphabetical= []
repeat = True
while repeat == True:
    for x in range(5):
        wordInput = input("Please enter a word: ")
        if wordInput.isdigit() == True:
            print("The input has to be a a word!")
            repeat = True
        else:
            alphabetical.append(wordInput)
            repeat = False

alphabetical.sort()
print(*alphabetical,sep = ",")