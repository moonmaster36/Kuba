import unittest
from Board import *


class TestMakeMove(unittest.TestCase):
    def test_horizontal_ko_rule(self):
        # game = Kuba(('p1', 'W'), ('p2', 'B'))
        # game.setupBoard()
        #
        # # Implementing Ko Rule Testing.
        # # Get row 2 into state: [' ', 'W', 'W', 'R', 'B', 'B', ' ']
        # game.make_move('p1', (1, 0), 'R')
        # game.showBoard()
        # game.make_move('p2', (1, 6), 'L')
        # game.showBoard()
        #
        # game.make_move('p1', (1, 1), 'R')  # W pushes right
        # game.showBoard()
        #
        # game.showGame()
        # move = game.make_move('p2', (1, 6), 'L')  # B pushes left, reversing the move W just made.
        # game.showBoard()
        #
        # game.showGame()
        pass

    def test_vertical_ko_rule(self):
        pass
