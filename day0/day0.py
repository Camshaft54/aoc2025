"""
This is actually Day 2 from 2024
"""
import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
# nums = list(map(int, file.split("\n")))
items = file.split("\n")


def part1():
    safe_count = 0
    for item in items:
        parsed = list(map(int, item.split(" ")))
        increasing = parsed[0] < parsed[1]
        is_safe = True
        for i in range(1, len(parsed)):
            if 1 <= abs(parsed[i] - parsed[i - 1]) <= 3:
                if (increasing and parsed[i - 1] < parsed[i]) or (not increasing and parsed[i - 1] > parsed[i]):
                    continue
                else:
                    is_safe = False
            else:
                is_safe = False
        if is_safe:
            safe_count += 1

    print("Part 1: ", safe_count)

def is_safe(parsed_input, increasing: bool, remove = None):
    if remove is not None:
        parsed = parsed_input.copy()
        parsed.pop(remove)
    else:
        parsed = parsed_input

    for i in range(1, len(parsed)):
        if 1 <= abs(parsed[i] - parsed[i - 1]) <= 3:
            if (increasing and parsed[i - 1] < parsed[i]) or (not increasing and parsed[i - 1] > parsed[i]):
                continue
            else:
                return False, i
        else:
            return False, i
    return True, -1

def part2():
    safe_count = 0
    for item in items:
        parsed = list(map(int, item.split(" ")))
        safe = is_safe(parsed, True)[0] or (is_safe(parsed, False)[0])
        if safe:
            safe_count += 1
            continue
        for i in range(len(parsed)):
            safe = is_safe(parsed, True, i)[0] or (is_safe(parsed, False, i)[0])
            if safe:
                safe_count += 1
                break

    print("Part 2: ", safe_count)

part1()
part2()