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

"""
this block included in launcher functionality

if screenSizeLarge:
    screenW = screenW * 1.5
    screenH = screenH * 1.5
"""