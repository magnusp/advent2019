import pytest
import dec3


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
        (["U2", "U2"], {(0, 0), (0, 1), (0, 2)}),
        (["U2", "R1,U2,L1"], {(0, 0), (0, 2)}),
    ]
)
def test_xrayed(test, expectation):
    wiring1, wiring2 = test
    layout1 = dec3.setrogify_wiring(wiring1)
    layout2 = dec3.setrogify_wiring(wiring2)
    intersection = layout1.intersection(layout2)
    assert intersection == expectation

@pytest.mark.parametrize(
    'test, expectation',
    [
        ({(0, 0), (0, 1)}, 1),
        ({(0, 0), (0, 1), (0, 2)}, 1),
        ({(0, 0), (0, 2)}, 2),
    ]
)
def test_santas_solver_works(test, expectation):
    assert dec3.solve_for_santa(test) == expectation
