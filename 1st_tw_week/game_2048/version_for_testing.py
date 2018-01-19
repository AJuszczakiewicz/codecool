import random

def init_game():
    board = [[0 for col in range(4)] for row in range(4)]
    for i in range(2):
        x = new_tile(board)[0]
        y = new_tile(board)[1]
        tile = new_tile(board)[2]
        board[x][y] = tile
    return board

def add_new_tile(board):
    for row in board:
        if 0 in row:
            temp=new_tile(board)
            x = temp[0]
            y = temp[1]
            tile = temp[2]
            board[x][y] = tile
            break
    return board

def new_tile(board):
    two_or_four = random.random()
    if two_or_four <= 0:
        new_tile_value = 4
    else:
        new_tile_value = 2

    new_x  = random.randint(0, 3)
    new_y = random.randint(0, 3)
    while board[new_x][new_y] != 0:
        new_x= random.randint(0, 3)
        new_y = random.randint(0, 3)
    return [new_x, new_y, new_tile_value]

def remove_zeros(lst):
    return [x for x in lst if x != 0]

def add_zeros(lst):
    while len(lst) < 4:
        lst.append(0)
    return lst

def merge_line(line):
    lst = remove_zeros(line)
    new_list = []
    while lst:
        if len(lst) == 1:
            new_list.append(lst[0])
            lst.pop(0)
        elif lst[0] == lst[1]:
            new_list.append(lst[0]*2)
            lst.pop(0)
            lst.pop(0)
        else:
            new_list.append(lst[0])
            lst.pop(0)
    new_list = add_zeros(new_list)
    return(new_list)

def left_merge(board):
    merged = []
    for x in board:
        merged.append(merge_line(x))
    return merged

def right_merge(board):
    merged = []
    for x in board:
        line = x
        line.reverse()
        line = merge_line(line)
        line.reverse()
        merged.append(line)
    return merged

def up_merge(board):
    new_board = [[0 for col in range(4)] for row in range(4)]
    line = []
    merged = []
    temp_board = []
    for x in range(0,4):
        for y in range(0,4):
            line.append(board[y][x])    
        line = merge_line(line)
        temp_board.append(line)
        line = []    
    for x in range(0,4):
        for y in range(0,4):
            new_board[y][x] = temp_board[x][y]
    return new_board

def down_merge(board):
    new_board = [[0 for col in range(4)] for row in range(4)]
    line = []
    temp_board = []
    for x in range(0,4):
        for y in [3,2,1,0]:
            line.append(board[y][x])          
        line = merge_line(line)
        temp_board.append(line)
        line = []
        #print(temp_board)
    for x in range(0,4):
        lst = [3,2,1,0]
        for y in range(0,4):
            new_board[lst[x]][y] = temp_board[y][x]
    return new_board

def game_is_over(board):
    '''returns True when game is over'''
    for i in range(0,4):
        for j in range(0,4):
            if (board[i][j] == 2048):
                return True
    for i in range(0,4):
        for j in range(0,4):
            if (board[i][j] == 0):
                return False
    for i in range(0,4):
        for j in range(0,3):
            if (board[i][j] == board[i][j+1]):
                return False
    for j in range(0,4):
        for i in range(0,3):
            if board[i][j] == board[i+1][j]:
                return False
    return True

def is_winner(board):
    for x in range(0,4):
        for y in range(0,4):
            if board[x][y] == 2048:
                return True
    return False

def reset():
    val = init_game()
    return val

def get_score(board):
    score = 0
    for row in board:
        score += sum(row)
    return(score)

def print_score(board):
    score = get_score(board)
    return "Your current score: {}".format(score)

def show_board(board):
   board_string = ''''''
   for row in board:
       board_string += ('      '.join(str(x) for x in row)) + "\n\n"
   return board_string
