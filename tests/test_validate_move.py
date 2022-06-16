import unittest
from kuba.Board import *


class TestValidateMove(unittest.TestCase):
    # Invalid Moves
    def test_invalid_backward_break_from_chain(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        move = test_game.validate_move('p1', (1, 1), 'B')
        self.assertIsNotNone(move)
        self.assertFalse(move)

    def test_invalid_right_break_from_chain(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        move = test_game.validate_move('p1', (1, 1), 'R')
        self.assertIsNotNone(move)
        self.assertFalse(move)

    def test_invalid_left_push_own_marble_off(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        move = test_game.validate_move('p1', (1, 1), 'L')
        self.assertIsNotNone(move)
        self.assertFalse(move)

    def test_invalid_forward_push_own_marble_off(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        move = test_game.validate_move('p1', (1, 1), 'F')
        self.assertIsNotNone(move)
        self.assertFalse(move)

    # Valid moves
    def test_valid_backwards(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        move = test_game.validate_move('p1', (0, 1), 'B')
        self.assertIsNotNone(move)
        self.assertTrue(move)

    def test_valid_right(self):
        test_game = Kuba(('p1', 'W'), ('p2', 'B'))
        test_game.setupBoard()
        move = test_game.validate_move('p1', (0, 0), 'R')
        self.assertIsNotNone(move)
        self.assertTrue(move)
