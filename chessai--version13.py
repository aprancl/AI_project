# chessai--version13.py
# description: This program displays a chessboard, and allows the user 
#              to play against another player nearby, or to play against the computer.

import tkinter as tk
import random
from PIL import ImageTk, Image
import os
import pdb  

IMAGEROOT = ['Pieces']  # directory for images
LIGHT = '#FFFFFF' # for squares
DARK = '#196F3D'
WIDTH = 800  # in pixels
HEIGHT = 800  # in pixels
NUMSQUARES = 8  # number of squares on chessboard
STATE_OF_BOARD = [
    [-3,-5,-4,-1,-2,-4,-5,-3],
    [-6,-6,-6,-6,-6,-6,-6,-6],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 6, 6, 6, 6, 6, 6, 6, 6],
    [ 3, 5, 4, 2, 1, 4, 5, 3]]
PIECE_DICT = { 0:'none', 1:'w_king', 2:'w_queen', 3:'w_rook', 4:'w_bishop', 5:'w_knight', 6:'w_pawn', 
                     -1:'b_king',-2:'b_queen', -3:'b_rook', -4:'b_bishop', -5:'b_knight', -6:'b_pawn'}
# variables necessary for moving pieces
PREVIOUS_PIECE = []
DEBUG = True  # set to True to print stuff for debugging code
LAST_POSITION = []
COUNTER = [1]
AI_LAST_POSITION = []
AI_LAST_PC = []

def main(): 
    # Setup the GUI
    gui, canvas = setup()

    # Draw squares on board
    drawboard(canvas)

    # tailor user experience through user input 
        # play alone or with ai?
    single_player = input("Would you like to play against the computer?: ").lower()
    while single_player[0] != 'y' and single_player[0] != 'n':
        print("you must answer (yes) or (no)")
        single_player = input("Would you like to play against the computer?: ").lower()
    if single_player[0] == 'y':
        single_player = True
    else:
        single_player = False

        # play normal chess or chess 2?
    normal = input("Would you like to play normal chess?: ")
    while normal[0] != 'y' and normal[0] != 'n':
        print("you must answer (yes) or (no)")
        normal = input("Would you like to play normal chess?: ")
    if normal[0] == 'n':
        IMAGEROOT.append('Pieces_2')
    else:
        pass

    # Draw pieces
    pc_names = ['w_king', 'w_queen', 'w_rook', 'w_bishop', 'w_knight', 'w_pawn', 
                'b_king', 'b_queen', 'b_rook', 'b_bishop', 'b_knight', 'b_pawn']
    img_obj_list = []
    for i in pc_names:
        img_obj = tk.PhotoImage(file=os.path.join(IMAGEROOT[-1], "{}.svg.png".format(i)))
        img_obj_list.append(img_obj)

    w_king = img_obj_list[0]
    w_queen = img_obj_list[1]
    w_rook = img_obj_list[2]
    w_bishop = img_obj_list[3]
    w_knight = img_obj_list[4]
    w_pawn = img_obj_list[5]
    b_king = img_obj_list[6]
    b_queen = img_obj_list[7]
    b_rook = img_obj_list[8]
    b_bishop = img_obj_list[9]
    b_knight = img_obj_list[10]
    b_pawn = img_obj_list[11]
    img_obj_dict = {'w_king': w_king, 'w_queen': w_queen, 'w_rook': w_rook, 'w_bishop': w_bishop, 'w_knight': w_knight, 'w_pawn': w_pawn, 
                    'b_king': b_king, 'b_queen': b_queen, 'b_rook': b_rook, 'b_bishop': b_bishop, 'b_knight': b_knight, 'b_pawn': b_pawn }
    
    update_board(canvas, STATE_OF_BOARD, img_obj_dict)

    if DEBUG: showboard(STATE_OF_BOARD)

    # Add event functions
    canvas.bind("<Button>", lambda event: pick_up_pc(event, STATE_OF_BOARD, PREVIOUS_PIECE, LAST_POSITION))
    canvas.bind("<ButtonRelease-1>", lambda event: put_down_pc(event, STATE_OF_BOARD, PREVIOUS_PIECE, LAST_POSITION, canvas, img_obj_dict, single_player))

    # Run the main loop
    gui.mainloop() 

def setup():
    '''Create the tkinter gui and canvas to draw the board and pieces in.'''
    gui = tk.Tk()
    gui.geometry("{}x{}".format(WIDTH, HEIGHT))
    gui.title("Chess")
    canvas = tk.Canvas(gui, width=WIDTH, height=HEIGHT)
    canvas.pack()
    return gui, canvas

def drawboard(canvas):
    '''Draw squares on the tkinter canvas.'''
    wid = WIDTH / NUMSQUARES  # width of each square, in pixels
    hei = HEIGHT / NUMSQUARES  # height of each square, in pixels
    
    for row in range(NUMSQUARES):
        if row % 2 == 0:
            for col in range(NUMSQUARES):
                if col % 2 == 0:
                    clr = LIGHT
                else:
                    clr = DARK
                x0, y0 = col * wid, row * hei  # coordinates of top-left corner of square
                x1, y1 = (col + 1) * wid, (row + 1) * hei  # coordinates of bottom-right corner of square
                canvas.create_rectangle(x0, y0, x1, y1, fill=clr, outline=clr)

        if row % 2 == 1:
            for col in range(NUMSQUARES):
                if col % 2 == 0:
                    clr = DARK
                else:
                    clr = LIGHT

                x0, y0 = col * wid, row * hei  # coordinates of top-left corner of square
                x1, y1 = (col + 1) * wid, (row + 1) * hei  # coordinates of bottom-right corner of square
                canvas.create_rectangle(x0, y0, x1, y1, fill=clr, outline=clr)

def rules(pc_name, start_x, start_y, end_x, end_y): # (integer input, index, index) 
    '''Determines whether a move is legal or not'''
    #white pawn
    if pc_name == 6:
    
        if start_y < end_y: # stops white pawns from moving backwards 
            return False
        elif start_y == 6:
            if start_y - end_y <= 2 and end_x == start_x: # allows pawn to move once or twice on first move 
                return True 
            else:
                return False
        else:
            if start_y - end_y <= 1 and end_x == start_x: # forces pawn to only move once if it has moved before 
                return True
            else:
                return False
    
    #black pawn
    elif pc_name == -6:
    
        if start_y > end_y: # stops black pawns from moving backwards 
            return False

        elif start_y == 1:
            if abs(start_y - end_y) <= 2 and end_x == start_x: # allows pawn to move once or twice on first move 
                return True 
            else:
                return False
        else:
            if abs(start_y - end_y) <= 1 and end_x == start_x: # forces pawn to only move once if it has moved before 
                return True
            else:
                return False

    #knight 
    elif abs(pc_name) == 5:
        if abs(start_y - end_y) == 2 and abs(start_x - end_x) == 1: # permits the knight to move 2 spaces vertivally and 1 horizontally
            return True
        elif abs (start_y - end_y) == 1 and abs(start_x - end_x) == 2: # permits the knight to move 1 space vertically and 2 horizontally 
            return True
        else:
            return False
    
    #bishop 
    elif abs(pc_name) == 4:
        if abs(start_x - end_x) == abs(start_y - end_y): # any movement diagonally is allowed 
            return True 
        else:
            return False 
    
    #rook
    elif abs(pc_name) == 3:
        if start_x == end_x or start_y == end_y: # any vertical movement is allowed 
            return True 
        else:
            return False 
    
    #Queen 
    elif abs(pc_name) == 2: # like a rook/bishop combo 
        if start_x == end_x or start_y == end_y: # any vertical movement is allowed 
            return True 
        elif abs(start_x - end_x) == abs(start_y - end_y): # any movement diagonally is allowed 
            return True 
        else:
            return False 
    
    #King 
    elif abs(pc_name) == 1:
        if (abs(start_x - end_x) == 1) and start_y == end_y: # allows the king to move up once on the verticle axis
            return True 
        elif (abs(start_y - end_y) == 1) and start_x == end_x: # allows the king to move up once on the horizontal axis
            return True 
        elif abs(start_x - end_x) == abs(start_y - end_y) and abs(start_x - end_x) == 1 and abs(start_y - end_y) == 1: #allows for diagonl movements, one square per move
            return True 
        else:
            return False 

def pick_up_pc(event, state, prev_piece, last_pos):
        '''Deletes a piece that is clicked on, and saves it until it is placed '''

        # locate the clicked square on the board, and document it for later use
        x = int(event.x)
        y = int(event.y)
        x_cord = x // 100
        y_cord = y // 100
        last_pos.append([x_cord, y_cord])

        #find out what piece is on the square that was clicked, and document it 
        piece = state[y_cord][x_cord]
        prev_piece.append(piece)

        #Pick up that piece 
        row = state.pop(y // 100)
        row.pop(x // 100)
        row.insert(x //100, 0)
        state.insert(y // 100, row)  
        # display relevant information in the terminal       
        if DEBUG:
            showboard(state)
            print(1)
            print(x_cord, y_cord)
            print(prev_piece)
            print(last_pos)
            print(PIECE_DICT[piece])

def put_down_pc(event, state, prev_piece, last_pos, canvas, img_obj_dict, single_player):
    '''Places pieces down when certain conditions are met, and calls for AI move.'''
    # locate the desired square to place the piece 
    x = int(event.x)
    y = int(event.y)
    x_cord = x //100
    y_cord = y //100

    #judge whether the move is legal
    piece = prev_piece[-1]
    check = rules(piece, last_pos[-1][0], last_pos[-1][1], x_cord, y_cord )
    
    if check == True: # if so... place the piece down
        row = state.pop(y //100)
        row.pop(x //100)
        row.insert(x // 100, piece)
        state.insert(y // 100, row)
    
    else: # if not... ignore the move 
        row = state.pop(last_pos[-1][1])
        row.pop(last_pos[-1][0])
        row.insert(last_pos[-1][0], piece)
        state.insert(last_pos[-1][1], row)
    
    # call for AI move 
    if single_player == True:
        ai_move(STATE_OF_BOARD, canvas, img_obj_dict, AI_LAST_POSITION, AI_LAST_PC)
    
    if DEBUG: # display relevant information in the terminal
        showboard(state)
        print(2)
        print(PIECE_DICT[piece])
        print(x_cord, y_cord)
        print(check)
    # display changes to the board on the gui
    update_board(canvas, state, img_obj_dict)
    
def ai_move(state, canvas, img_obj_dict, ai_last_pos, ai_last_pc):
    '''AI makes a random move that is not bound by the rules of the game.'''
    #find random square within the first 3 rows and all 8 columns
    x = random.randrange(800)
    y = random.randrange(200)
    x_cord = x //100
    y_cord = y //100
    ai_last_pos.append([x_cord, y_cord])
    
    #pick up the piece
    row = state.pop(y_cord)
    pc = row.pop(x_cord)
    row.insert(x_cord, 0)
    state.insert(y_cord, row)
    ai_last_pc.append(pc)
    
    # a loop is necessary to generate random desitnation squares and to check them one by one, but this causes the program to crash after nth iterations. 

    #Find a random square
    x_new = random.randrange(800)
    y_new = random.randrange(550)
    x_cord_new = x_new //100
    y_cord_new = y_new //100
    
    # place the piece
    row = state.pop(y_cord_new)
    row.pop(x_cord_new)
    row.insert(x_cord_new, ai_last_pc[-1])
    state.insert(y_cord_new, row)
    
def update_board(canvas, state_of_board, img_obj_dict):
    '''Display changed made to the STATE_OF_BOARD list by deleting old pieces and placing new ones.'''

    print(" --",COUNTER, "-- ") # check for update_board() being called 
    for i in canvas.find_withtag('old'): #Delete all pieces with the tag 'old'
         canvas.delete(i)
    # place pieces square by square 
    for row in range(len(state_of_board)):
        for col in range(len(state_of_board[row])):
            whichpiece = PIECE_DICT[state_of_board[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                draw(canvas, img_obj_dict[whichpiece] , row, col) 
    x = COUNTER.pop(0)
    COUNTER.append(x + 1)
   
def showboard(board):
    '''Helper function to display the current state of the board.'''
    print('=' * 24)
    for row in board:
        for col in row:
            print("{0:>2}".format(col), end=" ")
        print()
    print('=' * 24)

def draw(canvas, piece, row, col): # piece in this case needs to be a photoimage 
    '''displays a PhotoImage object.'''
    canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW, tag= 'old')    
    
if __name__ == "__main__":
    main()
