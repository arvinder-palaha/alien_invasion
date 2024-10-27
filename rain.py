import pygame
from pygame.sprite import Sprite
import random

class Rain(Sprite):
    """A class to manage rain."""

    def __init__(self, ai_game):
        """Initialize the rain and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # create a rain drop and set its rect attribute.
        self.rect = pygame.Rect(0, 0, 1, 4)

        # set random position for the rain drop
        self.rect.x = random.randint(0, self.settings.screen_width)
        self.rect.y = self.screen_rect.top
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the rain drop down the screen."""
        self.y += self.settings.rain_speed
        self.rect.y = self.y
        
    def draw_rain(self):
        """Draw the rain drop at its current location."""
        pygame.draw.rect(self.screen, self.settings.rain_color, self.rect)