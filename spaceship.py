import pygame


class SpaceShip:
    """Definition and operations of spaceship"""

    def __init__(self, ai_game):  # ai_game get parammetrs
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.speed_spaceship = ai_game.settings.speed_spaceship

        # Load img
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom  # Defoult position ships = midbottom position in screen

        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed_spaceship

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.speed_spaceship

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

