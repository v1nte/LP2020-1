from random import randint as ran 
from os import system as sys

board = ["1","2","3","4","5","6","7","8","9"]

def Main():
    """This is the main function"""

    for i in range(9):
        sys("clear")
        print_board()

        if i % 2:
            random_move()
        else:
            insert_user()
        
        _winner = winner()
        
        if not _winner == 0:
            break
            
    sys("clear")
    print_board()
    
    if _winner == 1:
        print("Ganaste xd")
    elif _winner == 2:
        print("hermano perdiste, como tan tonto")
    else:
        print("empate?XDXDXD")

def print_board():
    """ Just print how Board is"""

    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])



def insert_user():
    """User make his move"""

    while True: #Emulate Do-While
        print('Haga su jugada')
        move = input()
        
        if is_valid_move(move):
            #move-1, because of index. 
            board[int(move)-1] = "X"
            break

def random_move():
    """Make a random move"""

    while True: #emulate Do-While
        move = ran(1,9)
        if is_valid_move(str(move)):
            board[move-1] = "O"
            break


def is_valid_move(move):
    """Return True if is a valid move, false otherwise"""
    
    aux = move
    if aux in "123456789":
        aux = int(aux)
        if board[aux-1] not in "XO":
            return True 

    return False

def winner():
    """Return 1 if user win, 2 lose, and 0 draw"""

    if board[0] == "X" or board[0] == "O":
        if board[0] == board[1] and board[0] == board[2]:
            if board[0] == "X":
                return 1
            else:
                return 2  

        if board[0] == board[3] and board[0] == board[6]:
            if board[0] == "X":
                return 1 
            else:
                return 2  

    if board[4] == "X" or board[4] == "O":
        if board[4] == board[0] and board[4] == board[8]:
            if board[4] == "X":
                return 1 
            else:
                return 2  

        if board[4] == board[3] and board[4] == board[5]:
            if board[4] == "X":
                return 1 
            else:
                return 2  

        if board[4] == board[6] and board[4] == board[2]:
            if board[4] == "X":
                return 1 
            else:
                return 2  

        if board[4] == board[1] and board[4] == board[7]:
            if board[4] == "X":
                return 1 
            else:
                return 2 

    if board[8] == "X" or board[8] == "O":
        if board[8] == board[2] and board[8] == board[5]:
            if board[8] == "X":
                return 1
            else:
                return 2

        if board[8] == board[6] and board[8] == board[7]:
            if board[8] == "X":
                return 1
            else:
                return 2 
    return 0

if __name__=="__main__":
    Main()
