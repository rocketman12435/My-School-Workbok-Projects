#This program makes codewords by adding certain strings.
import sys
#defining variables
wordlist = []
repeat = True
#While loop to repeat round and round until the user enters a valid input
while repeat == True:
    #User input
    word = input("Please enter a word: ")
    
    try:
        word = word.strip()
        #Is it a word containing letters?
        if word.isalpha() == False:
            print("Please enter a valid input\n")
            repeat = True
        else:
            repeat=False
        if repeat == False:
            #Split the word into its letters
            for x in range(len(word)):
                wordlist.append(word[x])
            #Even number of characters

            if len(word)%2 == 0:
                #Mid-point of the word
                y=int(len(word)/2)
                #Add the codes
                wordlist.insert(y,"egg")
                a = "".join(str(element) for element in wordlist)
                #Take out natural python list spaces
                a.replace(" ","")
                print("The code is:",a)

            #Odd number of characters
            elif len(word)%2 != 0:
                #1 before the mid-point
                y=int((len(word)/2))
                #Insert codes
                wordlist.insert(y,"ga")
                #1 after the mid-point
                b=int((len(word)/2)+2)
                #Insert codes
                wordlist.insert(b,"ga")
                a = "".join(str(element) for element in wordlist)
                #Take out natural python list spaces
                a.replace(" ","")
                print("The code is:",a)

    except ValueError:
        print("Please enter a valid input\n")
        repeat = True





