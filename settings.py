class Settings:
    """Class for all game setting """

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (30, 90, 136)
        self.speed_spaceship = 1

        self.shot_speed = 3
        self.shot_width = 5
        self.shot_height = 15
        self.shot_limited = 3
        self.shot_color = (20, 20, 20)

        self.aliens_rows = 6
        self.aliens_speed = 0.3
        self.aliens_direction = 1
        self.aliens_drop = 5
