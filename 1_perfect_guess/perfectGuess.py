from random import randint , seed
import os
def intGuess():
    guess= int(input('Enter a guess: '))
    return guess

def game(rand, guess, tries):
        while True:

            if guess<rand:
                print("Try a higher number")
                guess = intGuess()
                tries+=1
            elif guess>rand:
                print("Enter a lower number")
                guess = intGuess()
                tries+=1
            else:
                print('Perfect Guess')
                print(f'You guessed the number in {tries} tries\n')
                break
seed(23)
while True:
    print('Welcome to THE PERFECT GUESS\n')
    rand = randint(1, 100)
    guess = intGuess()
    tries = 1
    
    game(rand, guess, tries)
    
    print('Do you want to play the game again?')
    ans = input('Enter yes to continue no to exit: ')
    os.system('cls')
    if ans.lower() == 'no':
        break
        
    