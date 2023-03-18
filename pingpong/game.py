import os
import sys

import pygame

from constants import *
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

        self.font = pygame.font.Font(font_path, 50)
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

        # 공이 게임 화면 위로 넘어간 경우 - 플레이어가 승리한 경우
        if self.ball.rect.y < 0 :
            self.player_score += 1
            self.ball.reset(self.player.rect.centerx, self.player.rect.centery)
        
        # 공이 게임 화면 아래로 넘어간 경우 - 적이 승리한 경우
        elif self.ball.rect.y > SCREEN_HEIGHT:
            self.enemy_score += 1
            self.ball.reset(self.enemy.rect.centerx, self.enemy.rect.centery)

    def display_message(self,screen, message, color):
        label = self.font.render(message, True, color)
        width = label.get_width()
        height = label.get_height()
        pos_x = int((SCREEN_WIDHT/2)-(width/2))
        pos_y = int((SCREEN_HEIGHT/2)-(height/2))
        screen.blit(label, (pos_x, pos_y))
        pygame.display.update()

    def display_frame(self, screen):
        screen.fill(BLUE)

        if self.player_score == 10:
            self.display_message(screen, "승리!",WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)

        elif self.enemy_score == 10:
            self.display_message(screen, "패배!",WHITE)
            self.player_score = 0
            self.enemy_score = 0
            pygame.time.wait(2000)
        else:
            self.ball.draw(screen)
            self.player.draw(screen)
            self.enemy.draw(screen)

        for x in range(0,SCREEN_WIDHT,24):
            pygame.draw.rect(screen,WHITE,[x,int(SCREEN_HEIGHT/2),10,10])

        enemy_score_label = self.font.render(str(self.enemy_score),True,WHITE)
        screen.blit(enemy_score_label,(10,260))

        player_score_label = self.font.render(str(self.player_score),True,WHITE)
        screen.blit(player_score_label,(10,340))
    


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)