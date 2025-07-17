import random
import os
from wordsets import wordSets


def fre(word): # returns frequency of each letter
    wordCounter = ""
    wordCount = {} # dictionary to store the frequency of each unique letter

    for i in range(0,len(word)):
        char = word[i]
        counter = 0
        if char in wordCounter: # to ensure each letter is only checked once
            continue
        wordCounter += char
        for j in range(0,len(word)):
            if char == word[j]:
                counter +=1
                
        wordCount.update({char:[counter,]})  
        
    return(wordCount)


def main():
    category = random.choice(list(wordSets.keys()))
    word = random.choice(wordSets[category])
    size = len(word)
    chances = size+3
    guessed = ""
    wordFre = fre(word)
    
    print(wordFre)
    print(f"GUESS THE WORD\n\n HINT: The word is a {str(category).upper()}")
    print(f"You have {chances} chances to guess the correct letters. We will show one letter")
    print(word) # for testing
    
    hintIndex = random.randint(0,size)
    hint = word[hintIndex]
    guessed += hint
    wordFre[hint][0] -= 1
    wordFre[hint].append([hintIndex,])
    
    print(wordFre)
    
    # if(wordFre[hint] == 0):
    #     del wordFre[hint]
    
    for i in range(0, size):
        if i == hintIndex:
            print(hint, end= " ")
        else:
            print("_", end= " ")
    print("\n") # to add a newline character
    
    while True:
        guessedFre = fre(guessed)
        char = input("Enter a letter: ")
        
        if not char.isalpha:
            print("Enter an letter")
            continue

        if len(char) > 1:
            print("Only enter one letter")
        
        if char not in word:
            print("letter is not in word")
            
        if char in guessed:
            if wordFre[char] <= guessedFre[char]:
                print("letter already present")
                continue
        
        guessed += char
        
        for i in range(0,size):
            if char == word[i]:
                print(char, end= " ")
            else:
                print("_", end= " ")
        print("\n")
            
    
    

    
    
if(__name__ == "__main__"):
    main()