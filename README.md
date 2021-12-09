# AI_project

+ Primary Problem:
- Changes made to the STATE_OF_BOARD list are not being displayed on the Tkinter gui. 
- I understand all of the processes independently...
    - 1. Drawing the chess board on a canvas within the Tkinter gui
    - 2. Assigning photo images to specific pieces to reference throughout the program
    - 3. Displaying the images on the Tkinter gui using a nested for loop
    - 4. Editing the STATE_OF_BOARD list with user input, via click and release
    - 5. Updating the changes to STATE_OF_BOARD using another nested for loop identical to step 3
- BUT, they do not function as intended at a collective level

+ Devised solutions for updating the board
    - Idea: Place the nested for loop referenced in steps 3 and 5 within a function. Call this function whenever there are changes to be displayed
    - Set back: Despite the piece of code in the function definition being identical to its working counterpart, and the fact that all variables are 
      properly defined, the pieces do not appear
    - Idea: simply duplicate the nested for loop so that it runs twice. Once before a move is made, and once after. 
    - Set back: python does not appear to run the second loop despite it being explicitly called. Apparent due to the fact that, 
      although the STATE_OF_BOARD list is changing, the starting position remains on the Tkinter gui. The second nested for loop is 
      not executing with an altered STATE_OF_BOARD list. 



+ smaller issues # this list is mainly for me, as I believe I can solve them independently 
- When a piece is replaced with ‘none’ in the pick_up_pc() function, it shifts neighboring pieces on the same row to the left 
- For the put_down_pc() function, in order to determine what the most previously picked up piece was, I will append the most recently deleted piece to a list, and index that list at -1. 
- I will continue to add to this list
