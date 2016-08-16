import pygame
import board

def main():
    # testing the board class
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    #surf = pygame.Surface((1400, 1400))
    clock = pygame.time.Clock()

    running = True

    print('Initializing board...')
    game_board = board.Board()
    test_box = board.Box()
    test_box.init_rect(100, 500)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
   
        screen.fill((250, 250, 250)) 
        #test_box.draw_box(screen)
        game_board.draw_board(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
