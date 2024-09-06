# Python 3.8.10

# For the complexity analysis, the following official documentation was used to determine the complexity of Python's native methods:
# https://wiki.python.org/moin/TimeComplexity

# Definition:
#  - n is the amount of rows in the board
#  - m is the amount of columns in the board

# PREGUNTAS: ¿Puedo asumir que las columnas tienen todas el mismo largo?
#            ¿Dejo el main y la impresion de la matriz final? Lo use para probar manualmente mi código
#            Cuando dice que el input se ve de esa forma, ¿puedo asumir que es una lista de listas o es una cadena que tengo que procesar?

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
    amount_of_columns = len(board[0]) # Knowing all columns have the same length

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
# - Has a time complexity of O(n * m)
# - Has a space complexity of O(n * m)

# Part B
# - Has a time complexity of O(n * m) because update_neighbours has a time complexity of O(1)
# - Has a space complexity of O(1) because update_neighbours has a space complexity of O(1)

# The resulting complexity of neighbours_minesweeper (and of the whole algorithm) is:
# O(n * m) for time complexity
# O(n * m) for space complexity

def main():
    board = [
        [0, 1, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 0]
    ]

    print("[")
    for row in neighbours_minesweeper(board):
        print("\t", end="")
        print(row)
    print("]")
            
main()