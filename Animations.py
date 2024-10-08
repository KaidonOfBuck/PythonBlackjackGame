# Functions for dealing cards and win/lose screens

from TableSprite import *
from CardSprite import *


#Functions for creating the static assets on screen

def createTable(screenW, screenH):
    table = TableSprite(screenW, screenH)
    return table

def createDeck(screenW):
    deckSprites = pygame.sprite.Group()

    card1 = CardSprite()
    card1.setLandscapeView()
    card1.setRenderLocation(screenW - 120, 100)
    deckSprites.add(card1)

    card2 = CardSprite()
    card2.setLandscapeView()
    card2.setRenderLocation(screenW - 120, 95)
    deckSprites.add(card2)

    card3 = CardSprite()
    card3.setLandscapeView()
    card3.setRenderLocation(screenW - 120, 90)
    deckSprites.add(card3)

    return deckSprites

def createCard(value, suit):
    # start location for cards: (screen width / 2) - 140, (screen height / 2) - 200
    # increment by +35, +20

    card = CardSprite(value, suit)
    return card
