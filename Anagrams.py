original = []
anagram = []
import sys
word = input("Please enter a word: ")
for x in range(len(word)):
    original.append(word[x])
original.sort()
anaword = input("Please enter another word: ")
if len(anaword) == len(word):
    for x in range(len(anaword)):
        anagram.append(anaword[x])
    anagram.sort()
    if anagram == original:
        print(anaword,"is an anagram of",word)
    else:
        print(anaword,"is not an anagram of",word)
        
else:
    print(anaword,"is not an anagram of",word)
