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


# NOTE <-- indicates a major step in the program
# ^ will be used to make comments easier to read by distinguishing primary and subordinate comments 

# potentially move this out here to be able to reference <canvas> variable in board_construction() function
# gui = tk.Tk()
# gui.geometry("{}x{}".format(WIDTH, HEIGHT))
# gui.title("Chess")
# canvas = tk.Canvas(gui, width=WIDTH, height=HEIGHT)
# canvas.pack()

def main(): 
    # NOTE BEGIN STEP 1: Create GUI and canvas
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
        # NOTE END STEP 1: Create GUI and canvas


    # Draw pieces on board

    # i'm not sure if this needs to stay anymore 
    # img = Image.open(os.path.join(IMAGEROOT, "b_rook.svg.png")).convert('RGBA')
    # img = img.resize((int(0.75 * wid), int(0.75 * hei)))  # resize based on a percentage of the size of each square
    # b_rook = ImageTk.PhotoImage(img)
    # canvas.create_image(wid / 2, hei / 2, image=b_rook, anchor=tk.CENTER)

    
    
    # NOTE BEGIN STEP 2: Create photo image objects to referecne throughout program 
    #  list of photo image objects ///// I will likely not need this once the imgObj_creator() works 
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

    # NOTE END STEP 2: Create photo image objects to referecne throughout program 

    
    
    # NOTE BEGIN STEP 3: display previously defined photo images in relation to values in STATE_OF_BOARD [].
    for row in range(len(STATE_OF_BOARD)):
        for col in range(len(STATE_OF_BOARD[row])):
            whichpiece = PIECE_DICT[STATE_OF_BOARD[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                draw(canvas, eval(whichpiece) , row, col) 
               # draw(canvas, imgObj_creator(whichpiece) , row, col)
    # NOTE END STEP 3: display previously defined photo images in relation to values in STATE_OF_BOARD [].
    

    def pick_up_pc(event): # doesn't delete pieces exactly as intended, but it changes the position of pieces in STATE_OG_BOARD list. Regardless of accuracy, I just want to output changed to the board. 
        print(1)
        global STATE_OF_BOARD
        global COORDINATES
        x = int(event.x)
        y = int(event.y)
        output = [x, y]
        piece = STATE_OF_BOARD[y // 100][x //100]
        row = STATE_OF_BOARD[y // 100]
        row.pop(piece)
        row.insert(x //100, 0) # 0 is a 'none' piece, this should delete the piece
        STATE_OF_BOARD.insert(y // 100, row)
        print(STATE_OF_BOARD)
        print(output)
        print(PIECE_DICT[piece])

    

    def put_down_pc(event): # picked_up_pieces will be .appended() to a list and .poped() out of that list, which will be used as input for this function. 
        print(2)
        x = int(event.x)
        y = int(event.y)
        output = [x, y]
        print(output)
        piece = STATE_OF_BOARD[y // 100][x //100]
        print(PIECE_DICT[piece])


    gui.bind("<Button>", pick_up_pc)
    gui.bind("<ButtonRelease-1>", put_down_pc)


    for row in range(len(STATE_OF_BOARD)):
        for col in range(len(STATE_OF_BOARD[row])):
            whichpiece = PIECE_DICT[STATE_OF_BOARD[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                draw(canvas, eval(whichpiece) , row, col) 
               # draw(canvas, imgObj_creator(whichpiece) , row, col)

    
    
    # Update the GUI
    gui.mainloop() 






# TODO: Make function where input is string (e.g. "w_king") and output is tk.PhotoImage //// within or outside of the function? - within? 
    #  we want to, instead of just listing the image_objects, use a function to create the necesary image_object 
    # this function will likely have to be referenced when pieces are places on the board
    
def imgObj_creator(pc_name):
    pc = tk.PhotoImage(file=os.path.join(IMAGEROOT, "{}.svg.png".format(pc_name))) 
    return pc # allows the invocation of this function to output the necessary image_object

def draw(canvas, piece, row, col):
    canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW)

def move(canvas, piece, row, col, drow, dcol):
    # TODO: write this function!
    # canvas.move(piece, piece.x, piece.y)
    pass

#   Ideally, the for loop used to construct the entire board should be in a function so that the process can be called when lifting and placing pieces
def board_construction(x): # the for loop I am referencing within this function is a process I want to initiate at multiple places throughout the program
    global PIECE_DICT
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
            whichpiece = PIECE_DICT[x[row][col]] 
            # pdb.set_trace()
            if whichpiece != 'none':
                #draw(canvas, eval(whichpiece) , row, col) # canvas is not defined 
                #draw(canvas, imgObj_creator(whichpiece), row, col)
                pass
    


if __name__ == "__main__":
    main()