import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
items = file.split("\n")


def part1():
    x = 50
    times_eq_0 = 0
    for item in items:
        is_left = item[0] == 'L'
        value = int(item[1:])
        x = (x + (-value if is_left else value)) % 100
        if x == 0:
            times_eq_0 += 1
    print("Part 1:", times_eq_0)

def part2():
    x = 50
    times_pass_0 = 0
    for item in items:
        is_left = item[0] == 'L'
        value = int(item[1:])
        times_pass_0 += count_crossings(x, value, is_left)
        x = (x + (-value if is_left else value)) % 100
    print("Part 2:", times_pass_0)


def count_crossings(current_x, distance, is_left):
    # Case 1: we moved left and land at 0 mod 100 (and we were not already at 0)
    if is_left and 0 < current_x <= distance % 100:
        # We add 1 to account for landing at 0 and add # of times we passed zero (but did not land at it)
        return 1 + distance // 100
    # Case 2: we move right and land at 0 mod 100
    elif not is_left and current_x + distance % 100 >= 100:
        return 1 + distance // 100
    # We did not land at 0 or were already at 0 so only count times we would have passed it
    return distance // 100

part1()
part2()