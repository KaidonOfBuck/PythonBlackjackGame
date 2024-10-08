import pygame

class LauncherButton(pygame.sprite.Sprite):
    def __init__(self, text, Xpos, Ypos):
        super(LauncherButton, self).__init__()

        self.surf = pygame.Surface((150, 75))
        self.surf.fill((128, 128, 128))
        self.rect = self.surf.get_rect()

        font = pygame.font.Font(None, 24)
        self.text = font.render(text, True, (255, 255, 255))
        self.text_rect = self.text.get_rect(
            center=(
                self.surf.get_width() / 2,
                self.surf.get_height() / 2
            )
        )
        self.surf.blit(self.text, self.text_rect)

        self.setStartLocation(Xpos, Ypos)

    def setStartLocation(self, Xpos, Ypos):
        self.rect = self.surf.get_rect(
            center=(
                Xpos,
                Ypos
            )
        )
    