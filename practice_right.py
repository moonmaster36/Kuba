from collections import deque
import copy


def get_marble(col, board):
    return board[col]


def shift_right(row, start):
    row_copy = copy.deepcopy(row)
    # Find the end
    end = start
    while end < len(row_copy) and row_copy[end] != ' ':
        end += 1
    print(F'(start, end) = ({start, end})')
    if end <= start:
        return False
    print(f'before: {row_copy}')

    if end == len(row_copy):
        end -= 2

    for i in range(end, start, -1):
        print(i)
        row_copy[i] = row_copy[i - 1]
    row_copy[start] = ' '
    print(f'after: {row_copy}')

    return True


if __name__ == '__main__':
    # cur_row = ['W', 'W', 'R', 'R', 'R', 'B', ' ']
    cur_row = ['W', 'W', ' ', ' ', ' ', 'B', 'B']
    print(shift_right(cur_row, 0))
