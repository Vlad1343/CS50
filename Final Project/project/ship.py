import pygame
from pygame.sprite import Sprite



class Ship(Sprite):
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # self.image = pygame.image.load('alien_invasion/images/spaceship.bmp')
        self.image = pygame.image.load('Final Project/project/spaceship.bmp')

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

class AIGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.ship = Ship(self)

    def run(self):
        while True:
            self.screen.fill((230, 230, 230))
            self.ship.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    game = AIGame()
    game.run()

