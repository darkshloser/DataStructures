

# +-------+-------+-------+
# | 5 3 . | . 7 . | . . . |
# | 6 . . | 1 9 5 | . . . |
# | . 9 8 | . . . | . 6 . |
# +-------+-------+-------+
# | 8 . . | . 6 . | . . 3 |
# | 4 . . | 8 . 3 | . . 1 |
# | 7 . . | . 2 . | . . 6 |
# +-------+-------+-------+
# | . 6 . | . . . | 2 8 . |
# | . . . | 4 1 9 | . . 5 |
# | . . . | . 8 . | . 7 9 |
# +-------+-------+-------+


def solve_sudoku_3x3(board):
    def is_valid(r, c, num):
        # Check row
        print(board[r])
        if num in board[r]:
            return False

        # Check column
        if num in (board[i][c] for i in range(9)):
            return False

        # Check 3x3 box
        box_row_start = (r // 3) * 3
        box_col_start = (c // 3) * 3
        for i in range(3):
            for j in range(3):
                if board[box_row_start + i][box_col_start + j] == num:
                    return False

        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for num in map(str, range(1, 10)):  # Use str to match the board's string format (because of '.')
                        if is_valid(r, c, num):
                            board[r][c] = num
                            if solve():
                                return True
                            board[r][c] = '.'  # backtrack
                    return False
        return True

    return solve()