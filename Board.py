class Player:
    def __init__(self, name, marble_color):
        self.name = name
        self.marble_color = marble_color
        self.marble_count = 8
        self.captured = 0

    def get_name(self):
        return self.name

    def marble_color(self):
        return self.marble_color()

    def marble_count(self):
        return self.marble_count

    def captured(self):
        return self.captured


class Kuba:
    X_RANGE = 7
    Y_RANGE = 7

    def __init__(self, p1: tuple, p2: tuple):
        self.board = [[' ' for _ in range(self.X_RANGE)] for _ in range(self.Y_RANGE)]

    def showBoard(self):
        for i in range(self.Y_RANGE):
            print(self.board[i])
        print()

    def clearBoard(self):
        for i in range(self.Y_RANGE):
            self.board[i].clear()
        self.board = [[' ' for _ in range(self.X_RANGE)] for _ in range(self.Y_RANGE)]

    def setupBoard(self):
        # Top left
        self.board[0][0] = 'W'
        self.board[0][1] = 'W'
        self.board[1][0] = 'W'
        self.board[1][1] = 'W'

        # Top right
        self.board[0][6] = 'B'
        self.board[0][5] = 'B'
        self.board[1][5] = 'B'
        self.board[1][6] = 'B'

        # Bottom Left
        self.board[5][0] = 'B'
        self.board[5][1] = 'B'
        self.board[6][0] = 'B'
        self.board[6][1] = 'B'

        # Bottom Right
        self.board[5][5] = 'W'
        self.board[5][6] = 'W'
        self.board[6][5] = 'W'
        self.board[6][6] = 'W'

        # Red marbles
        self.board[1][3] = 'R'
        self.board[2][2] = 'R'
        self.board[2][3] = 'R'
        self.board[2][4] = 'R'
        self.board[3][1] = 'R'
        self.board[3][2] = 'R'
        self.board[3][3] = 'R'
        self.board[3][4] = 'R'
        self.board[3][5] = 'R'
        self.board[4][2] = 'R'
        self.board[4][3] = 'R'
        self.board[4][4] = 'R'
        self.board[5][5] = 'R'

    def get_marble(self, coords: tuple):
        """Return the marble at the given position"""
        row = coords[0]
        col = coords[1]
        return self.board[row][col]

    # Functions that may be spun off into their own classl later.
    def


if __name__ == '__main__':
    game = Kuba()
    game.setupBoard()
    game.showBoard()

    p1 = Player('p1', 'W')
    p2 = Player('p2', 'B')
