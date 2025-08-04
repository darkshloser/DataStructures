import unittest
from copy import deepcopy
from sudoku_3x3 import solve_sudoku_3x3  # You’ll need to create this module

class TestSudokuSolver(unittest.TestCase):
    def setUp(self):
        self.initial_board = [
            ['5','3','.','.','7','.','.','.','.'],
            ['6','.','.','1','9','5','.','.','.'],
            ['.','9','8','.','.','.','.','6','.'],
            ['8','.','.','.','6','.','.','.','3'],
            ['4','.','.','8','.','3','.','.','1'],
            ['7','.','.','.','2','.','.','.','6'],
            ['.','6','.','.','.','.','2','8','.'],
            ['.','.','.','4','1','9','.','.','5'],
            ['.','.','.','.','8','.','.','7','9']
        ]

        self.solved_board = [
            ['5','3','4','6','7','8','9','1','2'],
            ['6','7','2','1','9','5','3','4','8'],
            ['1','9','8','3','4','2','5','6','7'],
            ['8','5','9','7','6','1','4','2','3'],
            ['4','2','6','8','5','3','7','9','1'],
            ['7','1','3','9','2','4','8','5','6'],
            ['9','6','1','5','3','7','2','8','4'],
            ['2','8','7','4','1','9','6','3','5'],
            ['3','4','5','2','8','6','1','7','9']
        ]

    def test_solver_returns_true(self):
        board = deepcopy(self.initial_board)
        result = solve_sudoku_3x3(board)
        self.assertTrue(result)

    def test_board_is_solved_correctly(self):
        board = deepcopy(self.initial_board)
        solve_sudoku_3x3(board)
        self.assertEqual(board, self.solved_board)

    def test_no_empty_cells_after_solving(self):
        board = deepcopy(self.initial_board)
        solve_sudoku_3x3(board)
        for row in board:
            self.assertNotIn('.', row)

if __name__ == "__main__":
    unittest.main()