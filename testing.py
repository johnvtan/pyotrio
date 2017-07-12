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
    screen.fill((255, 255, 255))
    
    game_board.update(1, 'med', (255, 0, 0), (1, 1))
    game_board.update(2, 'big', (0, 255, 0), (0, 0))
    game_board.update(3, 'small', (0, 0, 255), (2, 1))
    game_board._print_board()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
   
        #screen.fill((255, 255, 255)) 
        #test_box.draw_box(screen)
        game_board.draw_board(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
