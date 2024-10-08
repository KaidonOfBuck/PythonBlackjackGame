import pygame

class WelcomeSprite(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super(WelcomeSprite, self).__init__()

        image = pygame.image.load('img/welcome.png')
        image = pygame.transform.scale(image, (w,  h))

        self.surf = image.convert()
        self.rect = self.surf.get_rect(
            center = (
                w / 2,
                h / 2
            )
        )

    def removeSprite(self):
        self.kill()