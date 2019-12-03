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
