import unittest
from .Board import *


class TestValidateMove(unittest.TestCase):
    # Tests should return the marble at the OPPOSITE
    def test_backward_move(self):
        """
        Expect forward coords
        (row - 1, col)
        """
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        opposite_marble = test_game.get_opposite_marble((0, 1), 'B')
        self.assertIsNone(opposite_marble)

    def test_right_move(self):
        """
        Expect left coords
        (row, col  - 1)
        """
        pass

    def test_forward_move(self):
        """
        Expect backward coords
        (row + 1, col)
        """
        pass

    def test_left_move(self):
        """
        Expect right coords
        (row + 1, col)
        """
        pass


if __name__ == '__main__':
    unittest.main()
