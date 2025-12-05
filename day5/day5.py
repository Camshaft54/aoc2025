from pytreemap import TreeMap

file = open('input.txt').read()
ranges = [(int(line.split("-")[0]), int(line.split("-")[1])) for line in file.split("\n\n")[0].split("\n")]
nums = list(map(int, file.split("\n\n")[1].split("\n")))


def part1():
    goods = 0
    for num in nums:
        good = False
        for r in ranges:
            if r[0] <= num <= r[1]:
                good = True
                break
        if good:
            goods += 1
    print("Part 1:", goods)


def insert(my_map: TreeMap, r):
    start = r[0]
    end = r[1]
    prev_entry = my_map.floor_entry(start)
    if prev_entry is not None and start <= prev_entry.value + 1:
        new_end = max(prev_entry.value, end)
        my_map.put(prev_entry.key, new_end)
    else:
        my_map.put(start, end)


def part2():
    sorted_ranges = sorted(ranges)
    my_map = TreeMap()

    for r in sorted_ranges:
        insert(my_map, r)

    values = 0
    for entry in my_map.entry_set():
        values += entry.value - entry.key + 1
    print("Part 2:", values)


if __name__ == '__main__':
    part1()
    part2()