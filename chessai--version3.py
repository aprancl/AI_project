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

def main(): 
    
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
            # draw(canvas, imgObj_creator(whichpiece) , row, col)
    
    
    if DEBUG: showboard(STATE_OF_BOARD)
    
    gui.bind("<Button>", pick_up_pc)
    gui.bind("<ButtonRelease-1>", put_down_pc)

    # Update the GUI
    gui.mainloop() 




# NOTE functions 

# TODO: Make function where input is string (e.g. "w_king") and output is tk.PhotoImage //// within or outside of the function? - within? 


def pick_up_pc(event): 
        if DEBUG: print(1)
        global STATE_OF_BOARD
        global PREVIOUS_PIECE
        x = int(event.x)
        y = int(event.y)
        output = [x, y]
        piece = STATE_OF_BOARD[y // 100][x //100]
        PREVIOUS_PIECE.append(piece)
        row = STATE_OF_BOARD.pop(y // 100)
        row.pop(x // 100)
        row.insert(x //100, 0)
        STATE_OF_BOARD.insert(y // 100, row)
        
        if DEBUG:
            print(output)
            print(PIECE_DICT[piece])
            showboard(STATE_OF_BOARD)
            print(PREVIOUS_PIECE)

def put_down_pc(event): 
        global STATE_OF_BOARD
        global PREVIOUS_PIECE
        if DEBUG: print(2)
        x = int(event.x)
        y = int(event.y)
        output = [x, y]
        piece = PREVIOUS_PIECE[-1]
        row = STATE_OF_BOARD.pop(y //100)
        row.pop(x //100)
        row.insert(x // 100, piece)
        STATE_OF_BOARD.insert(y // 100, row)
        
        if DEBUG:
            print(output)
            print(PIECE_DICT[piece])
            showboard(STATE_OF_BOARD)


def showboard(board):
    '''Helper function to display the current state of the board.'''
    print('=' * 24)
    for row in board:
        for col in row:
            print("{0:>2}".format(col), end=" ")
        print()
    print('=' * 24)

def imgObj_creator(pc_name): 
    pc = tk.PhotoImage(file=os.path.join(IMAGEROOT, "{}.svg.png".format(pc_name))) 
    return pc # allows the invocation of this function to output the necessary image_object

def draw(canvas, piece, row, col):
    canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW)


def board_construction(x, y):
    
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
    for row in range(len(x)):
        for col in range(len(x[row])):
            whichpiece = y[x[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                #draw(canvas, eval(whichpiece) , row, col) # canvas is not defined 
                #draw(canvas, imgObj_creator(whichpiece), row, col)
                pass
    


if __name__ == "__main__":
    main()