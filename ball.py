import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.display.set_caption('파이선')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))


clock = pygame.time.Clock()

ball_x = int(SCREEN_WIDTH / 2)
ball_y = int(SCREEN_HEIGHT / 2)
ball_dx = 4
ball_dy = 4
ball_size = 40


done = False
while not done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
    
    ball_x += ball_dx
    ball_y += ball_dy 
    if (ball_x + ball_size) > SCREEN_WIDTH or (ball_x - ball_size) < 0:
        ball_dx *= -1
    if (ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) < 0:
        ball_dy *= -1
        
    max_speed = 100
    if (ball_dx > max_speed or ball_dx < -1 * max_speed or ball_dy > max_speed or ball_dy < -1 * max_speed):
        ball_dx *= 0.5
        ball_dy *= 0.5


    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, [ball_x,ball_y], ball_size, 0)
    pygame.display.flip()



    clock.tick(60)

pygame.quit()