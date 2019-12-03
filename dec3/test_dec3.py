import unittest

import pytest

from dec3 import extents, max_grid, dimension, bug_offset


@pytest.mark.parametrize(
    'test, expectation',
    [
        ("U10", [(0, 10), (0, 0)]),
        ("U10,D10", [(0, 10), (0, 0)]),
        ("U10,D20", [(0, 10), (0, -10)]),
        ("U10,D20,R5", [(5, 10), (0, -10)]),
        ("U10,D20,L5", [(0, 10), (-5, -10)]),
    ]
)
def test_extents(test, expectation):
    size = extents(test)
    assert size == expectation


@pytest.mark.parametrize(
    'test, expectation',
    [
        (
                [
                    [(0, 0), (0, 0)],
                    [(0, 0), (0, 0)]
                ],
                [(0, 0), (0, 0)]
        ),
        (
                [
                    [(0, 10), (0, 0)],
                    [(0, 0), (0, 0)]
                ],
                [(0, 10), (0, 0)]
        ),
        (
                [
                    [(15, 1), (1, 1)],
                    [(25, 1), (1, 1)]
                ],
                [(25, 1), (1, 1)]
        ),
        (
                [
                    [(15, 1), (1, 1)],
                    [(25, 10), (1, 1)]
                ],
                [(25, 10), (1, 1)]
        ),
        (
                [
                    [(15, 1), (1, 1)],
                    [(25, -10), (1, 1)]
                ],
                [(25, -10), (1, 1)]
        )
    ]
)
def test_max_grid(test, expectation):
    layout1, layout2 = test
    assert max_grid(layout1, layout2) == expectation


@pytest.mark.parametrize(
    'test, expectation',
    [
        ([(0, 10), (0, 0)], [10, 0]),
        ([(0, 5), (0, 0)], [5, 0]),
        ([(5, 5), (0, 0)], [5, 5]),
        ([(5, 5), (0, -5)], [10, 5]),
        ([(15, 5), (-5, -5)], [10, 20]),
    ]
)
def test_dimension(test, expectation):
    assert dimension(test) == expectation


@pytest.mark.parametrize(
    'test, expectation',
    [
        ([(9284, 7720), (-4662, -4556)], [4662, 4556]),
    ]
)
def test_bug_offset(test, expectation):
    assert bug_offset(test) == expectation
