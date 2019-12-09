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
def test_is_valid_matcher(test, expectation):
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
    assert dec4.santa_ripper(start, stop, dec4.is_valid) == expectation

@pytest.mark.parametrize(
    'test, expectation',
    [
        (111111, False),
        (223450, False),
        (123789, False),
        (112233, True),
        (123444, False),
        (111122, True),
        (699999, False),
    ]
)
def test_is_valid_extended(test, expectation):
    assert dec4.is_valid_extended(test) == expectation