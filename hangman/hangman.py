import sys
import random as r
from os import path
from termcolor import colored, cprint

# Draw Hangman

hangman = ["""
    _____________
    |           |
    |           |
    |           |
    |
    |
    |
    |
    |
---------
""",
"""
    _____________
    |           |
    |           |
    |           |
    |         (. .) 
    |           
    |          
    |          
    |
---------
""",
"""
    _____________
    |           |
    |           |
    |           |
    |         (. .) 
    |           |
    |          
    |          
    |
---------
""",
"""
    _____________
    |           |
    |           |
    |           |
    |         (. .) 
    |           |
    |          /|
    |          
    |
---------
""",
"""
    _____________
    |           |
    |           |
    |           |
    |         (. .) 
    |           |
    |          /|\\
    |          
    |
---------
""",
"""
    _____________
    |           |
    |           |
    |           |
    |         (. .) 
    |           |
    |          /|\\
    |          / 
    |
---------
""",
"""
    _____________
    |           |
    |           |
    |           |
    |          (!) 
    |           |
    |          /|\\
    |          / \\
    |
---------
"""]

def showMenu():
    cprint("Select mode", 'green')
    cprint("1. One Player", 'green')
    cprint("2. Two Player", 'green')

# if player 2 wins then print this
player2won = """
***********************
*    PLAYER-2 WON     *
***********************
"""

youWon = """
***************************
*    HURRAY!! YOU WON     *
***************************
"""
def onePlayerMode():

    # File path must be correct (list of words)
    filePath = 'hangman/words.txt'
    tries = 6
    chance = 0
    blank = []
    index = 0

    youWin = False
    Player = 'Computer'

    if path.exists(filePath):
        with open(filePath) as f:
            words = f.read()
            words = words.split('\n')
    else:
        words = ["python", 'java', 'javascript', 'ruby', 'google', 'microsoft']

    while chance < 6:
        if Player == 'Computer':
            word = r.choice(words)
            blank = ['-' for i in word]
            print(chr(27) + "[2J")
            Player = 'You'
        
        # show the gallows
        print(hangman[index])
        print("\n")
        print(' '.join(w for w in blank))
        cprint("Your turn", 'blue', attrs=['bold'], file=sys.stderr)
        if tries-chance > 1:
            print(f"({tries-chance}) chances left")
        else:
            print(f"Only ({tries-chance}) chance left")
        guess = input("Guess a letter: ").lower()

        if guess in blank:
            # even if the letter is correct but the player has 
            # already entered it then also it will be considered wrong
            chance += 1
            index += 1
        elif guess in word:
            # right guess
            for i,w in enumerate(word):
                if guess == w:
                    blank[i] = guess
            guess_str = ''.join(w for w in blank)
            # check if all the letters are guessed
            if guess_str == word:
                youWin = True
                cprint('\nCorrect Word: ', 'yellow', end='')
                cprint(word, 'yellow')
                cprint(youWon, 'green')
                break
        else:
            chance += 1
            index += 1

    if youWin:
        pass
    else:
        # if player 2 lose, display this
        cprint("\n! ! ! ! You have been hanged ! ! ! !", 'red')
        cprint(hangman[index], 'red')
        cprint('\nCorrect Word: ', 'yellow', end='')
        cprint(word, 'yellow')


def twoPlayerMode():
    # loop until 6 wrong guesses
    Player = 1
    tries = 6
    chance = 0
    blank = []
    index = 0
    player2win = False
    while chance < 6:
        # At start ask player 1 to enter a word
        if Player == 1:
            cprint("Player-1", 'yellow', file=sys.stderr)
            word = input("Enter a word: ").lower()
            blank = ['-' for i in word]
            print(chr(27) + "[2J")
            Player = 2

        # show the gallows
        print(hangman[index])
        print("\n")
        print(' '.join(w for w in blank))
        cprint("Player-2", 'blue', attrs=['bold'], file=sys.stderr)
        if tries-chance > 1:
            print(f"({tries-chance}) chances left")
        else:
            print(f"Only ({tries-chance}) chance left")
        guess = input("Guess a letter: ").lower()

        if guess in blank:
            # even if the letter is correct but the player has 
            # already entered it then also it will be considered wrong
            chance += 1
            index += 1
        elif guess in word:
            # right guess
            for i,w in enumerate(word):
                if guess == w:
                    blank[i] = guess
            guess_str = ''.join(w for w in blank)
            # check if all the letters are guessed
            if guess_str == word:
                player2win = True
                cprint('\nCorrect Word: ', 'yellow', end='')
                cprint(word, 'yellow')
                cprint(player2won, 'green')
                break
        else:
            chance += 1
            index += 1

    if player2win:
        pass
    else:
        # if player 2 lose, display this
        cprint("\n! ! ! ! Player-2 has been hanged ! ! ! !", 'red')
        cprint(hangman[index], 'red')
        cprint('\nCorrect Word: ', 'yellow', end='')
        cprint(word, 'yellow')

def start():
    showMenu()
    choice = int(input("Select your choice:(1 or 2): "))

    if choice == 2:
        twoPlayerMode()
    elif choice == 1:
        onePlayerMode()
    else:
        print("Invalid choice!, Try again")

start()



    


