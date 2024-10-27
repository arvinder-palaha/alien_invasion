import pygame
from pygame.sprite import Sprite
import random

class Star(Sprite):
    """A class to represent a single star in the sky."""    
    def __init__(self, ai_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Create a star rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.star_size, self.settings.star_size)
        self.rect.x = random.randint(0, self.settings.screen_width)
        self.rect.y = random.randint(0, self.settings.screen_height)


    def draw_star(self):
        """Draw the star at its current location."""
        pygame.draw.circle(self.screen, self.settings.star_color, self.rect.center, self.settings.star_size)