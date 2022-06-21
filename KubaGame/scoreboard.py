import pygame
from KubaGame.constants import RED, WHITE, BLACK, BLUE, GREY, SQUARE_SIZE, ROWS, COLS
from KubaGame.player import Player
from KubaGame.board import Board


class ScoreBoard:
    def __init__(self, win, kuba):
        self._win = win
        self._kuba_game = kuba

    def draw(self, win):
        self.draw_frame(win)

    def draw_frame(self, win):
        win.fill(BLUE)

    def update(self):
        pass
