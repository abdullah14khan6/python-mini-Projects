import random
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
    while True:
        category = random.choice(list(wordSets.keys())) # selects a random category
        word = random.choice(wordSets[category]) # selects a random word from that category
        size = len(word)
        chances = size+3
        guessed = ["_" for i in range(0,size)] # list for storing guesses
        wordFre = fre(word)
        
        # print(wordFre) # for testing
        # print(word) # for testing
        
        hintIndex = random.randint(0,size-1) # give the first letter as hint
        hint = word[hintIndex]
        guessed[hintIndex] = hint # inserts that letter at that index
        wordFre[hint][0] -= 1
        del wordFre[hint][1][0] # deletes the first occurance index
        
        # print(wordFre) # for testing
        
        
        while True:
            flag = True # flag to check if all the words are guessed
            if chances == 0:
                print("OUT OF LIVES, BEST OF LUCK NEXT TIME")
                break
            
            print(f"GUESS THE WORD\nHINT: The word is a {str(category).upper()}")
            print(f"You have {chances} chances to guess the correct letters\n")
            for i in guessed: # prints the guessed leters
                if i == "_":
                    flag = False
                print(i,end=" ")
            print("\n")
            
            char = input("Enter a letter: ")
            
            chances -= 1
            if not char.isalpha(): # skip if not alphabet
                print("\nOnly enter a letter\n")
                continue

            if len(char) > 1: # skip if more than 1 letter
                print("\nOnly enter one letter\n")
                continue
            
            if char not in word: # skip if not in word
                print("\nletter is not in word\n")
                continue
                
            if char in guessed:
                if wordFre[char][0] < guessed.count(char): # skip if already guessed all occurances
                    print("\nletter already present\n")
                    continue
            
            wordFre[char][0] -= 1
            indexList = wordFre[char][1]
            guessed[indexList[0]] = char
            del wordFre[char][1][0]
            
            for i in guessed: # prints the guessed leters
                if i == "_":
                    flag = False
                print(i,end=" ")
            print() # to add a newline character
            
            if flag == True:
                print("CONGRATULATIONS YOU HAVE GUESSED ALL THE LETTERS CORRECTLY!")
                break # leaves the loop
        
    
        print("\nDo you wish to play again?")
        buffer = input("Enter yes or no: ")
        if "yes" not in buffer:
            break
            
    
    

    
    
if(__name__ == "__main__"):
    main()