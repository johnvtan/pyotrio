import pygame
import sys
import Board

# defining the size of the screen
SIZE = WIDTH, HEIGHT = 1800, 1800

# color definitions - maybe own library or something for this, or maybe it would fit better
# in the library for the game board/square
BLACK = (0, 0, 0)
RED =(255, 0, 0)
GREEN = (0, 255, 0)
BLUE =(0, 0, 255)
WHITE =(255, 255, 255)

def main():
    
    # initialization stuff
    pygame.init()
    screen = pygame.display.set_mode(SIZE)

    # define our surface as the same size as the screen 
    surface = pygame.surface(screen.get_size()
    pygame.display.set_caption('OTRIO')
    clock = pygame.time.Clock()

    Board.board_init()
    # initializing board as 3x3 array, filled with None rn
    board = [[None, None, None]] * 3

    # variable to check win condition
    running = True

    while running:
        # poll user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
        # game logic
        
        # draw screen logic
        draw_screen()
        pygame.display.flip()
        clock.tick(60) # 60 fps


def draw_screen():
    screen.fill(WHITE)
    pygame.draw.rect
    

if __name__ == '__main__':
    main()
