import unittest
from kuba.Board import *


class TestValidateMove(unittest.TestCase):
    # Tests should return the marble at the OPPOSITE
    def test_backward_move(self):
        """
        Expect forward coords
        (row_number - 1, col)
        """
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        test_board = test_game.get_board()
        test_board[0][2] = 'R'
        test_board[2][0] = 'R'
        opposite_marble = test_game.get_opposite_marble((0, 1), 'B')
        self.assertIsNone(opposite_marble)

    def test_right_move(self):
        """
        Expect left coords
        (row_number, col  - 1)
        """
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        test_board = test_game.get_board()
        test_board[0][2] = 'R'
        test_board[2][0] = 'R'
        opposite_marble = test_game.get_opposite_marble((0, 1), 'R')
        self.assertEqual(opposite_marble, 'W')

    def test_forward_move(self):
        """
        Expect backward coords
        (row_number + 1, col)
        """
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        test_board = test_game.get_board()
        test_board[0][2] = 'R'
        test_board[2][0] = 'R'
        opposite_marble = test_game.get_opposite_marble((0, 1), 'F')
        self.assertEqual(opposite_marble, 'W')

    def test_left_move(self):
        """
        Expect right coords
        (row_number + 1, col)
        """
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        test_board = test_game.get_board()
        test_board[0][2] = 'R'
        test_board[2][0] = 'R'
        opposite_marble = test_game.get_opposite_marble((0, 1), 'L')
        self.assertEqual(opposite_marble, 'R')

    def test_empty_space(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        test_board = test_game.get_board()
        test_board[0][1] = ' '
        test_board[2][1] = 'W'
        opposite_marble = test_game.get_opposite_marble((1, 1), 'B')
        self.assertEqual(opposite_marble, ' ')



if __name__ == '__main__':
    unittest.main()
