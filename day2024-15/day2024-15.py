import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
# nums = list(map(int, file.split("\n")))
(board, commands) = [list(line) for line in file.split("\n\n")[0].split("\n")], file.split("\n\n")[1].replace("\n", "")

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def move(board, command, curr_loc):
    mapping = {
        "<": (0, -1),
        ">": (0, 1),
        "v": (1, 0),
        "^": (-1, 0),
    }
    new_loc = add(curr_loc, mapping[command])
    # Location should not change
    if board[new_loc[0]][new_loc[1]] == "#":
        return curr_loc
    # Location should change, no boxes to worry about
    elif board[new_loc[0]][new_loc[1]] == ".":
        board[curr_loc[0]][curr_loc[1]] = "."
        board[new_loc[0]][new_loc[1]] = "@"
        return new_loc
    else:
        after_last_box = new_loc
        while board[after_last_box[0]][after_last_box[1]] == "O":
            after_last_box = add(after_last_box, mapping[command])
        if board[after_last_box[0]][after_last_box[1]] == "#":
            return curr_loc
        else:
            board[curr_loc[0]][curr_loc[1]] = "."
            board[new_loc[0]][new_loc[1]] = "@"
            board[after_last_box[0]][after_last_box[1]] = "O"
            return new_loc

def part1():
    robot_loc = (-1, -1)
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == "@":
                robot_loc = (i, j)
                break

    for i, command in enumerate(commands):
        robot_loc = move(board, command, robot_loc)
        # print(i, command)
        # [print("".join(line)) for line in board]

    gps_sum = 0
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == "O":
                gps_sum += i * 100 + j

    print("Part 1:", gps_sum)


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()