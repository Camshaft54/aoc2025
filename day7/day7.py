import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
# nums = list(map(int, file.split("\n")))
items = [list(line) for line in file.split("\n")]


def part1():
    split = 0
    for i, line in enumerate(items[1:]):
        for j, val in enumerate(line):
            if items[i-1][j] in ['S', '|']:
                if val == '^':
                    split += 1
                    line[j - 1] = '|'
                    line[j + 1] = '|'
                else:
                    line[j] = '|'
    print("Part 1:", split)



def part2():
    possibilities = [[0] * len(items[0])  for _ in range(len(items))]
    possibilities[0] = [1 if val == 'S' else 0 for val in items[0]]
    for i in range(1, len(items)):
        for j in range(len(items[0])):
            if items[i][j] == '^':
                possibilities[i][j - 1] += possibilities[i - 1][j]
                possibilities[i][j + 1] += possibilities[i - 1][j]
            else:
                possibilities[i][j] += possibilities[i - 1][j]
    print("Part 2:", sum(possibilities[-1]))

if __name__ == '__main__':
    part1()
    part2()