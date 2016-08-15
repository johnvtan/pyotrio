import pygame

OFFSET = (300, 700)

class Box():
    ''' Contains all relevant info for each box in board grid '''
    def __init__(self):
        
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
        self.rect = None
        self.rect_color = (0, 0, 0) 
        self.center = None
        self.left = None
        self.top = None        

        # constants relevant to the box
        self.side_length = 400
        self.line_width = 2

    def init_rect(self, left, top):
        self.left = left
        self.top = top
        self.rect = pygame.Rect(left, top, self.side_length, self.side_length)
        self.center = (left + self.side_length / 2, top - self.side_length / 2)

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
        self.board_state = [[Box()] * 3] * 3]
        
        # coords defines board_state[0][0] as the bottom left and[2][2] as top right
        self.coords = [(left * 400 + OFFSET[0], top * 400 + OFFSET[1]) for left in range(3) for top in range(3)]
        
        count = 0  # internal count
        for row in board_state:
            for box in row:
                box.init_rect(coords[count][0], coords[count][1])

    def update_board_state(self):
        # how to input moves?? 
        # once we get the move here, then just set the element in Box to be True and set the color
        pass

    def check_if_win(self):
        pass
    
    def draw_board(self):
        pass

    



