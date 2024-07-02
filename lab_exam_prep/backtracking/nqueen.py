
def is_safe(board, x, y, n):
    for i in range(n):
        if board[i][y] == 1:
            return False

    row = x
    col = y
    while row >= 0 and col >= 0:
        if board[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    while row >= 0 and col < n:
        if board[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def check_n_queen(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if (check_n_queen(board, row+1, n)):
                return True
            board[row][col] = 0
    return False


def n_queen(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solution_found = check_n_queen(board, 0, n)
    return solution_found, board