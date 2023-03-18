import pygame
from constants import *

class Ball():
    def __init__(self, bounce_sound) -> None:
        self.rect = pygame.Rect(int(SCREEN_WIDHT / 2), int(SCREEN_HEIGHT/2),12,12)
        self.bounce_sound = bounce_sound
        self.dx = 0
        self.dy = 5

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.left < 0:
            self.dx *= -1
            self.rect.left = 0
            self.bounce_sound.play()
        elif self.rect.right > SCREEN_WIDHT:
            self.dx *= -1
            self.rect.right = SCREEN_WIDHT
            self.bounce_sound.play()

    def draw(self, screen):
        pygame.draw.rect(screen, ORANGE, self.rect)