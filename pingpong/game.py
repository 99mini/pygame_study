import os
import sys

import pygame

from constants import BLUE
from ball import Ball
from enemy import Enemy
from player import Player


class Game():
    def __init__(self):
        bounce_path = resource_path("pingpong/assets/bounce.wav")
        ping_path = resource_path("pingpong/assets/ping.wav")
        pong_path = resource_path("pingpong/assets/pong.wav")
        font_path = resource_path("pingpong/assets/NanumGothicCoding-Bold.ttf")

        bounce_sound = pygame.mixer.Sound(bounce_path)
        ping_sound = pygame.mixer.Sound(ping_path)
        pong_sound = pygame.mixer.Sound(pong_path)

        self.ball = Ball(bounce_sound)
        self.player = Player(ping_sound)
        self.enemy = Enemy(pong_sound)

        self.player_score = 0
        self.enemy_score = 0

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.dx -= 5
                elif event.key == pygame.K_RIGHT:
                    self.player.dx += 5
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.player.dx = 0
    def run_logic(self):
        self.ball.update()
        self.player.update(self.ball)
        self.enemy.update(self.ball)

    def display_message(self,screen, message, color):
        pass

    def display_frame(self, screen):
        screen.fill(BLUE)
        self.ball.draw(screen)
        self.player.draw(screen)
        self.enemy.draw(screen)
    


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)