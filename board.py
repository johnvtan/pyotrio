import pygame

OFFSET = (300, 50)

class Sizes:
    BIG, MED, SMALL = range(3)

class Box():
    ''' Contains all relevant info for each box in board grid '''
    def __init__(self):

        # the Box should have some coordinate on the board, where (0,0) is the bottom left box
        # and (2,2) is the top-right box
        self.coord = (None, None)
        
        # tracking states of pieces in the grid
        # also need to track/ colors
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
        ''' initializes bounding box and center point of the square '''
        self.rect = pygame.Rect(left, top, self.side_length, self.side_length)
        #self.area = (left, top, self.side_length, self.side_length)
        self.center = (int(left + self.side_length / 2), int(top + self.side_length / 2))

    def add_piece(self, size, color):
        ''' adds a piece to the box (big, medium, small) '''
        if size == Sizes.BIG:
            self.big = True
            self.big_color = color
        elif size == Sizes.MED:
            self.med = True
            self.med_color = color
        elif size == Sizes.SMALL:
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
    def __init__(self, num_players):
        
        self.num_players = num_players

        # defines board_state as 3x3 array of Box() objects
        # note that board_state is entirely for visual purposes
        self.board_state =[[Box(), Box(), Box()], [Box(), Box(), Box()], [Box(), Box(), Box()]]
        
        # raw_state keeps track of which player played which piece
        # each innermost array represents a single box, where the convention is
        # [Big, Med, Small]. This will be used for AI players 
        self.raw_state =  [[[0, 0, 0] for i in range(3)] for i in range(3)]

        # the board can essentially be cut into 9 3x3 grids. On each 3x3 grid,
        # a player has 8 ways to win (3 rows, 3 columns, 2 diagonals)
        # We have to append a list of length 4 to keep track of the 4 possible
        # "double diagonals", ie 3 in a row that changes in 2 dimensions each 
        # move, which isn't accounted for by the other 72 conditions. The scores 
        # array will track the number of pieces in each possible winning line
        # for each player. Once any value in the scores array reaches 3, a 
        # winner has been determined.
        # By convention, for each player, indices 0-2 refer to the dimension
        # determined by the piece size, 4-6 refer to the row, and 7-9 refer to
        # the column
        self.scores = [[[0 for i in range(8)] for j in range(9)] + [[0 for k in range(4)]] for n in range(num_players)]
        
        # coords defines board_state[0][0] as the top left and [2][2] as bottom right
        self.coords = [(left * 200 + OFFSET[0], top * 200 + OFFSET[1]) for left in range(3) for top in range(3)]
        
        # setting the coordinates of each box and initializing each rectangle
        count = 0  
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
        dimensions = (size, location[0], location[1])

        # update raw state
        self.raw_state[dimensions[0]][dimensions[1]][dimensions[2]] = player
        
        player -= 1
        
        # we update the scores array 
        # the following loop should take care of updating the non-double-diagonal
        # lines        
        for (dim0, offset) in zip(dimensions, [0, 3, 6]):           
            # first thing is to retrieve the other 2 dimensions
            count = 0
            checked = False
            for d in dimensions:
                if d == dim0 and not checked:
                    checked = True
                    continue
                if count == 0:
                    dim1 = d
                if count == 1:
                    dim2 = d
                count += 1
            
            #print(self.scores[player][dim1])
            # now update row and column score
            self.scores[player][dim0+offset][dim1] += 1
            self.scores[player][dim0+offset][dim2+3] += 1

            # now check and update if piece lies on one of the diagonals on
            # this square
            if (dim1 == dim2): 
                self.scores[player][dim0+offset][6] += 1
            elif (2 - dim1 == dim2):
                self.scores[player][dim0+offset][7] += 1

        # after the loop, we now have to update the double diagonal conditions
        # as well
        # if the piece is played at (1,1,1), then it counts as part of all 
        # double diagonals
        if (size == location[0] == location[1] == 1):
            self.scores[player][9] = [x + 1 for x in self.scores[player][9]]
        else:
            if (dimensions == (0, 0, 0) or dimensions == (2, 2, 2)):
                self.scores[player][9][0] += 1
            elif (dimensions == (0, 0, 2) or dimensions == (2, 2, 0)):
                self.scores[player][9][1] += 1
            elif (dimensions == (0, 2, 0) or dimensions == (2, 0, 2)):
                self.scores[player][9][2] += 1
            elif (dimensions == (0, 2, 2) or dimensions == (2, 0, 0)):
                self.scores[player][9][3] += 1
        
        # now update the board state
        self.board_state[location[0]][location[1]].add_piece(size, color)

    def check_if_win(self):
        # returns True and player number if win, False and -1  otherwise
        # since we're keeping track of the scores in update, all we have to do
        # here is check if any of the scores arrays contains a 3
        for i in range(self.num_players):
            for j in range(10): 
                if 3 in self.scores[i][j]:
                    return True, i+1
        return False, -1 
    
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
                for k in range(3):
                    print("Size: %d, Row: %d, Col: %d, player: %d" % (i, j, k, self.raw_state[i][j][k]))
