def rowOperation(inp):
    tmpboard = inp

    while(len(tmpboard) < 4):
        tmpboard.append(0)

    for j in range(3):
        if(tmpboard[j] == tmpboard[j + 1] and tmpboard[j] != 0):
            index = j + 1
            tmpboard[j] = tmpboard[j] + 1
            while(index < 3 and tmpboard[index] != 0):
                tmpboard[index] = tmpboard[index + 1]
                index = index + 1
            tmpboard[3] = 0

    return tmpboard

def move(board):
    for i in range(4):
        tmpboard = []

        for j in range(4):
            if(board[i * 4 + j] != 0): 
                tmpboard.append(board[i * 4 + j])
        
        board[i * 4 : i * 4 + 4] = rowOperation(tmpboard)
    
    return board

def rotate_and_move(state, index):
    tmp = list(state)
    tmp_2 = list(state)
    last_tmp = list(state)
    cur_point = 0
    
    if index == 1:
        for j in range(4):
            for k in range(4):
                tmp[j * 4 + k] = tmp_2[k * 4 + 3 - j]
    elif index == 2:
        for j in range(16):
                tmp[j] = tmp_2[15 - j]
    elif index == 3:
        for j in range(4):
            for k in range(4):
                tmp[j * 4 + k] = tmp_2[(3 - k) * 4 + j]
    #print_board(tmp)
    tmp = move(tmp)
    
    if index == 0:
        for j in range(16):
            last_tmp[j] = tmp[j]
    elif index == 1:
        for j in range(4):
            for k in range(4):
                last_tmp[k * 4 + 3 - j] = tmp[j * 4 + k]
    elif index == 2:
        for j in range(16):
                last_tmp[j] = tmp[15 - j]
    elif index == 3:
        for j in range(4):
            for k in range(4):
                last_tmp[(3 - k) * 4 + j] = tmp[j * 4 + k]
        
    return last_tmp