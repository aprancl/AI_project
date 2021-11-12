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

def main():
    # Create GUI and canvas
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



    # Draw pieces on board
    img = Image.open(os.path.join(IMAGEROOT, "b_rook.svg.png")).convert('RGBA')
    img = img.resize((int(0.75 * wid), int(0.75 * hei)))  # resize based on a percentage of the size of each square
    b_rook = ImageTk.PhotoImage(img)
    canvas.create_image(wid / 2, hei / 2, image=b_rook, anchor=tk.CENTER)

    # TODO: Make function where input is string (e.g. "w_king") and output is tk.PhotoImage 
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

    # Piece management

    state_of_board = [
    [-3,-5,-4,-1,-2,-4,-5,-3],
    [-6,-6,-6,-6,-6,-6,-6,-6],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 6, 6, 6, 6, 6, 6, 6, 6],
    [ 3, 5, 4, 2, 1, 4, 5, 3]]

    piece_dict = { 0:'none', 1:'w_king', 2:'w_queen', 3:'w_rook', 4:'w_bishop', 5:'w_knight', 6:'w_pawn', 
                          -1:'b_king',-2:'b_queen', -3:'b_rook', -4:'b_bishop', -5:'b_knight', -6:'b_pawn'}

    for row in range(len(state_of_board)):
        for col in range(len(state_of_board[row])):
            whichpiece = piece_dict[state_of_board[row][col]]
            if whichpiece != 'none':
                draw(canvas, eval(whichpiece), row, col)

    # maybe make a loop to reconstruct the board instead of hardcoding the pieces to their locations as they are now 
#    for horizontal in state_of_board:
#        x = horizontal
#        for vertical in horizontal:
#            if vertical == 1:
#                draw(vertical, x, col )



# Taking user input 

# Tracking the mouse 

    def click(event):
        x = int(event.x)
        y = int(event.y)
        output = [x, y]
        print(output)
        piece = state_of_board[y // 100][x //100]
        print(piece_dict[piece])
        
    gui.bind("<Button>", click)
    
  
    # Update the GUI
    gui.mainloop() 


def draw(canvas, piece, row, col):
    canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW)

def move(canvas, piece, row, col, drow, dcol):
    # TODO: write this function!
    # canvas.move()
    pass

    # Function reprocessing 
            # For every move, two functions needed to be redefined: the f(x) belonging to the square that the # pos_val is being moved from,
            # and the f(x) of the square that the # pos_val is moving to.
            
            # More may technically need to be redefined in the future depending how I indicate where a # pos_val can move, but that is to be determined.


    #       One idea on how to accomlish this. not sure if works.
    # def eval("sqr_var_{}".format(some expression gathering user input)):

    #       Another idea from playing with python shell //// probably easier
    # player_input = input()     
    # def eval(player_input):







# square value assingment 
    # Pieces: king = 1, queen = 2, rook = 3, bishop = 4, knight = 5, pawn = 6 




if __name__ == "__main__":
    main()