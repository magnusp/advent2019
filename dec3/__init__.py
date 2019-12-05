import math


def extents(input):
    bug = [0, 0]
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0

    for movement in input.split(','):
        bugX, bugY = bug
        direction, distance = [movement[0], int(movement[1:])]
        if direction is 'U':
            bugY = bugY + distance
        elif direction is 'D':
            bugY = bugY - distance
        elif direction is 'L':
            bugX = bugX - distance
        elif direction is 'R':
            bugX = bugX + distance
        else:
            raise RuntimeError(f"Bug cant move that way: {direction}")

        minX = min(bugX, minX)
        maxX = max(bugX, maxX)
        minY = min(bugY, minY)
        maxY = max(bugY, maxY)
        bug = [bugX, bugY]

    return [(maxX, maxY), (minX, minY)]


def max_grid(layout1, layout2):
    res1 = map(
        lambda pair: max(pair, key=abs),
        zip(layout1[0], layout2[0])
    )
    res2 = map(
        lambda pair: max(pair, key=abs),
        zip(layout1[1], layout2[1])
    )
    return [tuple(res1), tuple(res2)]


def dimension(grid):
    maxRange, minRange = grid
    return [maxRange[1] - minRange[1], maxRange[0] - minRange[0]]


def bug_offset(grid):
    _, minRange = grid
    return [abs(minRange[0]), abs(minRange[1])]


def setrogify_wiring(directions):
    wiring = {(0, 0)}
    bug = (0, 0)
    for movement in directions.split(','):
        bug_x, bug_y = bug
        direction, distance = [movement[0], int(movement[1:])]
        line = ()
        if direction is 'U':
            line = [(bug_x, q) for q in range(bug_y, bug_y+distance+1)]
            bug_y = bug_y + distance
        elif direction is 'D':
            line = [(bug_x, q) for q in range(bug_y, bug_y-distance-1, -1)]
            bug_y = bug_y - distance
        elif direction is 'L':
            line = [(q, bug_y) for q in range(bug_x, bug_x-distance-1, -1)]
            bug_x = bug_x - distance
        elif direction is 'R':
            line = [(q, bug_y) for q in range(bug_x, bug_x+distance+1)]
            bug_x = bug_x + distance
        else:
            raise RuntimeError(f"Bug cant move that way: {direction}")
        wiring = wiring.union(line)
        bug = (bug_x, bug_y)

    return wiring