import math
import os
import re

# file = open('test.txt').read()
file = open('input.txt').read()
items = [list(re.sub('[ .]+', ' ', line).strip().split(" ")) for line in file.split("\n")]
operators = items[-1]
nums = [list(map(int, line)) for line in items[:-1]]
# items = file.split("\n")


def part1():
    totals = [0] * len(nums[0])
    for i, row in enumerate(nums):
        for j, val in enumerate(row):
            if operators[j] == '+':
                totals[j] += val
            elif operators[j] == '*' and i > 0:
                totals[j] *= val
            else:
                totals[j] = val
            # totals[j] = eval(f"{totals[j] if i > 0 and operators[j] != '+' else 1}{operators[j]}{val}")
    print(sum(totals))


def part2():
    input_file = file.split("\n")
    max_num_digits = 3
    columns = [[''] * max_num_digits for _ in range(len(nums[0]))]
    for i, row in enumerate(input_file[:-1]):
        for column_idx in range(len(nums[0])):
            curr_column = row[column_idx * (max_num_digits + 1): (column_idx + 1) * (max_num_digits + 1) - 1]
            for offset in range(len(curr_column)):
                columns[column_idx][offset] += curr_column[offset].replace(" ", "")

    total = []
    for j, column in enumerate(columns):
        int_col = map(int, column)
        if operators[j] == '+':
            total.append(sum(int_col))
        else:
            prod = 1
            for entry in int_col:
                prod *= entry
            total.append(prod)
    print(sum(total))
        # for j, val in enumerate(row[::]):
        #     curr_column = j // max_num_digits
        #     columns[curr_column][j % (max_num_digits)] += val
    # items = [list() for line in file.split("\n")]

def part2_new():
    input_file = file.split("\n")
    operator_indices = [i for i, op in enumerate(input_file[-1]) if op != ' ']
    total = 0
    for idx, start_index in enumerate(operator_indices):
        operator = input_file[-1][start_index]
        end_index = operator_indices[idx + 1] - 1 if idx + 1 < len(operator_indices) else len(input_file[0])
        print(start_index, end_index)
        column = [''] * (end_index - start_index + 2)
        running = 0 if operator == '+' else 1
        for j in range(start_index, end_index):
            for i in range(len(input_file[:-1])):
                if j >= len(input_file[i]) or input_file[i][j] in [' ', '.']:
                    continue
                else:
                    column[j - start_index] += input_file[i][j].replace(" ", "")
            if column[j - start_index] == '':
                continue
            if operator == '+':
                running += int(column[j - start_index])
            elif operator == '*':
                running *= int(column[j - start_index])
        total += running
    print(total)




if __name__ == '__main__':
    part1()
    part2_new()