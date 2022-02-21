import pygame
from pygame.sprite import Sprite


class AlienShip(Sprite):
    """Definition and operation of alienship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screan = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/alienship.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width   # free space from left is the same how width img
        self.rect.y = self.rect.height  # free space from top  is the same how height img

        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.aliens_speed * self.settings.aliens_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screan.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

