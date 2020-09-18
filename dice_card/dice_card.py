# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:28:58 2020

@author: Asus
"""
from random import randint, shuffle

rules_and_instruction = """
** 24 Cards and a Dice **

Rules:
1. Player1 and Player2 name must be different.
2. Player1 plays first and then Player2's turn comes.
3. A is considered as 1.
4. Card deck contains only 24 cards (A-6)

Instructions:
The game is about getting the highest score. 
A player will first shuffle a deck of 24 cards.
Then shows one card and keeps it a side.
Then he/she have to throw a dice and if he/she gets the same number as in the card then
he/she gets the point equal to that number and that point will get added to his/her score.
Each player have 5 chances of throwing the dice for each card shown.
Each player continues this until the deck of cards gets empty.
Player scoring the highest point will be the winner.
"""
# returns the shuffle deck of 24 cards
def createDeck():
    """
    Deck should contain cards from 1(A) - 6 only (total 24 cards)
    """
    deck = []
    faceCard = ["A"]
    for i in range(4):
        deck.append("A")
        for j in range(2, 7):
            deck.append(j)
    shuffle(deck)
    return deck
        
# creates a player
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.currentCard = None
        
    def __str__(self):
        score = "Player name: {}\nScore: {}".format(self.name, 
                                                    self.score)
        return score
        
    def getDeck(self, deck):
        self.deck = deck
    
    def throwCard(self):
        self.currentCard = self.deck.pop()
        return self.currentCard
        
    def rollDice(self):
        diceNumber = randint(1, 6)
        print(diceNumber)
        if self.currentCard == 'A':
            if diceNumber == 1:
                self.score += diceNumber
                print("Matched")
                print("Points earned:",diceNumber)
                return True
        if diceNumber == self.currentCard:
            self.score += diceNumber
            print("Matched")
            print("Points earned:",diceNumber)
            return True
        return False

# prints the Rules and Instructions
def help():
    print(rules_and_instruction)
    while True:
        action = input("type --resume and hit enter to resume the game: ")
        if action == '--resume':
            break

def playGame(Player):  
    deck = createDeck()
    Player.getDeck(deck)
    
    while (len(Player.deck) > 0):
        action = input(f"({Player.name})Do you want to throw a card (y/n): ")
        
        if action == '--help':
            help()
        elif action == "y":
            print("Total cards remaining:", len(Player.deck))
            Player.throwCard()
            print("Card:", Player.currentCard)
            chance = 0
            while chance < 5:
                print(f"{5-chance} chances left")
                act = input("Throw a Dice: (y/n)")
                if act == '--help':
                    help()
                elif act == 'y':
                    win = Player.rollDice()
                    if win:
                        break
                    chance += 1
                elif act == 'n':
                    break
                print("Not Matched")
        elif action == 'n':
            break
    
    return Player.score

# Starts the game
def startGame():
    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name: ")
    while name2 == name1:
        print("**** Player names must be different ****")
        name2 = input("Enter Player 2 name: ")
    player = 1
    Player1 = Player(name1)
    Player2 = Player(name2)
    
    for i in range(2):
        if player == 1:
            print(f"\n**** {Player1.name}'s turn ****")
            playGame(Player1)
            print(chr(27) + "[2J") 
            player = 2
        else:
            print(f"\n**** {Player2.name}'s turn ****")
            playGame(Player2)
    
    # print player 1's & player 2's info
    print(Player1)
    print()
    print(Player2)
    
    print("\n### Result ###/n")
    # check who has won the game
    if Player1.score > Player2.score:
        print("!!!! *** {} won by {} points *** !!!!".format(Player1.name, 
                                           Player1.score-Player2.score))
    elif Player1.score == Player2.score:
        print("*********** Draw ************")
    else:
        print("!!!! *** {} won by {} points*** !!!!".format(Player2.name, 
                                           Player2.score-Player1.score))
        
startGame()
print("\n~~~~~~ Thans for playing ~~~~~~")
    
    

        
        