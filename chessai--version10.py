# chessai--version3.py
# description: Chess...

import tkinter as tk
from PIL import ImageTk, Image
import os
import pdb  # use pdb.set_trace() if you want to "step into" the code while it is running to do debugging

IMAGEROOT = 'Pieces'  # directory for images
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
    print(" --",COUNTER, "-- ")
    gui = tk.Tk()
    gui.geometry("{}x{}".format(WIDTH, HEIGHT))
    gui.title("Chess")
    canvas = tk.Canvas(gui, width=WIDTH, height=HEIGHT)
    canvas.pack()

    # Draw squares on board
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
       
    w_king = tk.PhotoImage(file=os.path.join(IMAGEROOT, "w_king.svg.png"))
    w_queen = tk.PhotoImage(file=os.path.join(IMAGEROOT, "w_queen.svg.png"))
    w_rook = tk.PhotoImage(file=os.path.join(IMAGEROOT, "w_rook.svg.png"))
    w_bishop = tk.PhotoImage(file=os.path.join(IMAGEROOT, "w_bishop.svg.png"))
    w_knight = tk.PhotoImage(file=os.path.join(IMAGEROOT, "w_knight.svg.png"))
    w_pawn = tk.PhotoImage(file=os.path.join(IMAGEROOT, "w_pawn.svg.png"))
    b_king = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_king.svg.png"))
    b_queen = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_queen.svg.png"))
    b_rook = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_rook.svg.png"))
    b_bishop = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_bishop.svg.png"))
    b_knight = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_knight.svg.png"))
    b_pawn = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_pawn.svg.png"))

    for row in range(len(STATE_OF_BOARD)):
        for col in range(len(STATE_OF_BOARD[row])):
            whichpiece = PIECE_DICT[STATE_OF_BOARD[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                draw(canvas, eval(whichpiece) , row, col) 
            #   draw(canvas, imgObj_creator(whichpiece) , row, col)
    
    if DEBUG: showboard(STATE_OF_BOARD)
    
    gui.bind("<Button>", pick_up_pc)
    gui.bind("<ButtonRelease-1>", put_down_pc)

    x = COUNTER.pop(0)
    COUNTER.append(x + 1)

    # Update the GUI
    gui.mainloop() 

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
        if abs(start_x - end_x) == abs(start_y - end_y):
            return True 
        else:
            return False 
    
    #rook
    elif abs(pc_name) == 3:
        if start_x == end_x or start_y == end_y:
            return True 
        else:
            return False 
    
    #Queen 
    elif abs(pc_name) == 2:
        if start_x == end_x or start_y == end_y:
            return True 
        elif abs(start_x - end_x) == abs(start_y - end_y):
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



            
def pick_up_pc(event): 

        global STATE_OF_BOARD
        global PREVIOUS_PIECE
        global LAST_POSITION
        x = int(event.x)
        y = int(event.y)
        x_cord = x // 100
        y_cord = y // 100
        LAST_POSITION.append([x_cord, y_cord])
        piece = STATE_OF_BOARD[y_cord][x_cord]
        PREVIOUS_PIECE.append(piece)
        row = STATE_OF_BOARD.pop(y // 100)
        row.pop(x // 100)
        row.insert(x //100, 0)
        STATE_OF_BOARD.insert(y // 100, row)
        
        if DEBUG:
            
            showboard(STATE_OF_BOARD)
            print(1)
            print(x_cord, y_cord)
            print(PREVIOUS_PIECE)
            print(LAST_POSITION)
            print(PIECE_DICT[piece])


def put_down_pc(event): 
        global STATE_OF_BOARD
        global PREVIOUS_PIECE
        global LAST_POSITION
        if DEBUG: print(2)
        x = int(event.x)
        y = int(event.y)
        x_cord = x //100
        y_cord = y //100
        piece = PREVIOUS_PIECE[-1]
        check = rules(piece, LAST_POSITION[-1][0], LAST_POSITION[-1][1], x_cord, y_cord )
        row = STATE_OF_BOARD.pop(y //100)
        row.pop(x //100)
        row.insert(x // 100, piece)
        STATE_OF_BOARD.insert(y // 100, row)
        
        if DEBUG:

            showboard(STATE_OF_BOARD)
            print(2)
            print(PIECE_DICT[piece])
            print(x_cord, y_cord)
            print(check)


def showboard(board):
    '''Helper function to display the current state of the board.'''
    print('=' * 24)
    for row in board:
        for col in row:
            print("{0:>2}".format(col), end=" ")
        print()
    print('=' * 24)

def imgObj_creator(pc_name): # input is just a string
    pc = tk.PhotoImage(file=os.path.join(IMAGEROOT, "{}.svg.png".format(pc_name))) 
    return pc # allows the invocation of this function to output the necessary image_object

def draw(canvas, piece, row, col): # piece in this case needs to be a photoimage 
    canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW)



if __name__ == "__main__":
    main()