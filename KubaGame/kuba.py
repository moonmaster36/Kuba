import pygame
from KubaGame.constants import RED, WHITE, BLACK, BLUE, GREY, SQUARE_SIZE, ROWS, COLS
from KubaGame.player import Player
from KubaGame.board import Board


def get_p1_from_user():
    print("Enter information for Player 1")
    name = input("Name: ")
    marble_color = input("Marble Color: ")
    print()
    return Player(name, marble_color.upper())


def get_p2_from_user():
    print("Enter information for Player 2")
    name = input("Name: ")
    marble_color = input("Marble Color: ")
    print()
    return Player(name, marble_color.upper())


class Kuba:
    def __init__(self, win):
        self.win = win
        self.p1 = get_p1_from_user()
        self.p2 = get_p2_from_user()
        self.winner = None
        self.current_turn = None
        if self.p1.get_marble_color() == 'W':
            self.current_turn = self.p1
        else:
            self.current_turn = self.p2

        self.selected = None
        self.board = Board()

    # def update(self):
    #     self.board.draw()
    #
    # def _init(self):
    #     self.selected = None
    #     self.board = Board()
    #
