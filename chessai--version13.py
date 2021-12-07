# chessai--version3.py
# description: Chess...

import tkinter as tk
from PIL import ImageTk, Image
import os
import pdb  # use pdb.set_trace() if you want to "step into" the code while it is running to do debugging


IMAGEROOT = ['Pieces']  # directory for images
LIGHT = '#FFFFFF'
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
PREVIOUS_PIECE = []
DEBUG = True  # set to True to print stuff for debugging code
LAST_POSITION = []
COUNTER = [1]


def main(): 
    # Setup the GUI
    gui, canvas = setup()

    # Draw squares on board
    drawboard(canvas)

    # Add button
    btn_0  = tk.Button(gui, text = "Chess 2", command = chess_2)
    btn_0.pack(side = 'top')
    
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
    canvas.bind("<ButtonRelease-1>", lambda event: put_down_pc(event, STATE_OF_BOARD, PREVIOUS_PIECE, LAST_POSITION, canvas, img_obj_dict))
    #gui.bind("<ButtonRelease-1>", update_board(canvas, STATE_OF_BOARD, img_obj_dict))
    # canvas.after(500, update_board(canvas, STATE_OF_BOARD, img_obj_dict)) #(canvas, STATE_OF_BOARD, img_obj_dict))
    #canvas.update()

    # Run the main loop
    gui.mainloop() 


def setup():
    '''Create the tkinter gui and canvas for drawing stuff.'''
    gui = tk.Tk()
    gui.geometry("{}x{}".format(WIDTH, HEIGHT))
    gui.title("Chess")
    canvas = tk.Canvas(gui, width=WIDTH, height=HEIGHT)
    canvas.pack()

    return gui, canvas


def drawboard(canvas):
    '''Draw the squares on the tkinter canvas.'''
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
        if (abs(start_x - end_x) == 1) and start_y == end_y:
            return True 
        elif (abs(start_y - end_y) == 1) and start_x == end_x:
            return True 
        elif abs(start_x - end_x) == abs(start_y - end_y) and abs(start_x - end_x) == 1 and abs(start_y - end_y) == 1:
            return True 
        else:
            return False 


def pick_up_pc(event, state, prev_piece, last_pos):
        x = int(event.x)
        y = int(event.y)
        x_cord = x // 100
        y_cord = y // 100
        last_pos.append([x_cord, y_cord])
        piece = state[y_cord][x_cord]
        prev_piece.append(piece)
        row = state.pop(y // 100)
        row.pop(x // 100)
        row.insert(x //100, 0)
        state.insert(y // 100, row)        
        if DEBUG:
            showboard(state)
            print(1)
            print(x_cord, y_cord)
            print(prev_piece)
            print(last_pos)
            print(PIECE_DICT[piece])


def put_down_pc(event, state, prev_piece, last_pos, canvas, img_obj_dict):
    '''Describe this.'''
    # pdb.set_trace()
    if DEBUG: print(2)
    #pdb.set_trace()
    x = int(event.x)
    y = int(event.y)
    x_cord = x //100
    y_cord = y //100
    piece = prev_piece[-1]
    check = rules(piece, last_pos[-1][0], last_pos[-1][1], x_cord, y_cord )
    if check == True:
        row = state.pop(y //100)
        row.pop(x //100)
        row.insert(x // 100, piece)
        state.insert(y // 100, row)
        #update_board(canvas, STATE_OF_BOARD, img_obj_dict)
    else:
        row = state.pop(last_pos[-1][1])
        row.pop(last_pos[-1][0])
        row.insert(last_pos[-1][0], piece)
        state.insert(last_pos[-1][1], row)
    
    update_board(canvas, state, img_obj_dict)

    if DEBUG:
        showboard(state)
        print(2)
        print(PIECE_DICT[piece])
        print(x_cord, y_cord)
        print(check)
    

def update_board(canvas, state_of_board, img_obj_dict):
    print(" --",COUNTER, "-- ") # check for the nth iteration 
    for row in range(len(state_of_board)):
        for col in range(len(state_of_board[row])):
            whichpiece = PIECE_DICT[state_of_board[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                draw(canvas, img_obj_dict[whichpiece] , row, col) 
            #   draw(canvas, imgObj_creator(whichpiece) , row, col)
    x = COUNTER.pop(0)
    COUNTER.append(x + 1)
    #canvas.bind("<ButtonRelease-1>", update_board(canvas, STATE_OF_BOARD, img_obj_dict))
    #canvas.after(500, update_board(canvas, STATE_OF_BOARD, img_obj_dict))
    

    

def process_board():
    pass

def showboard(board):
    '''Helper function to display the current state of the board.'''
    print('=' * 24)
    for row in board:
        for col in row:
            print("{0:>2}".format(col), end=" ")
        print()
    print('=' * 24)

def imgObj_creator(pc_name): # input is just a string
    pc = tk.PhotoImage(file=os.path.join(IMAGEROOT[-1], "{}.svg.png".format(pc_name))) 
    return pc # allows the invocation of this function to output the necessary image_object

def draw(canvas, piece, row, col): # piece in this case needs to be a photoimage 
    canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW)
    
def chess_2():
    IMAGEROOT.append("Pieces_2")

def chess_classic():
    IMAGEROOT.append("Pieces")
    




if __name__ == "__main__":
    main()
