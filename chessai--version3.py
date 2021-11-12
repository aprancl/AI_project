# chessai--version3.py
# description: Chess...

import tkinter as tk
import os
from tkinter.constants import ANCHOR

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
    
    def draw(piece, row, col):
        canvas.create_image(col*100, row *100, image=piece, anchor=tk.NW)

    draw(w_king, 7, 4)
    draw(w_queen, 7, 3)
    draw(w_rook, 7, 0)
    draw(w_rook, 7, 7)
    draw(w_bishop, 7, 2)
    draw(w_bishop, 7, 6)
    draw(w_knight, 7, 1)
    draw(w_knight, 7, 5)
    draw(w_pawn, 6, 0)
    draw(w_pawn, 6, 1)
    draw(w_pawn, 6, 2)
    draw(w_pawn, 6, 3)
    draw(w_pawn, 6, 4)
    draw(w_pawn, 6, 5)
    draw(w_pawn, 6, 6)
    draw(w_pawn, 6, 7)

    draw(b_king, 0, 3)
    draw(b_queen, 0, 4)
    draw(b_rook, 0, 0)
    draw(b_rook, 0, 7)
    draw(b_bishop, 0, 2)
    draw(b_bishop, 0, 5)
    draw(b_knight, 0, 1)
    draw(b_knight, 0, 6)
    draw(b_pawn, 1, 0)
    draw(b_pawn, 1, 1)
    draw(b_pawn, 1, 2)
    draw(b_pawn, 1, 3)
    draw(b_pawn, 1, 4)
    draw(b_pawn, 1, 5)
    draw(b_pawn, 1, 6)
    draw(b_pawn, 1, 7)

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


# old code 
    # The chess board itself
    #squares(57-64)

    # square_57 = tk.Button(gui, command = sqr_val_57, padx = 40, pady = 40, text = "57", highlightbackground = "#196F3D" )
    # square_57.grid(row = 0, column = 0)
    # square_58 = tk.Button(gui, command = sqr_val_58, padx = 40, pady = 40, text = "58", highlightbackground = "white" )
    # square_58.grid(row = 0, column = 1)
    # square_59 = tk.Button(gui, command = sqr_val_59, padx = 40, pady = 40, text = "59", highlightbackground = "#196F3D" )
    # square_59.grid(row = 0, column = 2)
    # square_60 = tk.Button(gui, command = sqr_val_60, padx = 40, pady = 40, text = "60", highlightbackground = "white" )
    # square_60.grid(row = 0, column = 3)
    # square_61 = tk.Button(gui, command = sqr_val_61, padx = 40, pady = 40, text = "61", highlightbackground = "#196F3D" )
    # square_61.grid(row = 0, column = 4)
    # square_62 = tk.Button(gui, command = sqr_val_62, padx = 40, pady = 40, text = "62", highlightbackground = "white" )
    # square_62.grid(row = 0, column = 5)
    # square_63 = tk.Button(gui, command = sqr_val_63, padx = 40, pady = 40, text = "63", highlightbackground = "#196F3D" )
    # square_63.grid(row = 0, column = 6)
    # square_64 = tk.Button(gui, command = sqr_val_64, padx = 40, pady = 40, text = "64", highlightbackground = "white" )
    # square_64.grid(row = 0, column = 7)

    # #squares (49-56)
    # square_49 = tk.Button(gui, command = sqr_val_49, padx = 40, pady = 40, text = "49", highlightbackground = "white" )
    # square_49.grid(row = 1, column = 0)
    # square_50 = tk.Button(gui, command = sqr_val_50, padx = 40, pady = 40, text = "50", highlightbackground = "#196F3D" )
    # square_50.grid(row = 1, column = 1)
    # square_51 = tk.Button(gui, command = sqr_val_51, padx = 40, pady = 40, text = "51", highlightbackground = "white" )
    # square_51.grid(row = 1, column = 2)
    # square_52 = tk.Button(gui, command = sqr_val_52, padx = 40, pady = 40, text = "52", highlightbackground = "#196F3D" )
    # square_52.grid(row = 1, column = 3)
    # square_53 = tk.Button(gui, command = sqr_val_53, padx = 40, pady = 40, text = "53", highlightbackground = "white" )
    # square_53.grid(row = 1, column = 4)
    # square_54 = tk.Button(gui, command = sqr_val_54, padx = 40, pady = 40, text = "54", highlightbackground = "#196F3D" )
    # square_54.grid(row = 1, column = 5)
    # square_55 = tk.Button(gui, command = sqr_val_55, padx = 40, pady = 40, text = "55", highlightbackground = "white" )
    # square_55.grid(row = 1, column = 6)
    # square_56 = tk.Button(gui, command = sqr_val_56, padx = 40, pady = 40, text = "56", highlightbackground = "#196F3D" )
    # square_56.grid(row = 1, column = 7)

    # #squares (41-48)
    # square_41 = tk.Button(gui, command = sqr_val_41, padx = 40, pady = 40, text = "41", highlightbackground = "#196F3D" )
    # square_41.grid(row = 2, column = 0)
    # square_42 = tk.Button(gui, command = sqr_val_42, padx = 40, pady = 40, text = "42", highlightbackground = "white" )
    # square_42.grid(row = 2, column = 1)
    # square_43 = tk.Button(gui, command = sqr_val_43, padx = 40, pady = 40, text = "43", highlightbackground = "#196F3D" )
    # square_43.grid(row = 2, column = 2)
    # square_44 = tk.Button(gui, command = sqr_val_44, padx = 40, pady = 40, text = "44", highlightbackground = "white" )
    # square_44.grid(row = 2, column = 3)
    # square_45 = tk.Button(gui, command = sqr_val_45, padx = 40, pady = 40, text = "45", highlightbackground = "#196F3D" )
    # square_45.grid(row = 2, column = 4)
    # square_46 = tk.Button(gui, command = sqr_val_46, padx = 40, pady = 40, text = "46", highlightbackground = "white" )
    # square_46.grid(row = 2, column = 5)
    # square_47 = tk.Button(gui, command = sqr_val_47, padx = 40, pady = 40, text = "47", highlightbackground = "#196F3D" )
    # square_47.grid(row = 2, column = 6)
    # square_48 = tk.Button(gui, command = sqr_val_48, padx = 40, pady = 40, text = "48", highlightbackground = "white" )
    # square_48.grid(row = 2, column = 7)

    # #squares (33-40)
    # square_33 = tk.Button(gui, command = sqr_val_33, padx = 40, pady = 40, text = "33", highlightbackground = "white" )
    # square_33.grid(row = 3, column = 0)
    # square_34 = tk.Button(gui, command = sqr_val_34, padx = 40, pady = 40, text = "34", highlightbackground = "#196F3D" )
    # square_34.grid(row = 3, column = 1)
    # square_35 = tk.Button(gui, command = sqr_val_35, padx = 40, pady = 40, text = "35", highlightbackground = "white" )
    # square_35.grid(row = 3, column = 2)
    # square_36 = tk.Button(gui, command = sqr_val_36, padx = 40, pady = 40, text = "36", highlightbackground = "#196F3D" )
    # square_36.grid(row = 3, column = 3)
    # square_37 = tk.Button(gui, command = sqr_val_37, padx = 40, pady = 40, text = "37", highlightbackground = "white" )
    # square_37.grid(row = 3, column = 4)
    # square_38 = tk.Button(gui, command = sqr_val_38, padx = 40, pady = 40, text = "38", highlightbackground = "#196F3D" )
    # square_38.grid(row = 3, column = 5)
    # square_39 = tk.Button(gui, command = sqr_val_39, padx = 40, pady = 40, text = "39", highlightbackground = "white" )
    # square_39.grid(row = 3, column = 6)
    # square_40 = tk.Button(gui, command = sqr_val_40, padx = 40, pady = 40, text = "40", highlightbackground = "#196F3D" )
    # square_40.grid(row = 3, column = 7)

    # #squares (25-32)
    # square_25 = tk.Button(gui, command = sqr_val_25, padx = 40, pady = 40, text = "25", highlightbackground = "#196F3D" )
    # square_25.grid(row = 4, column = 0)
    # square_26 = tk.Button(gui, command = sqr_val_26, padx = 40, pady = 40, text = "26", highlightbackground = "white" )
    # square_26.grid(row = 4, column = 1)
    # square_27 = tk.Button(gui, command = sqr_val_27, padx = 40, pady = 40, text = "27", highlightbackground = "#196F3D" )
    # square_27.grid(row = 4, column = 2)
    # square_28 = tk.Button(gui, command = sqr_val_28, padx = 40, pady = 40, text = "28", highlightbackground = "white" )
    # square_28.grid(row = 4, column = 3)
    # square_29 = tk.Button(gui, command = sqr_val_29, padx = 40, pady = 40, text = "29", highlightbackground = "#196F3D" )
    # square_29.grid(row = 4, column = 4)
    # square_30 = tk.Button(gui, command = sqr_val_30, padx = 40, pady = 40, text = "30", highlightbackground = "white" )
    # square_30.grid(row = 4, column = 5)
    # square_31 = tk.Button(gui, command = sqr_val_31, padx = 40, pady = 40, text = "31", highlightbackground = "#196F3D" )
    # square_31.grid(row = 4, column = 6)
    # square_32 = tk.Button(gui, command = sqr_val_32, padx = 40, pady = 40, text = "32", highlightbackground = "white" )
    # square_32.grid(row = 4, column = 7)

    # #squares (17-24)
    # square_17 = tk.Button(gui, command = sqr_val_17, padx = 40, pady = 40, text = "17", highlightbackground = "white" )
    # square_17.grid(row = 5, column = 0)
    # square_18 = tk.Button(gui, command = sqr_val_18, padx = 40, pady = 40, text = "18", highlightbackground = "#196F3D" )
    # square_18.grid(row = 5, column = 1)
    # square_19 = tk.Button(gui, command = sqr_val_19, padx = 40, pady = 40, text = "19", highlightbackground = "white" )
    # square_19.grid(row = 5, column = 2)
    # square_20 = tk.Button(gui, command = sqr_val_20, padx = 40, pady = 40, text = "20", highlightbackground = "#196F3D" )
    # square_20.grid(row = 5, column = 3)
    # square_21 = tk.Button(gui, command = sqr_val_21, padx = 40, pady = 40, text = "21", highlightbackground = "white" )
    # square_21.grid(row = 5, column = 4)
    # square_22 = tk.Button(gui, command = sqr_val_22, padx = 40, pady = 40, text = "22", highlightbackground = "#196F3D" )
    # square_22.grid(row = 5, column = 5)
    # square_23 = tk.Button(gui, command = sqr_val_23, padx = 40, pady = 40, text = "23", highlightbackground = "white" )
    # square_23.grid(row = 5, column = 6)
    # square_24 = tk.Button(gui, command = sqr_val_24, padx = 40, pady = 40, text = "24", highlightbackground = "#196F3D" )
    # square_24.grid(row = 5, column = 7)

    # #squares (9-16)
    # square_9 = tk.Button(gui, command = sqr_val_9, padx = 40, pady = 40, text = "09", highlightbackground = "#196F3D" )
    # square_9.grid(row = 6, column = 0)
    # square_10 = tk.Button(gui, command = sqr_val_10, padx = 40, pady = 40, text = "10", highlightbackground = "white" )
    # square_10.grid(row = 6, column = 1)
    # square_11 = tk.Button(gui, command = sqr_val_11, padx = 40, pady = 40, text = "11", highlightbackground = "#196F3D" )
    # square_11.grid(row = 6, column = 2)
    # square_12 = tk.Button(gui, command = sqr_val_12, padx = 40, pady = 40, text = "12", highlightbackground = "white" )
    # square_12.grid(row = 6, column = 3)
    # square_13 = tk.Button(gui, command = sqr_val_13, padx = 40, pady = 40, text = "13", highlightbackground = "#196F3D" )
    # square_13.grid(row = 6, column = 4)
    # square_14 = tk.Button(gui, command = sqr_val_14, padx = 40, pady = 40, text = "14", highlightbackground = "white" )
    # square_14.grid(row = 6, column = 5)
    # square_15 = tk.Button(gui, command = sqr_val_15, padx = 40, pady = 40, text = "15", highlightbackground = "#196F3D" )
    # square_15.grid(row = 6, column = 6)
    # square_16 = tk.Button(gui, command = sqr_val_16, padx = 40, pady = 40, text = "16", highlightbackground = "white" )
    # square_16.grid(row = 6, column = 7)

    # #squares (1-8)
    # square_1 = tk.Button(gui, command = sqr_val_1, padx = 40, pady = 40, text = "01", highlightbackground = "white" )
    # square_1.grid(row = 7, column = 0)
    # square_2 = tk.Button(gui, command = sqr_val_2, padx = 40, pady = 40, text = "02", highlightbackground = "#196F3D" )
    # square_2.grid(row = 7, column = 1)
    # square_3 = tk.Button(gui, command = sqr_val_3, padx = 40, pady = 40, text = "03", highlightbackground = "white" )
    # square_3.grid(row = 7, column = 2)
    # square_4 = tk.Button(gui, command = sqr_val_4, padx = 40, pady = 40, text = "04", highlightbackground = "#196F3D" )
    # square_4.grid(row = 7, column = 3)
    # square_5 = tk.Button(gui, command = sqr_val_5, padx = 40, pady = 40, text = "05", highlightbackground = "white" )
    # square_5.grid(row = 7, column = 4)
    # square_6 = tk.Button(gui, command = sqr_val_6, padx = 40, pady = 40, text = "06", highlightbackground = "#196F3D" )
    # square_6.grid(row = 7, column = 5)
    # square_7 = tk.Button(gui, command = sqr_val_7, padx = 40, pady = 40, text = "07", highlightbackground = "white" )
    # square_7.grid(row = 7, column = 6)
    # square_8 = tk.Button(gui, command = sqr_val_8, padx = 40, pady = 40, text = "08",   highlightbackground = "#196F3D" )
    # square_8.grid(row = 7, column = 7)

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