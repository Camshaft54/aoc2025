import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
ranges = list(map(lambda x: (int(x.split("-")[0]), int(x.split("-")[1])), file.split("\n")[0].split(",")))
# items = file.split("\n")


def part1():
    invalid_nums = []
    for (start, end) in ranges:
        for num in range(start, end + 1):
            if is_invalid(num):
                invalid_nums.append(num)
    print("Part 1:", sum(invalid_nums))

def is_invalid(num):
    num_str = str(num)
    return num_str[:len(num_str) // 2] == num_str[len(num_str) // 2:]

def is_invalid2(num):
    num_str = str(num)
    if len(num_str) <= 1:
        return False
    if num_str[:len(num_str) // 2] == num_str[len(num_str) // 2:]:
        return True

    for chunk_size in range(1, len(num_str) // 2 + 1):
        if len(num_str) % chunk_size != 0:
            continue
        chunk = num_str[:chunk_size]
        passed = True
        for chunk_start in range(0, len(num_str), chunk_size):
            if chunk != num_str[chunk_start:chunk_start + chunk_size]:
                passed = False
                break
        if passed:
            return True
    return False


def part2():
    invalid_nums = []
    for (start, end) in ranges:
        for num in range(start, end + 1):
            if is_invalid2(num):
                invalid_nums.append(num)
    print("Part 2:", sum(invalid_nums))


if __name__ == '__main__':
    part1()
    part2()