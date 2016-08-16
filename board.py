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
        self.big_rad = 200

        self.med = False
        self.med_color = None
        self.med_rad = 100
       
        self.small = False
        self.small_color = None
        self.small_rad = 50        

        # next two are going to be used later
        # rect is a pygame.rect object
        # center_pos is its center, for drawing circles
        self.rect_color = (0, 0, 0) 
        self.center = None

        # for use w/ draw.rect - (left, top, width, height)
        self.area = (None, None, None, None)
        # constants relevant to the box
        self.side_length = 200
        self.line_width = 2 

    def init_rect(self, left, top):
        self.area = (left, top, self.side_length, self.side_length)
        self.center = (left + self.side_length / 2, top - self.side_length / 2)

    def draw_box(self, surface):
        ''' function for drawing everything inside the box '''
        pygame.draw.rect(surface, self.rect_color, self.area, self.line_width)
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
        self.board_state =[[Box(), Box(), Box()], [Box(), Box(), Box()], [Box(), Box(), Box()]]
        
        # coords defines board_state[0][0] as the bottom left and[2][2] as top right
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

    def update_board(self, player, piece, location):
        # we need the player object (which should have the color/number??), the piece placed, and the location (ideally, in coordinates)
        pass

    def check_if_win(self):
        pass
    
    def draw_board(self, surface):
        for row in self.board_state:
            for box in row:
                box.draw_box(surface)

