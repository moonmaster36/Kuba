class Player:
    def __init__(self, name, marble_color):
        self.name = name
        self.marble_color = marble_color
        self.marble_count = 8
        self.captured_count = 0

    def get_name(self):
        return self.name

    def get_marble_color(self):
        return self.marble_color

    def get_marble_count(self):
        return self.marble_count

    def get_captured_count(self):
        return self.captured_count


class Kuba:
    X_RANGE = 7
    Y_RANGE = 7

    def __init__(self, p1: tuple, p2: tuple):
        self.p1 = Player(p1[0], p1[1])
        self.p2 = Player(p2[0], p2[1])
        self.board = [[' ' for _ in range(self.X_RANGE)] for _ in range(self.Y_RANGE)]
        self.red = 13
        self.white = 8
        self.black = 8
        self.current_turn = None
        self.winner = None

    def get_current_turn(self):
        if self.current_turn:
            return self.current_turn.get_name()
        else:
            return None

    def get_winner(self):
        if self.winner:
            return self.winner.get_name()
        else:
            return None

    def get_captured(self, playername):
        if self.p1.get_name() == playername:
            return self.p1.get_captured_count()
        else:
            return self.p2.get_captured_count()

    def get_marble(self, coords: tuple):
        """Return the marble at the given position"""
        row = coords[0]
        col = coords[1]
        return self.board[row][col]

    def get_marble_count(self):
        white, black, red = 0, 0, 0

        for i in range(self.Y_RANGE):
            for j in range(self.X_RANGE):
                current_marble = self.board[i][j]
                if current_marble == 'W':
                    white += 1
                elif current_marble == 'B':
                    black += 1
                elif current_marble == 'R':
                    red += 1
        return white, black, red

    def showBoard(self):
        for i in range(self.Y_RANGE):
            print(self.board[i])
        print()

    def clearBoard(self):
        for i in range(self.Y_RANGE):
            self.board[i].clear()
        self.board = [[' ' for _ in range(self.X_RANGE)] for _ in range(self.Y_RANGE)]

    def showGame(self):
        """Prints various details about the game."""
        print(F'-------- Game Details --------')
        print(f'Board Status: \nWhite: {self.white} \nBlack: {self.black} \nRed: {self.red}\n')
        print(F'Player 1: {self.p1.get_name()}')
        print(F'Marble Color: {self.p1.get_marble_color()}')
        print(f'Marble Count: {self.p1.get_marble_count()}')
        print(F'Captured: {self.get_captured(self.p1.get_name())}')
        print()
        print(F'Player 2: {self.p2.get_name()}')
        print(F'Marble Color: {self.p1.get_marble_color()}')
        print(f'Marble Count: {self.p1.get_marble_count()}')
        print(F'Captured: {self.get_captured(self.p1.get_name())}')
        print('------------------------------')

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
        self.board[5][3] = 'R'

    def make_move(self, name: str, coords: tuple, direction: str) -> bool:
        candidate = self.get_marble(coords)
        # Verify that the player is allowed to move that marble.
        print(F'candidate = {candidate}')


    # Functions that may be spun off into their own class later.


if __name__ == '__main__':
    game = Kuba(('p1', 'W'), ('p2', 'B'))
    game.setupBoard()
    game.showBoard()
    game.showGame()

    game.make_move((1, 0), 'B')
