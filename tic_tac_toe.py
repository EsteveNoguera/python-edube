"""                         This is a tic tac toe game to be played in a terminal
The main idea is that there is an object called board that saves the current state of the board in a array 3x3
This array then is used to display the status of the game with the function displa_board() or check if there's 
a winner with the function victory_for() (either X for machine or O for user), that returns a boolean variable 
(winner) if a winner or a draw is found. Finally draw_move() and enter_move() allow to modifiy the board either
by the machine or the user respectively in order to make a move. The function tic_tac_toe() starts the game and
checks if the variable winner returned by the function victory_for() is true and stops the game if so. 
"""
from random import randrange

# This variable is used for different functions in order to check positions or draw a position
# It's a dictionary of all possible positions that can be chosen in the board
positions = {1:(0,0),2:(0,1),3:(0,2),
             4:(1,0),5:(1,1),6:(1,2),
             7:(2,0),8:(2,1),9:(2,2)} 

def display_board(board):
    
    for row in board: # for every row
        print("+-------"*3, end="+\n") # header
        print("|       "*3, end="|\n") # mid space
        print("|   ",row[0],"   ",
              "|   ",row[1],"   ",
              "|   ",row[2],"   ",sep="", end="|\n") # print the values in the board
        print("|       "*3, end="|\n") # mid space
    print("+-------"*3, end="+\n") # tail
        
def make_list_of_free_fields(board):
    
    free_positions = []
    for i in range(len(positions)): # For every element in dictionary positions
        if board[positions[i+1][0]][positions[i+1][1]] not in ["X","O"]: #check if position is not equal to X or O
            free_positions.append(positions[i+1]) # if not equal, add to list as free position
    return(free_positions)

def victory_for(board, sign):

   # This block checks if there's a winner
    reverse_i = [2,1,0] # This list is used to iterate i in reverse for the right diagonal
    left_diag = [] # List that saves left diagonal
    right_diag = [] # List that saves right diagonal
    for i in range(3): # sliding from 0 to 2 in rows
        check_row = [] # create a row with the values in board
        check_column = [] # create a column with the values in board
        left_diag.append(board[i][i]) # create the left diagonal
        right_diag.append(board[i][reverse_i[i]]) # create the right diagonal
        for j in range(3): # sliding from 0 to 2 in columns
            check_row.append(board[i][j]) # create check row
            check_column.append(board[j][i]) # create check column
        if check_row == [sign]*3 or check_column == [sign]*3: #check column or row are winners
            winner = True
            if sign == "X":
                print("Machine won!")
            else:
                print("You won!")
            return winner
    if left_diag == [sign]*3 or right_diag == [sign]*3: #check if any diagonal is a winner
        winner = True
        if sign == "X":
            print("Machine won!")
        else:
            print("You won!")
        return winner # Note: I have the feeling there must be a way to merge this if statement with the previous. 
    
    # This blocks checks if there's a draw. Function stops before if there's a winner. 
    free_positions=make_list_of_free_fields(board) 
    if free_positions == []: # there's no available positions
        print("This is a draw!") # then it's a draw
        winner = True
        return winner
    
    # If all other paths fail, this runs 
    print("Game continues!")
    winner = False
    return winner
        
def draw_move(board):
    
    free_positions = make_list_of_free_fields(board) # create a list with free positions
    move = positions[randrange(1,10)] #make a random move
    while move not in free_positions: #if the random move is not available
        move = positions[randrange(1,10)] #make another random move 
    board[move[0]][move[1]] = "X"
    print("The machine does...")
    display_board(board)
    return board

def enter_move(board):
   
    # The code below try to force user to select a proper integer value. May need some improvement. 
    try:
        position = int(input("Enter your move!:"))  #user enters a value
        print("You have selected", position)
    except: # The code could be expanded to force the user to enter a number like the checks below
        print("You probably entered something that cannot be used as a number. You got 1 more try only!")
        position = int(input("Enter your move!:"))
        print("You have selected", position)
    while position < 1 or position > 9: #if position is out of range
        position = int(input("Your position has to be between 1-9 (check the board):"))
    move = positions[position]
    
    # The code below checks if the value entered is available in the board
    free_positions = make_list_of_free_fields(board) # create a list with free positions
    while move not in free_positions: #if the cell not available
        position = int(input("Your position has to be empty (check the board):")) #force the user to chose another one
        if position >= 1 and position <= 9:
            move = positions[position]
        else:
            print("Remember that the values have to be between 1-9!")
    
    # Modify the board and display it
    board[move[0]][move[1]] = "O"
    display_board(board)
    return board

def tic_tac_toe(board=[[1,2,3],[4,"X",6],[7,8,9]]):
    
    print("Welcome to Tic Tac Toe against the most powerful AI in the world, the infamous randrange function...")
    print("Prepare yourself! The machine has determined that the best way to win is being the first in moving and choosing the center..")
    winner = False # There is no winner yet, the game just started!
    display_board(board) # Print the board
    while not winner: #until the loop finds a winner
        board = enter_move(board) # let the user choose a move
        winner = victory_for(board,"O") # check if user won
        if winner: # if so
            break # stop it
        board = draw_move(board) # let the machine choose a move
        winner = victory_for(board,"X") # check if there is a winner
    print("Amazing game!")

tic_tac_toe() #sarts the game
