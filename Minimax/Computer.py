import random

def newNumber(board):
    a = random.randint(0, 15)
    while(board[a] != 0):
        a = random.randint(0, 15)

    b = random.randint(1, 100)
    if(b > 90):
        board[a] = 2
    else:
        board[a] = 1

    return board