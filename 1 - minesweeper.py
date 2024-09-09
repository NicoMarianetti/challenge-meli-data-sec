# Python 3.8.10

# For the complexity analysis, the following official documentation was used to determine the complexity of Python's native methods:
# https://wiki.python.org/moin/TimeComplexity

# Definition:
#  - n is the amount of rows in the board, knowing that the board is a square then n is also the amount of columns. Then n^2 is the amount of tiles on the board

MINE = 1
REPLACE_MINE = 9    

ROW = 0
COLUMN = 1

def is_in_board(neighbour, amount_of_rows, amount_of_columns):
    return neighbour[ROW] >= 0 and neighbour[ROW] < amount_of_rows and neighbour[COLUMN] >= 0 and neighbour[COLUMN] < amount_of_columns

def update_neighbours(i, j, board, neighbours_board, amount_of_rows, amount_of_columns):
    for neightbour_i in range(-1, 2):
        for neighbour_j in range(-1, 2):
            neighbour = (i + neightbour_i, j + neighbour_j)
            if neighbour != (i, j) and is_in_board(neighbour, amount_of_rows, amount_of_columns) and board[neighbour[ROW]][neighbour[COLUMN]] != MINE:
                        neighbours_board[neighbour[ROW]][neighbour[COLUMN]] += 1

def neighbours_minesweeper(board):

    amount_of_rows = len(board)
    if amount_of_rows == 0:
         return []

    amount_of_columns = amount_of_rows # Knowing the board is a square

    # Part A
    neighbours_board = [row.copy() for row in board]

    # Part B
    for i in range(amount_of_rows):
        for j in range(amount_of_columns):
            if board[i][j] == MINE:
                update_neighbours(i, j, board, neighbours_board, amount_of_rows, amount_of_columns)
                neighbours_board[i][j] = REPLACE_MINE

    return neighbours_board

# Complexity analysis of neighbours_minesweeper:

# Part A
# - Has a time complexity of O(n^2)
# - Has a space complexity of O(n^2)

# Part B
# - Has a time complexity of O(n^2) because update_neighbours has a time complexity of O(1)
# - Has a space complexity of O(1) because update_neighbours has a space complexity of O(1)

# The resulting complexity of neighbours_minesweeper (and of the whole algorithm) is:
# O(n^2) for time complexity
# O(n^2) for space complexity

def main():
    board = [
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0],
        [1, 1, 0, 1, 0]
    ]

    print("[")
    for row in neighbours_minesweeper(board):
        print("\t", end="")
        print(row)
    print("]")
            
main()