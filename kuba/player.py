class Player:
    def __init__(self, name, marble_color):
        self.name = name
        self.marble_color = marble_color
        self.marble_count = 8
        self.captured_count = 0
        self.board_state_after_move = None

    def __repr__(self):
        return f"{self.name} '{self.marble_color}'"

    def showBoardStateAfterMove(self):
        print(F"*** {self.name} board_state_after_move: ***")
        if self.board_state_after_move:
            for row in range(len(self.board_state_after_move)):
                print(self.board_state_after_move[row])
            print()
        else:
            print(f'board_copy: {self.board_state_after_move}\n')

    def get_name(self):
        return self.name

    def get_marble_color(self):
        return self.marble_color

    def get_marble_count(self):
        return self.marble_count

    def get_captured_count(self):
        return self.captured_count

    def get_board_state_after_move(self):
        return self.board_state_after_move

    def set_marble_count(self, x):
        self.marble_count = x

    def set_board_state_after_move(self, x):
        self.board_state_after_move = x

    def decrement_marble_count(self, x):
        self.marble_count -= x

    def increment_captured_count(self, x):
        self.captured_count += x