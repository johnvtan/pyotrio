import pygame

OFFSET = (300, 50)

class Box():
    ''' Contains all relevant info for each box in board grid '''
    def __init__(self):

        # the Box should have some coordinate on the board, where (0,0) is the bottom left box
        # and (2,2) is the top-right box
        self.coord = (None, None)
        
        # tracking states of pieces in the grid
        # also need to track colors
        self.big = False
        self.big_color = None
        self.big_rad = 80 

        self.med = False
        self.med_color = None
        self.med_rad = 50
       
        self.small = False
        self.small_color = None
        self.small_rad = 25       

        # next two are going to be used later
        # rect is a pygame.rect object
        # center_pos is its center, for drawing circles
        self.rect_color = (0, 0, 0) 
        self.center = None
        self.rect = None

        # for use w/ draw.rect - (left, top, width, height)
        #self.area = (None, None, None, None)
        # constants relevant to the box
        self.side_length = 200
        self.line_width = 10 

    def init_rect(self, left, top):
        self.rect = pygame.Rect(left, top, self.side_length, self.side_length)
        #self.area = (left, top, self.side_length, self.side_length)
        self.center = (int(left + self.side_length / 2), int(top + self.side_length / 2))

    def add_piece(self, size, color):
        ''' adds a piece to the box (big, medium, small) '''
        if size == 'big':
            self.big = True
            self.big_color = color
        elif size == 'med':
            self.med = True
            self.med_color = color
        elif size == 'small':
            self.small = True
            self.small_color = color
        else:
            print('Error: invalid piece size')

    def draw_box(self, surface):
        ''' function for drawing everything inside the box '''
        pygame.draw.rect(surface, self.rect_color, self.rect, self.line_width)
        if self.big is True:
            pygame.draw.circle(surface, self.big_color, self.center, self.big_rad, self.line_width)
        if self.med is True:
            pygame.draw.circle(surface, self.med_color, self.center, self.med_rad, self.line_width)
        if self.small is True:
            pygame.draw.circle(surface, self.small_color, self.center, self.small_rad, self.line_width)
 

class Board():
    ''' This class contains all the game logic and tracks the board state '''
    def __init__(self):
        
        # defines board_state as 3x3 array of Box() objects
        # note that board_state is entirely for visual purposes
        self.board_state =[[Box(), Box(), Box()], [Box(), Box(), Box()], [Box(), Box(), Box()]]
        
        # raw_state is what's used to check if win, and keep track of which 
        # player played in which boxes. Each atomic (?) list represents a single box
        # where the order is (Big, Med, Small)
        self.raw_state =  [[[0, 0, 0] for i in range(3)] for i in range(3)]

        # last move and last player are to make checking the win condition easy
        # last_move has the coords of the last move played
        self.last_move = None

        # last_player has the number of the player who played the last move
        self.last_player = None
        
        # coords defines board_state[0][0] as the top left and [2][2] as bottom right
        self.coords = [(left * 200 + OFFSET[0], top * 200 + OFFSET[1]) for left in range(3) for top in range(3)]
        
        # setting the coordinates of each box and initializing each rectangle
        count = 0  # internal count
        for i in range(3):
            print('Initializing row {}'.format(i))
            for j in range(3):
                box = self.board_state[i][j]
                box.coord = (i, j)
                box.init_rect(self.coords[count][0],self.coords[count][1])
                count += 1

    def update(self, player, size, color, location):
        # for now, lets say player is simply a number (1-4), size is a string
        # (big, med, small), and location is a tuple (x, y)
        
        # update the raw state
        self.raw_state[location[0]][location[1]] = player
        
        # now update the board state
        self.board_state[location[0]][location[1]].add_piece(size, color)
       

    def check_if_win(self):
        # returns True if last_player won, False otherwise
        pass
               
    
    def draw_board(self, surface):
        for row in self.board_state:
            for box in row:
                box.draw_box(surface)

    def get_board(self):
        return self.raw_state

    def _print_board(self):
        ''' helper function to print out raw board state '''
        for i in range(3):
            for j in range(3):
                print("Row: %d, Col: %d, player: %d" % (i, j, self.raw_state[i][j]))
