class View:
    X_RANGE = 7
    Y_RANGE = 7

    def __init__(self):
        self.board = [[' ' for _ in range(self.X_RANGE)] for _ in range(self.Y_RANGE)]

    def showBoard(self):
        for i in range(self.Y_RANGE):
            print(self.board[i])

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


if __name__ == '__main__':
    board = View()
    board.setupBoard()
    board.showBoard()
