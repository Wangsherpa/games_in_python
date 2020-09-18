# -*- coding: utf-8 -*-

from random import shuffle
def createDeck():
    Deck = []
    faceCards = ["A", "J", "Q", "K"]
    
    for i in range(4):
        for card in range(2, 11):
            Deck.append(str(card))
            
        for card in faceCards:
            Deck.append(card)
    shuffle(Deck)
    return Deck


class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet = 0
        
    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = "\n"+currentHand + "Score: " + str(self.score)
        
        return finalStatus
    
    def set_score(self):
        self.score = 0
        faceCardsDict = {"A":11, "J":10, "K":10, "Q":10,
                         "2":2, "3":3, "4":4, "5":5,
                         "6":6, "7":7, "8":8, "9":9, "10":10}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
                
        return self.score
    
    def hit(self, newCard):
        self.hand.append(newCard)
        self.score = self.set_score()
    
    def play(self, newHand):
        self.hand = newHand
        self.score = self.set_score()
        
    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount
        
    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        return False
    
    def draw(self):
        self.money += self.bet
        self.bet = 0
        
    def win(self, result):
        if result:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
                self.money += 2 * self.bet
            self.bet = 0
        else:
            self.bet = 0
    
def printHouse(house):
    for card in range(len(house.hand)):
        if card == 0:
            print('X', end=' ')
        elif card == (len(house.hand)-1):
            print(house.hand[card])
        else:
            print(house.hand[card], end=' ')
    
Deck = createDeck()
firstHand = [Deck.pop(), Deck.pop()]
secondHand = [Deck.pop(), Deck.pop()]
player1 = Player(firstHand)
House = Player(secondHand)

while player1.money > 0:
    if len(Deck) < 20:
        Deck = createDeck()
    print("\n",Deck)
    firstHand = [Deck.pop(), Deck.pop()]
    secondHand = [Deck.pop(), Deck.pop()] 
    player1.play(firstHand)
    House.play(secondHand)
    print("Player1:",player1)
    print("\nHouse:")
    printHouse(House)
    
    Bet = int(input("Please enter your bet: "))
    player1.betMoney(Bet)
    
    if player1.hasBlackJack():
        if House.hasBlackJack():
            player1.draw()
        else:
            player1.win(True)
    else:
        while player1.score < 21:
            action = input("Do you want to take the card again (y/n): ")
            if action == 'y':
                player1.hit(Deck.pop())
                print(player1)
                printHouse(House)
            else:
                break
            
        while House.score < 16:
            House.hit(Deck.pop())
        
        if player1.score > 21:
            if House.score > 21:
                player1.draw()
                print("***** Draw *****")
            else:
                player1.win(False)
                print("***** Lose *****")
        elif player1.score == House.score:
            player1.win(False)
            print("***** Draw *****")
        else:
            if player1.score < House.score:
                if House.score <= 21:
                    player1.win(False)
                    print("***** Lose *****")
                else:
                    player1.win(True)
                    print("***** Win *****")
            else:
                player1.win(True)
                print("***** Win *****")
            
    print("House:",House)
    print(f"Total Money: ${player1.money}")
    



        
        
        
        
        
        
        
        
        
        
        
        
        
