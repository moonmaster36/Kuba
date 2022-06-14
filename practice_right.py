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


def shift(start, row):
    new_row = row[:]
    end = start
    while end < len(row) and row[end] != ' ':
        end += 1
    for i in range(start + 1, end + 2):
        print(i, row[i])
    # j = end - 1
    # for i in range(end, start, -1):
    #     # print(i, row[i], row[j])
    #     new_row[i] = row[j]
    #     j -= 1
    new_row[start] = ' '
    print(F'   ({start}, {end}) {new_row}')


def move(nums, start):
    new = nums[:]
    cur = start

    end = start
    while end < len(nums) and nums[end]:
        end += 1

    # If our end is the edge, we know a marble is being pushed off. 
    if end == len(nums):
        end -= 1

    for i in range(start + 1, end + 1):
        new[i] = nums[cur]
        cur += 1

    new[start] = None
    for i in range(len(new)):
        nums[i] = new[i]
    print(f'{nums} ({start}, {end})')


if __name__ == '__main__':
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
    starting_row = ['W', 'W', ' ', 'R', ' ', 'B', 'B']
    print(f'Original: {starting_row}')
    shift(0, starting_row)
    # shift(1, [' ', 'W', 'W', 'R', ' ', 'B', 'B'])
    # shift(2, [' ', ' ', 'W', 'W', 'R', 'B', 'B'])
    """
    # row1 = [' ', ' ', ' ', 'W', 'W', 'R', 'B']
    # cur_row = ['W', 'W', 'R', 'R', 'R', 'B', ' ']
    # cur_row = ['W', 'W', ' ', ' ', ' ', 'B', 'B']
    # row = ['W', 'W', ' ', 'R', ' ', 'B', 'B']
