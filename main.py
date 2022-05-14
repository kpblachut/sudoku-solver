from copy import deepcopy


board = [
    [9,0,0,2,0,0,0,0,7],
    [1,4,0,5,0,7,2,0,3],
    [3,0,7,0,0,4,0,0,5],
    [0,0,6,1,7,0,0,0,0],
    [4,8,3,0,2,5,0,0,9],
    [7,0,1,0,3,8,0,0,0],
    [8,3,4,0,0,0,6,0,1],
    [0,0,0,0,8,1,9,5,4],
    [0,1,0,0,0,6,0,0,0]
]

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("-------------------------")
        for j in range(len(board[i])):
            if j % 3 == 0:
                print('|', end=" ")
            print(board[i][j], end=" ")

        print("|")
    print("-------------------------")
    

def validate(board, y, x, value):
    #spot validation
    if board[y][x] != 0:
        return False

    # vertical validation
    if value in board[y]:
        return False

    # horizontal validation
    if value in [board[i][x] for i in range(9)]:
        return False
    
    # box validation
    section_y = 3*(y // 3) 
    section_x = 3*(x // 3)

    for i in range(section_y, section_y + 3):
        for j in range(section_x, section_x + 3):
            if value  == board[i][j]:
                return False

    return True

def solve(board):
    if isSolved(board):
            print_board(board)
            return
    y, x = find_next_empty_square(board)
    for i in range(1, 10):
        
        if validate(board, y, x , i):
            # print(f"position: {y} : {x} | value: {i}")
            copy = deepcopy(board)
            copy[y][x] = i
            solve(copy)
                
        

def isSolved(board):
    for row in board:
        if 0 in row:
            return False
        
    return True


def find_next_empty_square(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    

if __name__ == "__main__":
    print_board(board)
    solve(board)
