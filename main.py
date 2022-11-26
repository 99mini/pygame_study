import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.display.set_caption('pygame')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


clock = pygame.time.Clock()

done = False
while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
    
    screen.fill(WHITE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()