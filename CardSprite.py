import pygame

class CardSprite(pygame.sprite.Sprite):
    def __init__(self, value = None, suit = None):
        super(CardSprite, self).__init__()

        
        if value and suit:
            self.faceUp = True
        else:
            self.faceUp = False

        self.value = value
        self.suit = suit

        if self.faceUp == False:
            image = pygame.image.load("img/cardBack_red4.png")
        else:
            filename = self.setCardFace(value, suit)
            image = pygame.image.load('img/' + filename)

        self.surf = image.convert()
        self.rect = self.surf.get_rect()

    def setRenderLocation(self, Xpos, Ypos):
        self.rect = self.surf.get_rect(
            center=(
                Xpos,
                Ypos
            )
        )
    
    def setLandscapeView(self):
        image = pygame.image.load("img/cardBack_red4.png")
        image = pygame.transform.rotate(image, 90)
        self.surf = image.convert()
        self.rect = self.surf.get_rect()

    def setCardFace(self, value, suit):
        filename = 'card'

        match suit:
            case 'Spades':
                filename = filename + 'Spades'
            case 'Clubs':
                filename = filename + 'Clubs'
            case 'Diamonds':
                filename = filename + 'Diamonds'
            case 'Hearts':
                filename = filename + 'Hearts'
            case 'Jokers':
                filename = filename + 'Joker'
            case _:
                pass

        filename = filename + str(value) + '.png'
        return filename
