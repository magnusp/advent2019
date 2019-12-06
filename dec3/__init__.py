import itertools
from typing import Set


def use_hex(wiring, x: int, y: int, travelled: int) -> tuple:
    maybe_tuple = filter(
        lambda t: t[0] == x and t[1] == y,
        wiring
    )
    try:
        return next(maybe_tuple)
    except StopIteration:
        return x, y, travelled


def setrogify_wiring(directions):
    wiring = {(0, 0, 0)}
    bug = (0, 0, 0)

    for movement in directions.split(','):
        bug_x, bug_y, distance_traveled = bug
        direction, distance = [movement[0], int(movement[1:])]
        line = ()
        if direction is 'U':
            line = [use_hex(wiring, bug_x, q, p) for q, p in zip(range(bug_y, bug_y + distance + 1), itertools.count(distance_traveled))]
            bug_y = bug_y + distance
        elif direction is 'D':
            line = [use_hex(wiring, bug_x, q, p) for q, p in zip(range(bug_y, bug_y - distance - 1, -1), itertools.count(distance_traveled))]
            bug_y = bug_y - distance
        elif direction is 'L':
            line = [use_hex(wiring, q, bug_y, p) for q, p in zip(range(bug_x, bug_x - distance - 1, -1), itertools.count(distance_traveled))]
            bug_x = bug_x - distance
        elif direction is 'R':
            line = [use_hex(wiring, q, bug_y, p) for q, p in zip(range(bug_x, bug_x + distance + 1), itertools.count(distance_traveled))]
            bug_x = bug_x + distance
        else:
            raise RuntimeError(f"Bug cant move that way: {direction}")
        wiring = wiring.union(line)
        bug = (bug_x, bug_y, distance_traveled + distance)

    return wiring


def solve_for_santa(intersection: Set) -> int:
    def keyFunction(element):
        return abs(element[0]) + abs(element[1])

    smaller_set = intersection.difference({(0, 0)})
    gingerbread_location = min(smaller_set, key=keyFunction)
    return keyFunction(gingerbread_location)


def make_vector_ranges(wiring):
    zero_cycle = itertools.cycle([0])
    positive_cycle = itertools.cycle([1])
    negative_cycle = itertools.cycle([-1])

    def make_vector(item):
        direction, distance = (item[0], int(item[1:]))
        if direction is 'U':
            change = (zero_cycle, positive_cycle)
        elif direction is 'D':
            change = (zero_cycle, negative_cycle)
        elif direction is 'L':
            change = (negative_cycle, zero_cycle)
        elif direction is 'R':
            change = (positive_cycle, zero_cycle)
        else:
            raise ValueError

        return itertools.islice(itertools.cycle(change), 0, distance)

    return [make_vector(x) for x in wiring.split(',')]

def build(layout):
    d = {}
    bug = (0, 0)
    for instruction in layout:
        bug_x, bug_y = bug
        flurp = list(instruction)
        i = 0


def solve_for_santa_but_better(wiring1, wiring2):
    pass