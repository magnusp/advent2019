import functools
from collections import defaultdict

import pytest
import dec3


@pytest.mark.parametrize(
    'test, expectation',
    [
        ("U2", {(0, 0, 0), (0, 1, 1), (0, 2, 2)}),
        ("D2", {(0, 0, 0), (0, -1, 1), (0, -2, 2)}),
        ("L2", {(0, 0, 0), (-1, 0, 1), (-2, 0, 2)}),
        #("R2", {(0, 0), (1, 0), (2, 0)}),
        #("U2,D2", {(0, 0), (0, 1), (0, 2)}),
        #("D2,U2", {(0, 0), (0, -1), (0, -2)}),
        #("R2,L2", {(0, 0), (1, 0), (2, 0)}),
        #("L2,R2", {(0, 0), (-1, 0), (-2, 0)}),
        ("U10,D10", {(0, 0, 0), (0, 1, 1), (0, 2, 2), (0, 3, 3), (0, 4, 4), (0, 5, 5), (0, 6, 6), (0, 7, 7), (0, 8, 8), (0, 9, 9), (0, 10, 10)}),
        ("L2,R2,U2", {(0, 0, 0), (-1, 0, 1), (-2, 0, 2), (0, 1, 5), (0, 2, 6)}),
        #("L2,R2,U2,D2", {(0, 0), (-1, 0), (-2, 0), (0, 1), (0, 2)}),
        #("L2,R2,D2,U2", {(0, 0), (-1, 0), (-2, 0), (0, -1), (0, -2)}),
        #("L0", {(0, 0)}),
        #("L1,R0", {(0, 0), (-1, 0)}),
    ]
)
def test_transmogrification(test, expectation):
    assert dec3.setrogify_wiring(test) == expectation

@pytest.mark.parametrize(
    'test, expectation',
    [
        (('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'), 610),
        (('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), 410),
    ]
)
def test_santas_solver_works(test, expectation):
    def hailmary(accumulator, value):
        x, y, distance = value
        accumulator[(x, y)] = distance
        return accumulator

    wiring1, wiring2 = test
    layout1 = dec3.setrogify_wiring(wiring1)
    layout2 = dec3.setrogify_wiring(wiring2)

    run1 = functools.reduce(
        hailmary,
        layout1,
        {}
    )
    run2 = functools.reduce(
        hailmary,
        layout2,
        {}
    )

    intersections = run1.keys() & run2.keys()
    intersections.remove((0, 0))

    def solver(accumulator, value):
        combined_distance = run1[value] + run2[value]

        if accumulator is None:
            return combined_distance
        elif combined_distance < accumulator:
            return combined_distance
        return accumulator

    return functools.reduce(
        solver,
        intersections,
        None
    )
