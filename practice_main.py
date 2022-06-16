import sys
import pygame
from KubaGame.constants import RED, WHITE, BLACK, BLUE, GREY, SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT
from KubaGame.kuba import Kuba
from KubaGame.board import Board
from KubaGame.player import Player

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kuba')
board = Board(("p1", "W"), ("p2", "B"))


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        WIN.fill(BLACK)
        board.draw(WIN)
        pygame.display.flip()


main()
