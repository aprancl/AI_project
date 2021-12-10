# Chess AI project 

+ Required files 
- chessai--verison13.py
  -/-This is the main program, and invokes all functions necessary to run the project

- all .png files within Pieces and Pieces_2 folders
  -/- The main program will reference two groups of images, depending on user input, and will pull
      from these folders to carry out its functions. 

+ Running the program 
- The user will be prompted with a decision to play either another user in the viscinity, or to play the computer 
- The user will then decide between using normal or alternate chess pieces
- If the user decides to play another user, the board is free for use. Aside from pawns taking forward and pieces having the ability to jump over other pieces, players are forced to follow the rules of the game. The program will not accept illegal moves (other than the cases previously specified). 
- If the user decides to play against the computer, any imput (even if the user were to move black's pieces) will cause the AI to randomly move a piece. The AI is not bound by the rules of the game, and it can only see squares on the first 4 rows; however, it is functional. 