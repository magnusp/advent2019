import pytest

import dec4


@pytest.mark.parametrize(
    'test, expectation',
    [
        (111111, True),
        (223450, False),
        (123789, False),
        (111123, True),
        (135679, False)
    ]
)
def test_santa_the_ripper_matcher(test, expectation):
    assert dec4.is_valid(test) == expectation

@pytest.mark.parametrize(
    'test, expectation',
    [
        ((111111, 111111), 1),
        ((111111, 111112), 2),
    ]
)
def test_range_makes_sense(test, expectation):
    start, stop = test
    assert dec4.santa_ripper(start, stop) == expectation