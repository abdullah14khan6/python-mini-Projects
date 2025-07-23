import random
import os
from wordsets import wordSets


def fre(word): # returns frequency of each letter
    wordCounter = ""
    wordCount = {} # dictionary to store the frequency of each unique letter 
        
    for char in word:
        indexList = [] # to store indices of each letter
        counter = 0
        if char in wordCounter: # to ensure each letter is only checked once
            continue
        wordCounter += char
        for j in range(0,len(word)):
            if char == word[j]:
                counter +=1
                indexList.append(j)
                
        wordCount.update({char:[counter,indexList]})
        
    return(wordCount)


def main():
    category = random.choice(list(wordSets.keys())) # selects a random category
    word = random.choice(wordSets[category]) # selects a random word from that category
    size = len(word)
    chances = size+3
    guessed = ["_" for i in range(0,size)] # list for storing guesses
    wordFre = fre(word)
    
    print(wordFre)
    print(f"GUESS THE WORD\n\nHINT: The word is a {str(category).upper()}")
    print(f"You have {chances} chances to guess the correct letters. We will show one letter")
    print(word) # for testing
    
    hintIndex = random.randint(0,size-1) # give the first letter as hint
    hint = word[hintIndex]
    guessed.insert(hintIndex,hint) # inserts that letter at that index
    wordFre[hint][0] -= 1
    
    print(wordFre)
    
    # if(wordFre[hint] == 0):
    #     del wordFre[hint]
    
    for i in guessed: # prints the guessed leters
        print(i,end=" ")
    print("\n") # to add a newline character
    
    while True:
        char = input("Enter a letter: ")
        
        if not char.isalpha():
            print("Only enter a letter")
            continue

        if len(char) > 1:
            print("Only enter one letter")
            continue
        
        if char not in word:
            print("letter is not in word")
            continue
            
        if char in guessed:
            if wordFre[char][0] <= guessed.count(char):
                print("letter already present")
                continue
        
        
        
        # for i in range(0, size):
        #     if char == word[i]:
        #         index = wordFre[char][1]
        
        
        # for i in range(0,size):
        #     temp = guessed[i]
        #     for j in range(0,size):
        #         if temp == word[i]:
                    
        #             print(char, end= " ")
        #         else:
        #             print("_", end= " ")
        print("\n")
            
    
    

    
    
if(__name__ == "__main__"):
    main()