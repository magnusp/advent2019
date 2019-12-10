from collections import defaultdict

test_input = [(item[0], item[1]) for item in [line.strip().split(')') for line in open('puzzle_input.txt').readlines()]]


def build_predecessor_graph(edges):
    graph = {k: None for k in list(set.union(*map(set, edges)))}
    for edge in edges:
        graph[edge[1]] = edge[0]
    return graph


def calculate_distance(graph, source, target):
    distance = 0
    current = source
    while current != target:
        current = graph[current]
        distance+=1
    return distance


def test_something():
    graph = build_predecessor_graph(test_input)
    distance_to_root = defaultdict(lambda: -1)
    for source in graph.keys():
        distance_to_root[source] = calculate_distance(graph, source, 'COM')

    summed_distances = sum(distance_to_root.values())
    # assert calculate_orbits(test_input) == 42
    i = 0
