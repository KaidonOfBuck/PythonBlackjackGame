class Card:

    # Constructor Function
    def __init__(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit
        self.faceUp = False

        match suit:
            case 'Spades' | 'Clubs':
                self.color = 'Black'
            case 'Diamonds' | 'Hearts':
                self.color = 'Red'
            case 'Jokers':
                self.color = 'Black'
    

    # Functions to return the class attributes
    def getValue(self):
        return self.value
    
    def getName(self):
        return self.name
    
    def getSuit(self):
        return self.suit
    
    def getColor(self):
        return self.color
    
    def getFaceUp(self):
        return self.faceUp
    
    # Functoins to set or change the class attributes
    def setValue(self, value):
        self.value = value

    def setName(self, name):
        self.name = name

    def setSuit(self, suit):
        self.suit = suit

    def setColor(self, color):
        self.color = color

    def setFaceUp(self, faceUp):
        self.faceUp = faceUp

    # Unique function to change all the attributes of the class at once
    def changeCard(self, value, name, suit):
        self.value = value
        self.name = name
        self.suit = suit

        # Sets the card's color based on it's assigned suit
        match suit:
            case 'Spades' | 'Clubs':
                self.color = 'Black'
            case 'Diamonds' | 'Hearts':
                self.color = 'Red'
            case 'Jokers':
                self.color = 'Black'

    # Function to print the card to the console
    def showCard(self):
        print('Card: ' + self.name + ' of ' + self.suit + '. Value: ' + str(self.value))