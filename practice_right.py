from collections import deque
import copy

def shift_right(row, start, end):
    # temp = start[0]
    # start[0] = ' '
    row_copy = copy.deepcopy(row)
    print(f'before: {row_copy}')
    for i in range(start + 1, end + 1):
        print(i)
        temp = row_copy[i]
        next = row_copy[i + 1]
        row_copy[i] = row_copy[i - 1]
    print(f'after: {row_copy}')


if __name__ == '__main__':
    cur_row = ['W', 'W', 'B', ' ', ' ', 'B', 'B']
    start = 0
    end = 3 

    print(shift_right(cur_row, start, end))