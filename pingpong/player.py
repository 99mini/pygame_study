import pygame
from constants import *

class Player():
    def __init__(self, ping_sound) -> None:
        self.rect = pygame.Rect((int(SCREEN_WIDHT / 2), SCREEN_HEIGHT - 40, 50, 15))
        self.ping_sound = ping_sound
        self.dx = 0

    def update(self, ball):

        if self.rect.left <= 0 and self.dx < 0:
            self.dx = 0
        elif self.rect.right >= SCREEN_WIDHT and self.dx > 0:
            self.dx = 0
        
        self.rect.x += self.dx

    def draw(self,screen):
        pygame.draw.rect(screen, RED, self.rect)