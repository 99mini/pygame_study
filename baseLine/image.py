import pygame
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320

LAND = (160,120,40)

pygame.init()

pygame.display.set_caption("우리 흥")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

background_image = pygame.image.load(os.path.join(assets_path, 'son.jpeg'))
money_image = pygame.image.load(os.path.join(assets_path, 'money.jpg'))
money_image = pygame.transform.scale(money_image, (100, 100))


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(LAND)

    screen.blit(background_image,background_image.get_rect())
    screen.blit(money_image, [80,60])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()