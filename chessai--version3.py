# chessai--version3.py
# description: Chess...

import tkinter as tk
import os

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
    for row in range(1):
        for col in range(NUMSQUARES):
            if col % 2 == 0:
                clr = DARK
            else:
                clr = LIGHT

            x0, y0 = col * wid, row * hei  # coordinates of top-left corner of square
            x1, y1 = (col + 1) * wid, (row + 1) * hei  # coordinates of bottom-right corner of square
            canvas.create_rectangle(x0, y0, x1, y1, fill=clr, outline=clr)

    # Draw pieces on board
    # b_rook = tk.PhotoImage(file=os.path.join(IMAGEROOT, "b_rook.svg.png"))
    # canvas.create_image(0, 0, image=b_rook, anchor=tk.NW)

    # Update the GUI
    gui.mainloop() 


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
            # For every move, two functions needed to be redefined: the f(x) belonging to the square that the piece is being moved from,
            # and the f(x) of the square that the piece is moving to.
            
            # More may technically need to be redefined in the future depending how I indicate where a piece can move, but that is to be determined.


    #       One idea on how to accomlish this. not sure if works.
    # def eval("sqr_var_{}".format(some expression gathering user input)):

    #       Another idea from playing with python shell //// probably easier
    # player_input = input()     
    # def eval(player_input):












# square value assingment 
    # Pieces: king = 1, queen = 2, rook = 3, bishop = 4, knight = 5, pawn = 6 

def sqr_val_1():
    pos_val = 1
    piece = 3
    print(piece)

def sqr_val_2():
    pos_val = 2
    piece = 5
    print(piece)

def sqr_val_3():
    pos_val = 3
    piece = 4
    print(piece)

def sqr_val_4():
    pos_val = 4
    piece = 2
    print(piece)

def sqr_val_5():
    pos_val = 5
    piece = 1
    print(piece)

def sqr_val_6():
    pos_val = 6
    piece = 4
    print(piece)

def sqr_val_7():
    pos_val = 7
    piece = 5
    print(piece)

def sqr_val_8():
    pos_val = 8
    piece = 3
    print(piece)

def sqr_val_9():
    pos_val = 9
    piece = 6
    print(piece)

def sqr_val_10():
    pos_val = 10
    piece = 6
    print(piece)

def sqr_val_11():
    pos_val = 11
    piece = 6
    print(piece)

def sqr_val_12():
    pos_val = 12
    piece = 6
    print(piece)

def sqr_val_13():
    pos_val = 13
    piece = 6
    print(piece)

def sqr_val_14():
    pos_val = 14
    piece = 6
    print(piece)

def sqr_val_15():
    pos_val = 15
    piece = 6
    print(piece)

def sqr_val_16():
    pos_val = 16
    piece = 6
    print(piece)

def sqr_val_17():
    pos_val = 17
    piece = 0
    print(piece)

def sqr_val_18():
    pos_val = 18
    piece = 0
    print(piece)

def sqr_val_19():
    pos_val = 19
    piece = 0
    print(piece)

def sqr_val_20():
    pos_val = 20
    piece = 0
    print(piece)

def sqr_val_21():
    pos_val = 21
    piece = 0 
    print(piece)

def sqr_val_22():
    pos_val = 22
    piece = 0
    print(piece)

def sqr_val_23():
    pos_val = 23
    piece = 0
    print(piece)

def sqr_val_24():
    pos_val = 24
    piece = 0
    print(piece)

def sqr_val_25():
    pos_val = 25
    piece = 0
    print(piece)

def sqr_val_26():
    pos_val = 26
    piece = 0
    print(piece)

def sqr_val_27():
    pos_val = 27
    piece = 0
    print(piece)

def sqr_val_28():
    pos_val = 28
    piece = 0
    print(piece)

def sqr_val_29():
    pos_val = 29
    piece = 0
    print(piece)

def sqr_val_30():
    pos_val = 30
    piece = 0
    print(piece)

def sqr_val_31():
    pos_val = 31
    piece = 0
    print(piece)
    

def sqr_val_32():
    pos_val = 32
    piece = 0
    print(piece)

def sqr_val_33():
    pos_val = 33
    piece = 0
    print(piece)

def sqr_val_34():
    pos_val = 34
    piece = 0
    print(piece)

def sqr_val_35():
    pos_val = 35
    piece = 0
    print(piece)

def sqr_val_36():
    pos_val = 36
    piece = 0
    print(piece)

def sqr_val_37():
    pos_val = 37
    piece = 0
    print(piece)


def sqr_val_38():
    pos_val = 38
    piece = 0
    print(piece)

def sqr_val_39():
    pos_val = 39
    piece = 0
    print(piece)

def sqr_val_40():
    pos_val = 40
    piece = 0
    print(piece)

def sqr_val_41():
    pos_val = 41
    piece = 0
    print(piece)

def sqr_val_42():
    pos_val = 42
    piece = 0
    print(piece)

def sqr_val_43():
    pos_val = 43
    piece = 0
    print(piece)

def sqr_val_44():
    pos_val = 44
    piece = 0
    print(piece)

def sqr_val_45():
    pos_val = 45
    piece = 0
    print(piece)

def sqr_val_46():
    pos_val = 46
    piece = 0
    print(piece)

def sqr_val_47():
    pos_val = 47
    piece = 0
    print(piece)

def sqr_val_48():
    pos_val = 48
    piece = 0
    print(piece)

def sqr_val_49():
    pos_val = 49
    piece = 6
    print(piece)

def sqr_val_50():
    pos_val = 50
    piece = 6
    print(piece)

def sqr_val_51():
    pos_val = 51
    piece = 6
    print(piece)

def sqr_val_52():
    pos_val = 52
    piece = 6
    print(piece)

def sqr_val_53():
    pos_val = 53
    piece = 6
    print(piece)

def sqr_val_54():
    pos_val = 54
    piece = 6
    print(piece)

def sqr_val_55():
    pos_val = 55
    piece = 6
    print(piece)

def sqr_val_56():
    pos_val = 56
    piece = 6
    print(piece)

def sqr_val_57():
    pos_val = 57
    piece = 3
    print(piece)

def sqr_val_58():
    pos_val = 58
    piece = 5
    print(piece)

def sqr_val_59():
    pos_val = 59
    piece = 4
    print(piece)

def sqr_val_60():
    pos_val = 60
    piece = 1
    print(piece)

def sqr_val_61():
    pos_val = 61
    piece = 2
    print(piece)

def sqr_val_62():
    pos_val = 62
    piece = 4
    print(piece)

def sqr_val_63():
    pos_val = 63
    piece = 5
    print(piece)
    
def sqr_val_64():
    pos_val = 64
    piece = 3
    print(piece)


if __name__ == "__main__":
    main()