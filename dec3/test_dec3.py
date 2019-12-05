import unittest

import pytest
import dec3
from dec3 import extents, max_grid, dimension, bug_offset


@pytest.mark.parametrize(
    'test, expectation',
    [
        ("U2", {(0, 0), (0, 1), (0, 2)}),
        ("D2", {(0, 0), (0, -1), (0, -2)}),
        ("L2", {(0, 0), (-1, 0), (-2, 0)}),
        ("R2", {(0, 0), (1, 0), (2, 0)}),
        ("U2,D2", {(0, 0), (0, 1), (0, 2)}),
        ("D2,U2", {(0, 0), (0, -1), (0, -2)}),
        ("R2,L2", {(0, 0), (1, 0), (2, 0)}),
        ("L2,R2", {(0, 0), (-1, 0), (-2, 0)}),
        ("U10,D10", {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10)}),
        ("L2,R2,U2", {(0, 0), (-1, 0), (-2, 0), (0, 1), (0, 2)}),
        ("L2,R2,U2,D2", {(0, 0), (-1, 0), (-2, 0), (0, 1), (0, 2)}),
        ("L2,R2,D2,U2", {(0, 0), (-1, 0), (-2, 0), (0, -1), (0, -2)}),
        ("L0", {(0, 0)}),
        ("L1,R0", {(0, 0), (-1, 0)}),
    ]
)
def test_transmogrification(test, expectation):
    assert dec3.setrogify_wiring(test) == expectation

@pytest.mark.parametrize(
    'test, expectation',
    [
        (["U2", "D2"], {(0, 0)}),
    ]
)
def test_xrayed(test, expectation):
    pytest.fail("derp")