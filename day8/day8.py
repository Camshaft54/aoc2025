import math
import os
import networkx as nx

# file = open('test.txt').read()
file = open('input.txt').read()
# nums = list(map(int, file.split("\n")))
junction_boxes = [tuple(map(int, line.split(","))) for line in file.split("\n")]

def calculate_connections(boxes):
    connections = []

    for i, box1 in enumerate(boxes[:-1]):
        for box2 in boxes[i+1:]:
                dist = math.dist(box1, box2)
                connections.append({"1": box1, "2": box2, "dist": dist})

    connections.sort(key=lambda x: x["dist"])

    return connections

def part1():
    connections = calculate_connections(junction_boxes)
    num_to_connect = 1000
    created_connections = connections[:num_to_connect]
    g = nx.Graph()
    g.add_nodes_from(junction_boxes)
    for conn in created_connections:
        g.add_edge(conn["1"], conn["2"], weight=conn["dist"])
    ccs = []
    for cc in nx.connected_components(g):
        ccs.append(len(cc))
    ccs.sort(reverse=True)
    print("Part 1:", ccs[0] * ccs[1] * ccs[2])


def part2():
    connections = calculate_connections(junction_boxes)
    g = nx.Graph()
    g.add_nodes_from(junction_boxes)
    for conn in connections:
        g.add_edge(conn["1"], conn["2"], weight=conn["dist"])
        if nx.is_connected(g):
            print("Part 2:", conn["1"][0] * conn["2"][0])
            return
    print("Failure")


if __name__ == '__main__':
    part1()
    part2()