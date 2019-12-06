import itertools
from collections import defaultdict


def make_vector_ranges(wiring):
    vector_mapping = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    def make_vector(item):
        direction, distance = (item[0], int(item[1:]))
        return itertools.repeat(vector_mapping[direction], distance)

    return [make_vector(x) for x in wiring.split(',')]


def build(layout):
    d = defaultdict(int)
    bug = (0, 0)
    counter = itertools.count(1, 1)
    for instruction in layout:
        for delta_x, delta_y in instruction:
            bug = (bug[0] + delta_x, bug[1] + delta_y)
            d[bug] = next(counter)

    if (0, 0) in d:
        del d[0, 0]
    return d


def find_nearest_intersection(layout1, layout2):
    def keyFunc(intersection):
        return abs(intersection[0]) + abs(intersection[1])

    closest_intersection = min(
        layout1.keys() & layout2.keys(),
        key=keyFunc
    )
    return keyFunc(closest_intersection)


def find_nearest_by_distance_travelled_intersection(layout1, layout2):
    def keyFunc(intersection):
        return layout1[intersection] + layout2[intersection]

    closest_intersection = min(
        layout1.keys() & layout2.keys(),
        key=keyFunc
    )
    return keyFunc(closest_intersection)
