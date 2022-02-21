# **Space-freaks**
### The game was created with the purpose of learning Python

#### I used the pygame library and practiced my language Python.
> #### In the game we move with arrows and space keys.

![space_freaks_imgscrean](https://user-images.githubusercontent.com/58234228/155032379-8d58f5a5-c8fd-435b-b213-31ba2aba55e9.PNG)

```python
import pygame
from settings import Settings
from spaceship import SpaceShip
from shot import Shot
from alienship import AlienShip


class SpaceFreaks:
    """Definition of settings and game operations"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()  # class contain settings game

        # set size screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Test for full screen
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Space freaks")  # Set the current window caption

        self.ship = SpaceShip(self)  # New obj wit parameter self - Access for var form class space_freaks
        self.shots = pygame.sprite.Group()  # Sprite group to management shots
        self.alienships = pygame.sprite.Group()
        self._create_alienships()

        self.game_active = True
        self.game_win = False

    def run_game(self):
        while True:  # Head loop of program
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.shots.update()
                self._update_scren()
            elif self.game_win is True and self.game_active is False:
                self._info_win()
            elif self.game_active is False:
                self._info_restart()

    def _check_events(self):
        for event in pygame.event.get():  # get events from queue interacting
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup(event)

            # print(event)  # Print all motion users

    def _check_keydown(self, event):
        if event.key == pygame.K_RIGHT:  # To turn right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # To turn left
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # Key for end of game
            sys.exit()
        elif event.key == pygame.K_SPACE:  # Key for fire shot
            self._create_fire_shot()
        elif event.key == pygame.K_r:
            self._restart_game()

    def _check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_scren(self):
        self.screen.fill(self.settings.bg_color)  # Update background color
        self.ship.blitme()  # Show spaceship
        self._update_shot()
        self._update_alienships()
        # self._info_restart()
        self.alienships.draw(self.screen)
        pygame.display.flip()

    def _create_fire_shot(self):
        new_shot = Shot(self)
        if len(self.shots) < self.settings.shot_limited:  # Limited shot
            self.shots.add(new_shot)

    def _update_shot(self):
        for shot in self.shots.sprites():
            shot.show_shot()
            if shot.rect.y <= 0:  # delete shot behind the screen
                self.shots.remove(shot)
        # print(len(self.shots))

        # check shots if hit delete alien ship and shot
        if pygame.sprite.groupcollide(self.shots, self.alienships, True, True):
            self.settings.aliens_drop += 0.8  # if hit +0.8 to speed drop

    def _create_alienships(self):
        alienship = AlienShip(self)
        alienship_width = alienship.rect.width
        max_space_x = self.settings.screen_width - (2 * alienship_width)
        max_alienships = max_space_x // (2 * alienship_width)

        for how_many_rows in range(1, self.settings.aliens_rows):
            for alien_ship_numer in range(max_alienships):
                alienship = AlienShip(self)
                alienship.x = alienship_width + 2 * alienship_width * alien_ship_numer
                alienship.rect.x = alienship.x
                alienship.rect.y = alienship_width * how_many_rows
                self.alienships.add(alienship)

    def _update_alienships(self):
        self._check_aliensships_edges()
        self.alienships.update()
        if pygame.sprite.spritecollideany(self.ship, self.alienships):
            print("Statek trafiony")
            self.game_active = False
        if len(self.alienships.spritedict) == 0:
            self.game_win = True
            self.game_active = False

    def _check_aliensships_edges(self):
        for alien in self.alienships.sprites():
            if alien.check_edges():
                self._change_aliensships_direction()
                break

    def _change_aliensships_direction(self):
        for alienship in self.alienships.sprites():
            alienship.rect.y += self.settings.aliens_drop
        self.settings.aliens_direction *= -1

    def _info_restart(self):
        font = pygame.font.SysFont("Verdana", 30)
        text = "GAME OVER - alien ship touched you - RESTART PRESS R"
        text_show = font.render(text, True, (0, 0, 0))
        self.rect = self.screen.get_rect()
        self.screen.blit(text_show, text_show.get_rect(center=self.screen.get_rect().center))
        pygame.display.flip()

    def _info_win(self):
        font = pygame.font.SysFont("Verdana", 30)
        text = "YOU WIN - RESTART PRESS R"
        text_show = font.render(text, True, (0, 0, 0))
        self.rect = self.screen.get_rect()
        self.screen.blit(text_show, text_show.get_rect(center=self.screen.get_rect().center))
        pygame.display.flip()

    def _restart_game(self):
        self.game_active = True

        self.alienships.empty()
        self.shots.empty()

        self._create_alienships()

```
