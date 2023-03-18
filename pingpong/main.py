import pygame
from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDHT
from game import Game


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDHT,SCREEN_HEIGHT))
    pygame.display.set_caption("PingPong Game")
    clock = pygame.time.Clock()
    game = Game()

    done = False
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ =="__main__":
    main()