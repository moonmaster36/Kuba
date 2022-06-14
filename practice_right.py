from collections import deque
import copy

def shift_right(row, start, end):
    # temp = start[0]
    # start[0] = ' '
    if end <= start:
        return  False
    row_copy = copy.deepcopy(row)
    print(f'before: {row_copy}')
    for i in range(end + 1, start, -1):
        print(i, row_copy)
        row_copy[i] = row_copy[i - 1]
    row_copy[start] = ' '
    print(f'after: {row_copy}')

    return True


if __name__ == '__main__':
    cur_row = ['W', 'W', 'R', 'R', 'R', 'B', 'B']
    start = 0
    end = 1

    print(shift_right(cur_row, start, end))