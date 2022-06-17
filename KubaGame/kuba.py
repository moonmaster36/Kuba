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


def calculate_direction(marble_coords, move_coords):
    print(marble_coords, move_coords)
    row1 = marble_coords[0]
    col1 = marble_coords[1]
    row2 = move_coords[0]
    col2 = move_coords[1]

    row_movement = row2 - row1
    col_movement = col2 - col1
    print(F'(row1, col1): ({row1}, {col1})')
    print(F'(row2, col2): ({row2}, {col2})')
    # print(F'row_movement = {row2} - {row1} = {row_movement}')
    # print(F'col_movement = {col2} - {col1} = {col_movement}')
    print(f'res = ({row_movement}, {col_movement})')
    out = None
    if row_movement == row1 + 2:
        out = 'B'
    print(f'direction = {out}')
    print()
    return out



class Kuba:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, win):
        # self._init()
        self.win = win
        self.board = Board(("p1", "W"), ("p2", "B"))
        self.selected_coords = None
        self.selected_marble_coords = None

    def update(self):
        self.board.draw(self.win)
        pygame.display.update()

    def select(self, row, col, win):
        print(f'name = {self.board.get_current_turn()}')
        current_player = self.board.get_player(self.board.get_current_turn())
        if self.selected_marble_coords:
            # print(F'color:  {self.selected_marble}')
            self.selected_coords = (row, col)
            direction = calculate_direction(self.selected_marble_coords, self.selected_coords)

            result = self.board.make_move(current_player.get_name(),
                                          (self.selected_marble_coords[0], self.selected_marble_coords[1]), direction)
            if not result:
                self.selected_marble_coords = None
                self.selected_coords = None
                self.select(row, col, win)
            else:
                # Clear after sucessful move
                self.selected_coords = None
                self.selected_marble_coords = None

        marble = self.board.get_marble((row, col))
        if marble != " ":
            self.selected_marble_coords = (row, col)
            # Highlight the selected marble.
            # x = SQUARE_SIZE * col + SQUARE_SIZE // 2
            # y = SQUARE_SIZE * row + SQUARE_SIZE // 2
            # radius = SQUARE_SIZE // 5 - self.PADDING
            # pygame.draw.circle(win, BLUE, (x, y), radius)
            # self.update()
            return True
        else:
            self.selected_coords = None
            self.selected_marble_coords = None
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
