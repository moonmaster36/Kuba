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
        # self._init()
        self.win = win
        self.board = Board(("p1", "W"), ("p2", "B"))
        self.selected = None

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, row, col):
        if self.selected:
            result = self.board.make_move((row, col))
            if not result:
                self.selected = None
                self.select(row, col)

        marble = self.board.get_marble((row, col))
        current_player_name = self.board.get_current_turn()
        current_player = self.board.get_player(current_player_name)
        if marble != " " and marble == current_player.get_marble_color():
            self.selected = marble
            return True

        return False

    """
    # def _init(self):
    #     self.selected = None
    #     self.board = Board(("p1", "W"), ("p2", "B"))
        # p1 = get_p1_from_user()
        # p2 = get_p2_from_user()
        # self.board = Board((p1.get_name(), p1.get_marble_count()),
        #                    (p2.get_name(), p2.get_marble_count()))
        # self.turn = self.board.get_current_turn()

    # def reset(self):
    #     self._init()
    """

