from shapely.geometry.polygon import Polygon

# file = open('test.txt').read()
file = open('input.txt').read()
nums = [tuple(map(int, line.split(","))) for line in file.split("\n")]
# items = file.split("\n")


def part1():
    max_area = 0
    for i, num1 in enumerate(nums[:-1]):
        for j, num2 in enumerate(nums, start=i+1):
            area = (abs(num1[0] - num2[0]) + 1) * (abs(num1[1] - num2[1]) + 1)
            max_area = max(area, max_area)
    print("Part 1:", max_area)


def part2():
    polygon = Polygon(nums)
    max_area = 0
    for i, num1 in enumerate(nums[:-1]):
        for j, num2 in enumerate(nums, start=i + 1):
            candidate = Polygon([num1, (num1[0], num2[1]), num2, (num2[0], num1[1])])
            area = (abs(num1[0] - num2[0]) + 1) * (abs(num1[1] - num2[1]) + 1)
            if area > max_area and polygon.covers(candidate):
                max_area = area
    print("Part 2:", max_area)

if __name__ == '__main__':
    part1()
    part2()