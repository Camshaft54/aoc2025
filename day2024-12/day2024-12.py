import math
import os

# file = open('test.txt').read()
file = open('input.txt').read()
# nums = list(map(int, file.split("\n")))
items = file.split("\n")

LEFT = 0
RIGHT = 1
TOP = 2
BOTTOM = 3


class Side:
    def __init__(self):
        pass


def is_plot(neighbor):
    return neighbor is not None and not isinstance(neighbor, Side)


def is_side(neighbor):
    return neighbor is not None and isinstance(neighbor, Side)


class Plot:
    def __init__(self, plot_type, top=None, left=None, bottom=None, right=None):
        self.type = plot_type
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def degree(self):
        return len(self.neighbors())

    def neighbors(self):
        return set(
            filter(lambda x: x is not None and not isinstance(x, Side), [self.top, self.left, self.bottom, self.right]))

    def add_left_side(self):
        if is_plot(self.top) and is_side(self.top.left):
            self.left = self.top.left
        elif not is_plot(self.left):
            self.left = Side()

    def add_top_side(self):
        if is_plot(self.left) and is_side(self.left.top):
            self.top = self.left.top
        elif not is_plot(self.top):
            self.top = Side()

    def add_bottom_side(self):
        if is_plot(self.left) and is_side(self.left.bottom):
            self.bottom = self.left.bottom
        elif not is_plot(self.bottom):
            self.bottom = Side()

    def add_right_side(self):
        if is_plot(self.top) and is_side(self.top.right):
            self.right = self.top.right
        elif not is_plot(self.right):
            self.right = Side()

    def get_neighbor(self, index):
        if index == LEFT:
            return self.left
        elif index == RIGHT:
            return self.right
        elif index == TOP:
            return self.top
        elif index == BOTTOM:
            return self.bottom
        else:
            raise IndexError


def create_farm_map(input_rows: list[str]):
    farm_map = []
    for i, row in enumerate(input_rows):
        farm_map.append([])
        for j, col in enumerate(row):
            farm_map[i].append(Plot(col))
            if i > 0 and farm_map[i - 1][j].type == col:
                farm_map[i][j].top = farm_map[i - 1][j]
                farm_map[i - 1][j].bottom = farm_map[i][j]
            if j > 0 and farm_map[i][j - 1].type == col:
                farm_map[i][j].left = farm_map[i][j - 1]
                farm_map[i][j - 1].right = farm_map[i][j]
    return farm_map


def create_regions(farm_map: list[list[Plot]]):
    region_sets = {}
    visited = set()
    for plots in farm_map:
        for root_plot in plots:
            if root_plot in visited:
                continue
            curr_region = set()
            region_sets[root_plot] = curr_region
            curr_region.add(root_plot)
            frontier = set()
            frontier.add(root_plot)
            while len(frontier) > 0:
                next_plot = frontier.pop()
                frontier = frontier.union(next_plot.neighbors() - visited)
                visited.add(next_plot)
                curr_region.add(next_plot)
    return region_sets


def compute_area(region_set: set[Plot]):
    return len(region_set)


def compute_perimeter(region_set: set[Plot]):
    total = 0
    for plot in region_set:
        total += 4 - plot.degree()
    return total


# def add_sides(visited: set[Plot], curr: Plot):
#     if curr in visited:
#         return
#     visited.add(curr)
#     curr.add_top_side()
#     curr.add_left_side()
#     curr.add_bottom_side()
#     curr.add_right_side()
#     if is_plot(curr.top):
#         add_sides(visited, curr.top)
#     if is_plot(curr.left):
#         add_sides(visited, curr.left)
#     if is_plot(curr.bottom):
#         add_sides(visited, curr.bottom)
#     if is_plot(curr.right):
#         add_sides(visited, curr.right)

def compute_sides(farm_map: list[list[Plot]], region_sets: dict[Plot, set[Plot]]):
    side_counts = {}
    for i, row in enumerate(farm_map):
        for j, start_plot in enumerate(row):
            if start_plot in region_sets.keys():  # if curr plot is a root plot of a region, start counting sides
                curr_region = region_sets[start_plot]
                counts = [0, 0, 0, 0]
                for inner_i in range(0, len(farm_map)):
                    last_seen = [None, None, None, None]
                    for inner_j in range(0, len(farm_map[0])):
                        curr_plot = farm_map[inner_i][inner_j]
                        if curr_plot in curr_region:
                            if curr_plot.top is None:
                                if last_seen[TOP] is None or last_seen[TOP] + 1 < inner_j:
                                    counts[TOP] += 1
                                last_seen[TOP] = inner_j
                            if curr_plot.bottom is None:
                                if last_seen[BOTTOM] is None or last_seen[BOTTOM] + 1 < inner_j:
                                    counts[BOTTOM] += 1
                                last_seen[BOTTOM] = inner_j

                for inner_j in range(0, len(farm_map[0])):
                    last_seen = [None, None, None, None]
                    for inner_i in range(0, len(farm_map)):
                        curr_plot = farm_map[inner_i][inner_j]
                        if curr_plot in curr_region:
                            if curr_plot.left is None:
                                if last_seen[LEFT] is None or last_seen[LEFT] + 1 < inner_i:
                                    counts[LEFT] += 1
                                last_seen[LEFT] = inner_i
                            if curr_plot.right is None:
                                if last_seen[RIGHT] is None or last_seen[RIGHT] + 1 < inner_i:
                                    counts[RIGHT] += 1
                                last_seen[RIGHT] = inner_i
                side_counts[start_plot] = sum(counts)
    return side_counts



def count_sides(region_set: set[Plot]):
    sides = set()
    for plot in region_set:
        if is_side(plot.left):
            sides.add(plot.left)
        if is_side(plot.right):
            sides.add(plot.right)
        if is_side(plot.bottom):
            sides.add(plot.bottom)
        if is_side(plot.top):
            sides.add(plot.top)
    return len(sides)


def part1():
    farm_map = create_farm_map(items)
    region_sets = create_regions(farm_map).values()
    area = [compute_area(region) for region in region_sets]
    perimeter = [compute_perimeter(region) for region in region_sets]
    cost = sum(area[i] * perimeter[i] for i in range(len(region_sets)))
    print("Part 1:", cost)


def part2():
    farm_map = create_farm_map(items)
    region_sets = create_regions(farm_map)
    side_counts = compute_sides(farm_map, region_sets)
    cost = sum(compute_area(region) * side_counts[root] for (root, region) in region_sets.items())
    print("Part 2:", cost)


if __name__ == '__main__':
    part1()
    part2()
