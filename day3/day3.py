import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
nums = [list(map(int, list(line))) for line in file.split("\n")]
# items = file.split("\n")


def max_jolts(bank):
    max_battery = 0
    curr_max = 0
    for i in range(len(bank) - 1):
        if bank[i] >= max_battery:
            curr_max = max(int(10 * bank[i] + max(bank[i+1:])), curr_max)
    return curr_max

# memo[(start, i)] = greatest jolts in bank[start:] of length i
def max_jolts_n(memo, bank, start, n):
    if n == 1:
        if (start, 1) not in memo:
            memo[(start, 1)] = max(bank[start:])
        return memo[(start, 1)]
    max_seen = 0
    for i in range(start, len(bank) - n + 1):
        if (i + 1, n - 1) not in memo:
            memo[(i + 1, n - 1)] = max_jolts_n(memo, bank, i + 1, n - 1)
        max_seen = max(max_seen,  bank[i] * (10**(n-1)) + memo[(i + 1, n - 1)])
    return max_seen


def part1():
    jolts_sum = 0
    for bank in nums:
        jolts_sum += max_jolts(bank)
    print("Part 1:", jolts_sum)


def part2():
    jolts_sum = 0
    for bank in nums:
        jolts_sum += max_jolts_n({}, bank, 0, 12)
    print("Part 2:", jolts_sum)


if __name__ == '__main__':
    part1()
    part2()