# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from KubaGame.constants import RED, WHITE, BLACK, BLUE, GREY, SQUARE_SIZE, ROWS, COLS, WIDTH, HEIGHT
from KubaGame.kuba import Kuba


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kuba')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    kuba = Kuba(WIN)

    while run:
        clock.tick(FPS)

        if kuba.get_winner():
            print(f'Winner: {kuba.get_winner()}')
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                kuba.select(row, col, WIN)

        kuba.update()

    # pygame.quit()


main()