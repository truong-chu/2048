from Player import rotate_and_move

STEP = 5

def print_board(state):
    for i in range(4):
        for j in range(4):
            k = state[i * 4 + j]
            if k == 0:
                print("-", end=" ")
            else:
                print(2 ** k, end=" ")
        print()
    print()

def calculate(state):
    point = 0
    not_empty = 0

    for i in range(16):

        if state[i] == 0:
            continue
        
        point = point + 2 ** state[i]
        not_empty = not_empty + 1

    return float(point / not_empty)

def minimax(state, depth, turn):
    # score gained
    # possible score gained
    # empty tiles on the board
    # monotonicity

    if depth == 0:
        return calculate(state), state

    if turn == "play":
        point_list = []

        for i in range(4):
            point_state, new_state = minimax(tuple(rotate_and_move(list(state), i)), depth - 1, "comp")
            point_list.append(tuple([point_state, new_state]))

        point_list.sort()
        if depth == STEP:
            return point_list[3]
        else:
            return point_list[3][0], state
    else:
        # calculate possible score
        point_list = []
        tmp_list = list(state)

        for i in range(16):
            if tmp_list[i] != 0:
                continue

            tmp_list[i] = 1
            point_state, new_state = minimax(tuple(tmp_list), depth - 1, "play")
            point_list.append(tuple([point_state, new_state]))

            
            tmp_list[i] = 2
            point_state, new_state = minimax(tuple(tmp_list), depth - 1, "play")
            point_list.append(tuple([point_state, new_state]))

            tmp_list[i] = 0
        
        point_list.sort()
        
        if depth == STEP:
            return point_list[0]
        else:
            return point_list[0][0], state
        
state = (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)

for i in range(100):
    print_board(list(state))
    point_get, state = minimax(state, STEP, "play")
    print_board(list(state))
    point_get, state = minimax(state, STEP, "comp")

print_board(list(state))