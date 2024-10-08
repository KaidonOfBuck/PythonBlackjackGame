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
    MOUSEBUTTONDOWN as mouseButtonDown,
    MOUSEBUTTONUP as mouseButtonUp,
    K_SPACE as kSpace

)

pygame.init()

pygame.quit()

# Defining the default screen size for the game window
screenW = 837 * 1.5
screenH = 670 * 1.5

screen = pygame.display.set_mode([screenW, screenH])
pygame.display.set_caption('Play Blackjack!')

# Creating Sprite group for rendering
allSprites = pygame.sprite.Group()
deckSprites = pygame.sprite.Group()
playerDealerHandSprites = pygame.sprite.Group() #new sprite group for cards dealt to player and dealer
welcomeSprites = pygame.sprite.Group()

# Create a table sprite outside the game loop and render it once
table = createTable(screenW, screenH)
screen.fill((35, 96, 59)) #23603b
screen.blit(table.surf, table.rect)

# Create the welcome screen sprite and render it before game starts
# welcomeScreen = WelcomeSprite(screenW, screenH)
# screen.blit(welcomeScreen.surf, welcomeScreen.rect)

running = True # Variable to keep the game loop going

# Main Game loop Starts Here
while running:
    for event in pygame.event.get():

        if event.type == KeyDown and event.key == kEscape:
            running = False

        elif event.type == Quit:
            running = False
        
        # elif event.type == mouseButtonUp and event.button == 1:
        #     welcomeScreen.removeSprite()

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

    pygame.display.flip()

pygame.quit()