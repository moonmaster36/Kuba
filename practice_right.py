from collections import deque
import copy


def get_marble(col, board):
    return board[col]


def old_shift(start, row):
    new_row = row[:]
    end = start
    while end < len(row) - 1 and row[end] != ' ':
        end += 1
    j = start
    for i in range(start + 1, end + 1):
        new_row[i] = row[j]
        j += 1
    new_row[start] = ' '
    print(F'   ({start}, {end}) {new_row}')


def move_nums(nums, start):
    new = nums[:]
    cur = start

    end = start
    while end < len(nums) and nums[end]:
        end += 1

    # If our end is the edge, we know a marble is being pushed off.
    if end == len(nums):
        end -= 1

    # Check to see if this will knock our own marble off

    for i in range(start + 1, end + 1):
        new[i] = nums[cur]
        cur += 1

    new[start] = None
    for i in range(len(new)):
        nums[i] = new[i]
    print(f'{nums} ({start}, {end})')


def shift(row_input, start):
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
    temp_row = row_input[:]
    cur = start
    for i in range(start + 1, end + 1):
        temp_row[i] = row_input[cur]
        cur += 1
    temp_row[start] = ' '
    # Copy into input row
    for i in range(len(temp_row)):
        row_input[i] = temp_row[i]
    print(F'   ({start}, {end}) {temp_row}')
    return True


if __name__ == '__main__':
    starting_row = ['W', 'W', ' ', 'R', ' ', 'B', 'B']
    print(f'Original: {starting_row}')
    print(shift(starting_row, 0))
    print(shift(starting_row, 1))
    print(shift(starting_row, 2))
    print(shift(starting_row, 3))
    print(shift(starting_row, 4))
    print(shift(starting_row, 5))

    # shift(1, [' ', 'W', 'W', 'R', ' ', 'B', 'B'])
    # shift(2, [' ', ' ', 'W', 'W', 'R', 'B', 'B'])

    # row1 = [' ', ' ', ' ', 'W', 'W', 'R', 'B']
    # cur_row = ['W', 'W', 'R', 'R', 'R', 'B', ' ']
    # cur_row = ['W', 'W', ' ', ' ', ' ', 'B', 'B']
    # row = ['W', 'W', ' ', 'R', ' ', 'B', 'B']

    """
        a1 = [1, 2, 3, 4, None, None]
        a = [1, 2, None, None, None, None, 5]
        print(a)
        move(a, 0)
        move(a, 1)
        move(a, 2)
        move(a, 3)
        move(a, 4)

        # new2 = move(new1, 1, 5)
        # new3 = move(new2, 2, 6)
        # new4 = move(new3, 3, 6)
        # new5 = move(new4, 4, 6)
        # print(move(a, 2, 6))
        """
