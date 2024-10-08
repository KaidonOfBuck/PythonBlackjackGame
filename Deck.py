from Card import *
from MergeSort import *
import random

class Deck:

    # Constructor Function
    def __init__(self, blackjackDeck = False):
        self.data = []
        self.isSorted = None
        self.isNewDeckOrder = None
        self.containsJokers = None

        if blackjackDeck:
            self.createBlackjackDeck()
        else:
            self.createStandardDeck()

    # Creates a standard deck of 52 cards in new deck order
    def createStandardDeck(self):
        self.data = []
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

        for i in range(2):
            for j in range(1, 14):
                if j > 1 and j < 11:
                    self.data.append(Card(j, str(j), suits[i]))
                else:
                    match j:
                        case 1:
                            self.data.append(Card(j, 'Ace', suits[i]))  
                        case 11:
                            self.data.append(Card(j, 'Jack', suits[i]))
                        case 12:
                            self.data.append(Card(j, 'Queen', suits[i]))
                        case 13:
                            self.data.append(Card(j, 'King', suits[i]))
        
        for i in range(2, 4):
            for j in range(13, 0, -1):
                if j > 1 and j < 11:
                    self.data.append(Card(j, str(j), suits[i]))
                else:
                    match j:
                        case 1:
                            self.data.append(Card(j, 'Ace', suits[i]))  
                        case 11:
                            self.data.append(Card(j, 'Jack', suits[i]))
                        case 12:
                            self.data.append(Card(j, 'Queen', suits[i]))
                        case 13:
                            self.data.append(Card(j, 'King', suits[i]))

        self.isSorted = False
        self.isNewDeckOrder = True
        self.containsJokers = False

    # Creates a deck of 54 cards with 2 jokers at the front of the deck
    def createJokerDeck(self):
        self.data = []
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

        self.data.append(Card(0, 'Joker', 'Jokers')) * 2

        for i in range(2):
            for j in range(1, 14):
                if j > 1 and j < 11:
                    self.data.append(Card(j, str(j), suits[i]))
                else:
                    match j:
                        case 1:
                            self.data.append(Card(j, 'Ace', suits[i]))  
                        case 11:
                            self.data.append(Card(j, 'Jack', suits[i]))
                        case 12:
                            self.data.append(Card(j, 'Queen', suits[i]))
                        case 13:
                            self.data.append(Card(j, 'King', suits[i]))
        
        for i in range(2, 4):
            for j in range(13, 0, -1):
                if j > 1 and j < 11:
                    self.data.append(Card(j, str(j), suits[i]))
                else:
                    match j:
                        case 1:
                            self.data.append(Card(j, 'Ace', suits[i]))  
                        case 11:
                            self.data.append(Card(j, 'Jack', suits[i]))
                        case 12:
                            self.data.append(Card(j, 'Queen', suits[i]))
                        case 13:
                            self.data.append(Card(j, 'King', suits[i]))

        self.isSorted = False
        self.isNewDeckOrder = True
        self.containsJokers = True


    def createBlackjackDeck(self):
        self.data = []
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

        for i in range(4):
            for j in range(1, 14):
                if j > 1 and j < 11:
                    self.data.append(Card(j, str(j), suits[i]))
                elif j == 1:
                    self.data.append(Card(j, 'Ace', suits[i]))
                else:
                    match j:
                        case 11:
                            self.data.append(Card(10, 'Jack', suits[i]))
                        case 12:
                            self.data.append(Card(10, 'Queen', suits[i]))
                        case 13:
                            self.data.append(Card(10, 'King', suits[i]))

        self.isSorted = False
        self.isNewDeckOrder = False
        self.containsJokers = False
    
    # shuffles the deck by shuffling the numbers 0 to 51
    # then adds the card at each index to a new list
    def shuffleDeck(self):

        nums = list(range(0,52))
        random.shuffle(nums)

        shuffledDeck = []

        for i in nums:
            shuffledDeck.append(self.data[i])

        self.data = shuffledDeck
        self.isSorted = False
        self.isNewDeckOrder = False

    # sorts the deck by adding each suit to its own list
    # then sorts each list by value
    # then adds the 4 smaller  lists to a larger list to contain the whole deck
    def sortDeck(self):

        suitList = [[], [], [], [], []]

        for i in self.data:
            match i.getSuit():
                case 'Jokers':
                    suitList[0].append(i)
                case 'Spades':
                    suitList[1].append(i)
                case 'Diamonds':
                    suitList[2].append(i)
                case 'Clubs':
                    suitList[3].append(i)
                case 'Hearts':
                    suitList[4].append(i)
                case _:
                    print("There has been an error")
                    break
        
        for j in suitList:
            MergeSortDeck(j, 0, len(j) - 1)

        a = 0
        b = 0
        c = 0

        for a in suitList:
            for b in a:
                self.data[c] = b
                c += 1
        
        self.isSorted = True
        self.isNewDeckOrder = False

    # Sorts the deck by the Card value first, then by suit
    def sortByValue(self):
        
        if self.isSorted == False:
            self.sortDeck()

        subList = []

        while self.data[0].getSuit() == 'Jokers':
            subList.append(self.data[0])
            self.data.pop(0)

        
        j = 0
        while j < 13:
            for i in range(j, len(self.data), 13):
                subList.append(self.data[i])
            j += 1
            
        self.data = subList

    # Returns the full list of cards in the deck
    def getData(self):
        return self.data

    # Function to print all cards in the deck
    def displayAllCards(self):
        for i in range(len(self.data)):
            print(self.data[i].getName() + ' of ' + self.data[i].getSuit())

    # Function to get the card a specific postion in the deck
    def getCardAtPosition(self, pos):
        return self.data[pos - 1]
    
    # Function to display the card a specific postion in the deck
    def displayCardAtPosition(self, pos):
        print(self.data[pos - 1].getName() + ' of ' + self.data[pos - 1].getSuit())

    # Removes Jokers from the Deck if they are present
    def removeJokers(self):

        if self.isSorted == False:
            self.sortDeck()

        while self.data[0].getSuit() == 'Jokers':
            self.data.pop(0)

        self.containsJokers = False

    # Adds 2 Jokers to the Deck if there are none present
    def addJokers(self):

        jokers = 0

        # Search the deck for Jokers
        for i in self.data:
            if i.getSuit() == 'Jokers':
                jokers += 1

        while jokers < 2:
            self.data.insert(0, Card(0, 'Joker', 'Jokers'))
            jokers += 1

        self.containsJokers = True

    def dealCard(self):
        return self.data.pop(0)