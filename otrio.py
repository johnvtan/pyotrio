import pygame
import sys

# defining the size of the screen
SIZE = WIDTH, HEIGHT = 1000, 1000

# color definitions - maybe own library or something for this, or maybe it would fit better
# in the library for the game board/square
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
WHITE = 255, 255, 255

def main():
    screen = pygame.display.set_mode(SIZE)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)
    pygame.display.flip()

if __name__ == '__main__':
    main()
