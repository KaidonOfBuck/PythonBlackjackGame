import pygame

class TableSprite(pygame.sprite.Sprite):
    def __init__(self, screenW, screenH):
        super(TableSprite, self).__init__()
        image = pygame.image.load("img/table.png")
        image = pygame.transform.scale(image, (837, 670))
        self.surf = image.convert()
        self.rect = self.surf.get_rect(
            center=(
                screenW / 2,
                screenH / 2
            )
        )