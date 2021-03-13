import numpy as np

#print board
def print_matrix(matrix):
    print('\n'+"  0 1 2")
    print('0 '+matrix[0][0]+' '+matrix[0][1]+' '+matrix[0][2]) 
    print('1 '+matrix[1][0]+' '+matrix[1][1]+' '+matrix[1][2])
    print('2 '+matrix[2][0]+' '+matrix[2][1]+' '+matrix[2][2]+'\n')

def check_winner(matrix,symbol):
    if check_line(matrix,symbol)==1:
        return 1
    if check_column(matrix,symbol)==1:
        return 1
    if check_diagonal(matrix,symbol)==1:
        return 1
    return 0

#check for winner in a line 
def check_line(matrix,symbol):
    for i in matrix:
        if i[0]==symbol and i[1]==symbol and i[2]==symbol:
            return 1
    return 0
 
#check for winner in a column   
def check_column(matrix,symbol):
    if matrix[0][0]==symbol and matrix[1][0]==symbol and matrix[2][0]==symbol:
        return 1
    if matrix[0][1]==symbol and matrix[1][1]==symbol and matrix[2][1]==symbol:
        return 1
    if matrix[0][2]==symbol and matrix[1][2]==symbol and matrix[2][2]==symbol:
        return 1
    return 0   
            
#check for winner in diagonal    
def check_diagonal(matrix,symbol):
    if matrix[0][0]==symbol and matrix[1][1]==symbol and matrix[2][2]==symbol:
        return 1
    if matrix[0][2]==symbol and matrix[1][1]==symbol and matrix[2][0]==symbol:
        return 1
    return 0

#check if there are any empty spaces
def check_draw(matrix):
    counter=0
    for i in range(3):
        for j in range(3):
            if matrix[i][j]=='-':
                counter+=1
    if counter==0:
        return 1
    return 0

#turn of the player
def player_turn(turn):
    #made_move=0 if no valid move was made else made_move=1 if a valid move was made
    made_move=0
    while made_move==0:
        inp=input("Please choose a position (line first, column second): ")
        if len(inp)!=2:
            print("Not a valid value")
        elif inp[0]!='0' and inp[0]!='1' and inp[0]!='2':
            print("Not a valid value")
        elif inp[1]!='0' and inp[1]!='1' and inp[1]!='2':
            print("Not a valid value")
        elif matrix[int(inp[0])][int(inp[1])]!='-':
            print("Position already occupied")
        else:
            matrix[int(inp[0])][int(inp[1])]=turn
            made_move=1
            
def reset(matrix):
    for i in range(3):
        for j in range(3):
            matrix[i][j]='-'
            
#Main
matrix=np.array([['-','-','-'],
              ['-','-','-'],
              ['-','-','-']
              ])
#true if game is still going
state_of_game=True
#current player turn
turn='X'

while state_of_game==True:
    print_matrix(matrix)
    if turn=='X':
        print("Turn of Player 1 ("+turn+")")
    elif turn=='0':
        print("Turn of Player 2 ("+turn+")")
    player_turn(turn)
    if check_winner(matrix, turn)==1:
        if turn=='0':
            print_matrix(matrix)
            print("Player 2 WON")
            inp=input("Want to play again? Type yes/no: ")
            if inp.upper()=='YES':
                state_of_game=True
                reset(matrix)
                turn='0'
            if inp.upper()=='NO':
                state_of_game=False
        if turn=='X':
            print_matrix(matrix)
            print("Player 1 WON")
            inp=input("Want to play again? Type yes/no: ")
            if inp.upper()=='YES':
                state_of_game=True
                reset(matrix)
                turn='0'
            if inp.upper()=='NO':
                state_of_game=False       
    if check_draw(matrix)==1:
        print_matrix(matrix)
        print("It is a draw")
        inp=input("Want to play again? Type yes/no: ")
        if inp.upper()=='YES':
            state_of_game=True
            reset(matrix)
            turn='0'
        if inp.upper()=='NO':
            state_of_game=False
    if turn=='X':
        turn='0'
    else:
        turn='X'
    