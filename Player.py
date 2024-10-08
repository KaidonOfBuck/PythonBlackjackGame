from Card import *

class Player:
    def __init__(self):
        self.hand = []
        self.handValue = 0

    def getHand(self) -> list[Card]: # Returns the array hand
        return self.hand

    def getHandValue(self): # Returns the integer handValue
        return self.handValue

    def setHand(self, arr): # Sets the hand to an array
        self.hand = arr

    def setHandValue(self, int): # Sets the handValue to an integer
        self.handValue = int

    def resetHand(self): # Resets the hand to an empty array
        self.hand = []

    def resetHandValue(self): # Resets the handValue to 0
        self.handValue = 0

    def addCardToHand(self, card): # Adds a card object to the hand array
        self.hand.append(card)

    def removeCardFromHand(self, index = None): # Removes a card from the hand (default, last card in the array)
        if not index:
            index = len(self.hand) - 1

        self.hand.pop(index)