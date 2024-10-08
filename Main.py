from Card import *
from CardSprite import *
from Deck import *
from TableSprite import *
from LauncherButton import *
from WelcomeSprite import *
from Animations import *
import pygame

from pygame.locals import (
    KEYDOWN as KeyDown,
    K_ESCAPE as kEscape,
    QUIT as Quit,
    MOUSEBUTTONDOWN as mouseButtonDown
)

pygame.init()

"""
Launcher functinality needs dynamic scaling of all assets to work properly.
That will come later, when it won't make my life much harder.

# Defining the screen size for the launcher window
launcherScreenW = 400
launcherScreenH = 250
launcherScreen = pygame.display.set_mode([launcherScreenW, launcherScreenH])
pygame.display.set_caption('Blackjack Launcher')

launcherSprites = pygame.sprite.Group()
launcherButtons = pygame.sprite.Group()

launcher = True # Varibale to keep the launcher window open
screenSizeLarge = True

while launcher:
    for event in pygame.event.get():

        if event.type == KeyDown:
            if event.key == kEscape:
                launcher = False

        elif event.type == Quit:
            launcher = False
        
        if event.type == mouseButtonDown and event.button == 1:
            if button1.rect.collidepoint(event.pos):
                screenSizeLarge = True
                launcher = False
            elif button2.rect.collidepoint(event.pos):
                screenSizeLarge = False
                launcher = False

    launcherScreen.fill((20, 20, 20))

    button1Text = 'Large (1256x1005)'
    button2Text = 'Small (837x670)'

    button1 = LauncherButton(button1Text, (launcherScreenW / 2) - 80, (launcherScreenH / 2))
    launcherSprites.add(button1)
    launcherButtons.add(button1)

    button2 = LauncherButton(button2Text, (launcherScreenW / 2) + 80, (launcherScreenH / 2))
    launcherSprites.add(button2)
    launcherButtons.add(button2)

    for sprite in launcherSprites:
        launcherScreen.blit(sprite.surf, sprite.rect)

    pygame.display.flip()

"""

pygame.quit()

# Defining the screen size for the game window
screenW = 837 * 1.5
screenH = 670 * 1.5

"""
this block included in launcher functionality

if screenSizeLarge:
    screenW = screenW * 1.5
    screenH = screenH * 1.5
"""

screen = pygame.display.set_mode([screenW, screenH])
pygame.display.set_caption('Play Blackjack!')

# Creating Sprite group for rendering
allSprites = pygame.sprite.Group()
deckSprites = pygame.sprite.Group()
welcomeSprites = pygame.sprite.Group()

running = True # Variable to keep the game loop going

# Main Game loop Starts Here
while running:
    for event in pygame.event.get():

        if event.type == KeyDown:
            if event.key == kEscape:
                running = False

        elif event.type == Quit:
            running = False

    screen.fill((35, 96, 59)) #23603b

    # pygame.draw.circle(screen, (255, 0, 0), (screenW /2, screenH / 2), 125)

    # Create the welcome screen sprite
    welcomeScreen = WelcomeSprite(screenW, screenH)
    welcomeSprites.add(welcomeScreen)

    # Create a Table Sprite
    allSprites.add(createTable(screenW, screenH))


    # Create a sprite for the Deck of Cards
    deckSprites.add(createDeck(screenW))
    allSprites.add(deckSprites)

    # Create sprites for different cards
    # start location for cards: (screen width / 2) - 140, (screen height / 2) - 200
    # increment by +35, +20
    
    card = createCard(3, 'Diamonds')
    card.setRenderLocation((screenW / 2) - 140, (screenH / 2) - 200)
    allSprites.add(card)

    # (2, 'Diamonds'), (10, 'Hearts'), (13, 'Clubs')

    # Render all sprites in the allSprites Group
    for sprite in allSprites:
        screen.blit(sprite.surf, sprite.rect)

    # for sprite in welcomeSprites:
    #     screen.blit(sprite.surf, sprite.rect)

    # if event.type == mouseButtonDown and event.button == 1:
    #     if welcomeScreen.rect.collidepoint(event.pos):
    #         welcomeScreen.removeSprite()

    pygame.display.flip()

pygame.quit()