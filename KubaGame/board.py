import pygame
from KubaGame.player import Player
from KubaGame.constants import RED, WHITE, BLACK, GREY, BLUE, SQUARE_SIZE, ROWS, COLS


class Board:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, p1: tuple, p2: tuple):
        self.p1 = Player(p1[0], p1[1])
        self.p2 = Player(p2[0], p2[1])
        self.board = [[' ' for _ in range(ROWS)] for _ in range(COLS)]
        self.board_copy = None
        self.red_marbles = 13
        self.white_marbles = self.black_marbles = 8
        self.current_turn = self.find_starting_player()
        self.winner = None
        self.selected_marble_coords = None
        self.ko_rule_violated = False
        self.setupBoard()

    def get_ko_rule_violated(self):
        return self.ko_rule_violated

    def set_selected_marble_coords(self, x):
        self.selected_marble_coords = x

    def find_starting_player(self):
        # White always starts the game.
        if self.p1.get_marble_color() == 'W':
            return self.p1.get_name()
        else:
            return self.p2.get_name()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(win, GREY, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_dots(self, win):
        radius = SQUARE_SIZE // 5 - self.PADDING
        for row in range(ROWS):
            for col in range(COLS):
                x = SQUARE_SIZE * col + SQUARE_SIZE // 2
                y = SQUARE_SIZE * row + SQUARE_SIZE // 2
                pygame.draw.circle(win, GREY, (x, y), radius + self.OUTLINE)
                pygame.draw.circle(win, BLACK, (x, y), radius)

    def draw_marbles(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != ' ':
                    x = SQUARE_SIZE * col + SQUARE_SIZE // 2
                    y = SQUARE_SIZE * row + SQUARE_SIZE // 2
                    if self.board[row][col] == 'W':
                        pygame.draw.circle(win, GREY, (x, y), radius + self.OUTLINE)
                        pygame.draw.circle(win, WHITE, (x, y), radius)
                    elif self.board[row][col] == 'B':
                        pygame.draw.circle(win, GREY, (x, y), radius + self.OUTLINE)
                        pygame.draw.circle(win, BLACK, (x, y), radius)
                    elif self.board[row][col] == 'R':
                        pygame.draw.circle(win, GREY, (x, y), radius + self.OUTLINE)
                        pygame.draw.circle(win, RED, (x, y), radius)

    def draw(self, win):
        self.draw_squares(win)
        self.draw_dots(win)
        self.draw_marbles(win)
        if self.selected_marble_coords:
            # Highlight the selected marble.
            row = self.selected_marble_coords[0]
            col = self.selected_marble_coords[1]
            x = SQUARE_SIZE * col + SQUARE_SIZE // 2
            y = SQUARE_SIZE * row + SQUARE_SIZE // 2
            radius = SQUARE_SIZE // 5 - self.PADDING
            pygame.draw.circle(win, BLUE, (x, y), radius)

    def showGame(self):
        """Prints various details about the game."""
        print(F'-------- Game Details --------')
        print(f'Board Status: \nWhite: {self.white_marbles} \nBlack: {self.black_marbles} \nRed: {self.red_marbles}')
        print(f'Winner: {self.get_winner()}')
        print(f'Turn: {self.get_current_turn()}')

        print()
        print(F'Player 1: {self.p1.get_name()}')
        print(F'Marble Color: {self.p1.get_marble_color()}')
        print(f'Marble Count: {self.p1.get_marble_count()}')
        print(F'Captured: {self.get_captured(self.p1.get_name())}')
        print()
        print(F'Player 2: {self.p2.get_name()}')
        print(F'Marble Color: {self.p2.get_marble_color()}')
        print(f'Marble Count: {self.p2.get_marble_count()}')
        print(F'Captured: {self.get_captured(self.p2.get_name())}')
        print('------------------------------')

    def setupBoard(self):
        # Top left
        self.board[0][0] = 'W'
        self.board[0][1] = 'W'
        self.board[1][0] = 'W'
        self.board[1][1] = 'W'

        # Top right
        self.board[0][5] = 'B'
        self.board[0][6] = 'B'
        self.board[1][6] = 'B'
        self.board[1][5] = 'B'

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

    def set_turn(self, x):
        self.current_turn = x

    def set_winner(self, x):
        self.winner = x

    def get_player(self, playername):
        """Returns the player object given a player name."""
        if self.p1.get_name() == playername:
            return self.p1

        if self.p2.get_name() == playername:
            return self.p2

    def get_board(self):
        return self.board

    def get_current_turn(self):
        return self.current_turn

    def get_winner(self):
        return self.winner

    def get_captured(self, playername):
        if self.p1.get_name() == playername:
            return self.p1.get_captured_count()
        else:
            return self.p2.get_captured_count()

    def get_marble(self, coords: tuple):
        """Return the marble at the given position"""
        row = coords[0]
        col = coords[1]
        # Determine if coords are valid
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.board[row][col]

    def get_marble_count(self):
        white, black, red = 0, 0, 0

        for i in range(COLS):
            for j in range(ROWS):
                current_marble = self.board[i][j]
                if current_marble == 'W':
                    white += 1
                elif current_marble == 'B':
                    black += 1
                elif current_marble == 'R':
                    red += 1
        return white, black, red

    def showBoard(self):
        for i in range(COLS):
            print(self.board[i])
        print()

    def clearBoard(self):
        for i in range(COLS):
            self.board[i].clear()
        self.board = [[' ' for _ in range(ROWS)] for _ in range(COLS)]

    def get_opposite_marble(self, coords: tuple, direction: str):
        """
        Return marble in space opposite of direction. If no marble in space opposite,
        returns None.
        """
        row = coords[0]
        col = coords[1]
        candidate_coords = None
        # Check if marble exists in opposite location of direction of move.
        # Check forward space.
        if direction == 'B':
            candidate_coords = (row - 1, col)  # Check forward space.
        # Check
        if direction == 'R':
            candidate_coords = (row, col - 1)  # Check left space.

        if direction == 'F':
            candidate_coords = (row + 1, col)  # Check backward space.

        if direction == 'L':
            candidate_coords = (row, col + 1)  # Check right space
        opposite_marble = self.get_marble(candidate_coords)
        return opposite_marble

    def check_for_winner(self, current_player, opponent_player) -> bool:
        """
        Immediately after a move has been made, determines if the player that made the
            move has won the game.
        :param current_player: player that just made a move.
        :param opponent_player: opponent of current_player
        :return: True if the player has won
        :return: False if the player has not won
        """
        pass

    def validate_move(self, playername: str, coords: tuple, direction: str) -> bool:
        """
        -Validates a move
        -NOTE: Player attempting to push own marble off is tested in move_right.
        :param playername: player pushing marble
        :param coords: location of marble to push
        :param direction: direction to push marble in
        :return:
        """
        # Check if game has already been won
        if self.get_winner():
            print(F'{self.winner} already won!')
            return False

        # Check if it is playername's turn
        if self.get_current_turn() and self.get_current_turn() != playername:
            print(F"It is not {playername}'s turn!")
            return False

        # Check if row is valid.
        if coords[0] < 0 or coords[0] >= ROWS:
            print(f'Invalid coordinates! coords: ({coords[0]}, {coords[1]})')
            return False

        # Check if column is valid.
        if coords[1] < 0 or coords[1] >= COLS:
            print(f'Invalid coordinates! coords: ({coords[0]}, {coords[1]})')
            return False

        # Verify that the player is allowed to move the chosen marble.
        candidate_marble = self.get_marble(coords)
        candidate_player = self.get_player(playername)

        if candidate_marble == ' ':
            print(f"No marble present at that space! coords: ({coords[0]}, {coords[1]})")
            return False

        if candidate_marble == 'R':
            print(f"You cannot move Red marbles! coords: ({coords[0]}, {coords[1]})")
            return False

        if candidate_marble != candidate_player.get_marble_color():  # This also tests if marble is out of bounds.
            print(F"You cannot move your opponent's marble! coords: ({coords[0]}, {coords[1]})")
            return False

        # Check for space to push.
        opposite_marble = self.get_opposite_marble(coords, direction)

        # Check if marble has space to move (i.e., that marble is not in middle of marble chain.)
        if opposite_marble == 'W' or opposite_marble == 'B' or opposite_marble == 'R':
            print(F'{candidate_player} attempted to push marble in chain: {coords} {direction}')
            return False

        return True

    def move_right(self, row_input, start, current_player):
        """
        - Push marbles at start in row_input to the right.
        - Determines number of marbles affected by move,
            then shifts the marbles over.
        - If player attempts to push own marble off, the
            move is abandoned and returns False
        - Opponent marbles on edge of board are pushed off,
            marble count is updated at end of function.
        - Red (neutral) marbles pushed off board are captured by the current_player.
            Captured count is updated immediately after a red marble is pushed off.
        :param row_input: row in board to shift
        :param start: marble being pushed
        :param current_player: player pushing marble
        :return: True if successful
        :return: False if player tries to knock their own marble off.
        """
        # Determine number of marbles to move
        end = start
        while end < len(row_input) and row_input[end] != ' ':
            end += 1

        # Check to see if this will knock our own marble off
        if end == len(row_input) and row_input[end - 1] == row_input[start]:
            return False

        # If our end is the edge, we know a marble is being pushed off.
        if end == len(row_input):
            end -= 1
            # Determine if a red marble will be pushed off.
            if row_input[end] == 'R':
                current_player.increment_captured_count(1)

        # Shift marbles over
        # temp_row = copy.deepcopy(row_input)
        temp_row = [x for x in row_input]
        cur = start
        for i in range(start + 1, end + 1):
            temp_row[i] = row_input[cur]
            cur += 1
        temp_row[start] = ' '

        # Copy temp_row into row_input
        for i in range(len(temp_row)):
            row_input[i] = temp_row[i]
        return True

    def make_move(self, playername: str, coords: tuple, direction: str) -> bool:
        print(F'make_move params: ({playername}, {coords}, {direction})')
        if not playername or not coords or not direction:
            return False
        current_player = self.get_player(playername)
        print(
            F'{current_player} attempts to move {coords} {direction}')

        # Before doing anything, check if the move is even valid.
        valid = self.validate_move(playername, coords, direction)
        if not valid:
            return False

        if direction == 'R':
            row_number = coords[0]
            successful_right_move = self.move_right(self.board[row_number], coords[1], current_player)
            if not successful_right_move:  # Return false if player tried to push their own marble off.
                print(f'Invalid {direction} move by {current_player.get_name()} at {direction} {coords}')
                return False

        elif direction == 'L':
            # Left movement is accomplished by reversing the row and using move_right function
            row_number = coords[0]
            start = coords[1]
            # row_copy = copy.deepcopy(self.board[row_number])
            row_copy = [x for x in self.board[row_number]]
            row_copy.reverse()

            successful_left_move = self.move_right(row_copy, COLS - 1 - start, current_player)
            if not successful_left_move:  # Return false if player tried to push their own marble off.
                print(f'Invalid {direction} move by {current_player.get_name()} at {direction} {coords}')
                return False

            # Reverse and copy transfer updated row onto game board.
            row_copy.reverse()
            for i in range(len(row_copy)):
                self.board[row_number][i] = row_copy[i]

        elif direction == 'B':
            # Backward movement is accomplished by copying the column then feeding the column into movement_right
            col_number = coords[1]
            # Iterate and copy column
            column_to_modify = []
            for i in range(ROWS):
                column_to_modify.append(self.board[i][col_number])

            successful_backward_move = self.move_right(column_to_modify, coords[0], current_player)
            if not successful_backward_move:  # Return false if player tried to push their own marble off.
                print(f'Invalid {direction} move by {current_player.get_name()} at {direction} {coords}')
                return False

            # Transfer list modified by move_right onto game board.
            for i in range(ROWS):
                self.board[i][col_number] = column_to_modify[i]

        elif direction == 'F':
            # Backward movement is accomplished by copying the column then feeding the column into movement_right
            col_number = coords[1]
            # Iterate and copy column
            column_to_modify = []
            for i in range(ROWS):
                column_to_modify.append(self.board[i][col_number])

            # Reverse before feeding into move_right (because moving forward is opposite of backwards)
            column_to_modify.reverse()

            successful_forward_move = self.move_right(column_to_modify, (COLS - 1) - coords[0],
                                                      current_player)
            if not successful_forward_move:  # Return false if player tried to push their own marble off.
                print(f'Invalid {direction} move by {current_player.get_name()} at {direction} {coords}')
                return False

            # Reverse then transfer modified column onto game board.
            column_to_modify.reverse()
            for i in range(ROWS):
                self.board[i][col_number] = column_to_modify[i]

        # Update all marble counts
        new_counts = self.get_marble_count()
        self.white_marbles = new_counts[0]
        self.black_marbles = new_counts[1]
        self.red_marbles = new_counts[2]

        if self.p1.get_marble_color() == 'W':
            self.p1.set_marble_count(self.white_marbles)
            self.p2.set_marble_count(self.black_marbles)
        else:
            self.p1.set_marble_count(self.black_marbles)
            self.p2.set_marble_count(self.white_marbles)

        # Determine who the opponent player is.
        # Determine who the opponent player is.
        opponent_player = None
        if self.p1.get_name() == current_player.get_name():
            opponent_player = self.p2
        else:
            opponent_player = self.p1

        # Ko Rule enforcement
        if self.board == opponent_player.get_board_state_after_move():
            # Restore game board to previous state
            self.board = opponent_player.get_board_state_after_move()
            restored_marble_count = self.get_marble_count()
            self.white_marbles = restored_marble_count[0]
            self.black_marbles = restored_marble_count[1]
            self.red_marbles = restored_marble_count[2]
            self.ko_rule_violated = True
            print(F"{current_player} violated Ko Rule {coords} {direction}")
            return False

        # After successful move, store board state in opponent_player
        opponent_player.set_board_state_after_move([list(row) for row in self.board])

        # Check if game has been won
        if current_player.get_captured_count() == 7 and self.red_marbles <= 6:
            self.winner = current_player.get_name()

        if opponent_player.get_marble_count() == 0:  # Opponent has no marbles
            self.winner = current_player.get_name()

        # Scan board to determine if opponent has any remaining moves.

        print(F'{current_player} successfully moved {coords} {direction}')
        print()
        self.current_turn = opponent_player.get_name()
        # Reset marble position
        self.selected_marble_coords = None
        self.ko_rule_violated = False
        return True


if __name__ == '__main__':
    game = Board(('p1', 'W'), ('p2', 'B'))
    game.setupBoard()

    # Implementing Ko Rule Testing.
    game.make_move('p1', (0, 0), 'B')
    game.make_move('p2', (6, 0), 'F')

    game.make_move('p1', (1, 0), 'B')
    move = game.make_move('p2', (5, 0), 'F')
    game.showBoard()

    # Violation
    game.make_move('p1', (1, 0), 'B')
    game.showBoard()

