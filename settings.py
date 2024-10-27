class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed = 1.0

        # star settings
        self.star_color = (192, 192, 192)
        self.star_size = 2
        self.star_density = 0.0001
        
        # rain settings
        self.rain_speed = 2.0
        self.rain_density = 0.003
        self.rain_color = (0, 0, 127)