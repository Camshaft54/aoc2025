import math
import os

file = open('input.txt').read()
items = [list(line) for line in file.split("\n")]

def count_adj(items, i, j):
    adj = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    count = 0
    for a in adj:
        adj_pos = (i + a[0], j + a[1])
        if 0 <= adj_pos[0] < len(items) and 0 <= adj_pos[1] < len(items[0]) and items[adj_pos[0]][adj_pos[1]] == '@':
            count += 1
    return count

def part1():
    num_accessible = 0
    for i, row in enumerate(items):
        for j, roll in enumerate(row):
            if roll == '@' and count_adj(items, i, j) < 4:
                num_accessible += 1
    print("Part 1:", num_accessible)

def remove_possible(items):
    num_removed = 0
    for i, row in enumerate(items):
        for j, roll in enumerate(row):
            if roll == '@' and count_adj(items, i, j) < 4:
                items[i][j] = '.'
                num_removed += 1
    return num_removed

def part2():
    total = 0
    while True:
        curr = remove_possible(items)
        total += curr
        if curr == 0:
            break
    print("Part 2:", total)


if __name__ == '__main__':
    part1()
    part2()