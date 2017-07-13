import pygame
#from board import Sizes
#from board import Board
import board

def main():
    # testing the board class
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    #surf = pygame.Surface((1400, 1400))
    clock = pygame.time.Clock()

    running = True

    print('Initializing board...')
    game_board = board.Board(3)
    #test_box = board.Box()
    #test_box.init_rect(100, 500)
    screen.fill((255, 255, 255))
    
    game_board.update(1, board.Sizes.BIG, (255, 0, 0), (0, 0))
    game_board.update(1, board.Sizes.BIG, (255, 0, 0), (1, 1))
    game_board.update(1, board.Sizes.BIG, (255, 0, 0), (2, 2))
    game_board._print_board()
    print(game_board.check_if_win())
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
