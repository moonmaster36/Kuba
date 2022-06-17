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
        self.selected_coords = None
        self.selected_marble_color = None

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, row, col):
        if self.selected_coords and self.selected_marble_color:
            print(F'*** Post ***')
            print(F'(row, col): ({row}, {col})')
            print(F'selected_coords:       {self.selected_coords}')
            print(F'selected_marble_color: {self.selected_marble_color}')
            result = self.board.make_move(self.selected_marble, (row, col))
            if not result:
                self.selected = None
                self.select(row, col)

        marble = self.board.get_marble((row, col))
        current_player_name = self.board.get_current_turn()
        current_player = self.board.get_player(current_player_name)
        if marble != " ":
            print(f'marble = {marble}')
            self.selected_marble_color = marble
            self.selected_coords = (row, col)
            print(f'*** Initial ***')
            print(F'selected_coords:       {self.selected_coords}')
            print(F'selected_marble_color: {self.selected_marble_color}')
            return True

        return False

    def get_winner(self):
        return self.board.get_winner()

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

