import pygame
from pygame.sprite import Sprite


class Shot(Sprite):
    """efinition and operations of shot from spaceship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.shot_color

        self.rect = pygame.Rect(0, 0, self.settings.shot_width, self.settings.shot_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.shot_speed
        self.rect.y = self.y

    def show_shot(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
