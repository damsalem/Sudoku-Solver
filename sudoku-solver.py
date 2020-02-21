

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    """Recursively run find_empty, valid, and solve to solve a sudoku board"""
    find = find_empty(board)
    # 1. if there are no empty spots, board is solved
    if not find:
        return True
    else:
        # 2. else, set row and col to position (tuple)
        row, col = find
    for i in range(1, 10):
        # 3. if board, num, pos is valid solution
        if valid(board, i, (row, col)):
            # 4. then add to board
            board[row][col] = i
            # 5. then try to call solve recursively until find is true
            if solve(board):
                return True
            # 7. resetting the last value, exiting for loop and goign to #6
            board[row][col] = 0

    # 6. or we it's false, we exit the recursive function, return to #5 and go to #7
    return False


def valid(board, num, pos):
    """Check for duplicate values in row, column, and box"""
    # check row
    for i in range(len(board[0])):
        # check if any digit in the row is same as our new num, excluding the col (pos[1]) of our new num
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(board)):
        # check if any digit in the column is same as our new num, excluding the row (pos[0]) of our new num
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check box
    # the col: the modulus of 3 is 0, 1, or 2
    box_x = pos[1] // 3
    # the row: the modulus of 3 is 0, 1, or 2
    box_y = pos[0] // 3
    # set a range for the height of box
    for i in range(box_y * 3, box_y * 3 + 3):
        # set a range for the width of box
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(board):
    """Format a board so it can be solved with solve()"""
    # every row
    for i in range(len(board)):
        # every 3rd row (modulo of 0) print a horizontal line
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        # every number in a row
        for j in range(len(board[0])):
            # every third number gets a pipe divider
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # if at the final position, print number
            if j == 8:
                print(board[i][j])
            else:
                # else, print out the number with a space, no new line
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """Find an empty position on the sudoku board to solve"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            # if find an empty spot (0), return it's position
            if board[i][j] == 0:
                return (i, j)  # row then column

    return None


print("Unsolved Board:")
print_board(board)
solve(board)
print("_______________________\n")
print("Solved Board:")
print_board(board)

# 1 Pick empty square
# 2 For loop to try each number
# 3 Find valid number
# 4 If valid number, repeat
# 5 Else, backtrack if number is not valid
