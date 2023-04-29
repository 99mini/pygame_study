import pygame 
import os

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 320

GRAY = (200,200,200)

pygame.init()

pygame.display.set_caption("keyboard")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

son_image = pygame.image.load(os.path.join(assets_path, 'son.jpeg'))

son_x = int(SCREEN_WIDTH / 2)
son_y = int(SCREEN_HEIGHT / 2)
son_dx = 0
son_dy = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                son_dx = -3
            elif event.key == pygame.K_RIGHT:
                son_dx = 3
            elif event.key == pygame.K_UP:
                son_dy = -3
            elif event.key == pygame.K_DOWN:
                son_dy = 3
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                son_dx = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                son_dy = 0

    son_x += son_dx
    son_y += son_dy

    screen.fill(GRAY)

    screen.blit(son_image, [son_x,son_y])
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

