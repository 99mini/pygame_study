import pygame

from constants import *
from ball import Ball


class Enemy():
    def __init__(self, pong_sound: pygame.mixer.Sound):
        self.rect = pygame.Rect(int(SCREEN_WIDHT/2),25,50,15)
        self.pong_sound = pong_sound
    
    def update(self,ball:Ball):
        if self.rect.centerx > ball.rect.centerx:
            diff = self.rect.centerx - ball.rect.centerx
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x -= 4
        elif self.rect.centerx < ball.rect.centerx:
            diff = ball.rect.centerx - self.rect.centerx 
            if diff <= 4:
                self.rect.centerx = ball.rect.centerx
            else:
                self.rect.x += 4
        if self.rect.colliderect(ball.rect):
            ball.dy *= -1
            ball.rect.top = self.rect.bottom
            self.pong_sound.play()
        
    def draw(self,screen):
        pygame.draw.rect(screen,BLACK, self.rect)