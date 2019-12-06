import pytest
import dec3

@pytest.mark.parametrize(
    'test, expectation',
    [
        (('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'), 159),
        (('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), 135),
    ]
)
def test_santas_nearest_solver_works(test, expectation):
    wiring1, wiring2 = test

    layout1 = dec3.build(dec3.make_vector_ranges(wiring1))
    layout2 = dec3.build(dec3.make_vector_ranges(wiring2))
    assert dec3.find_nearest_intersection(layout1, layout2) == expectation


@pytest.mark.parametrize(
    'test, expectation',
    [
        (('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'), 610),
        (('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), 410),
    ]
)
def test_santas_nearest_by_distance_travelled_solver_works(test, expectation):
    wiring1, wiring2 = test

    layout1 = dec3.build(dec3.make_vector_ranges(wiring1))
    layout2 = dec3.build(dec3.make_vector_ranges(wiring2))
    dec3.find_nearest_by_distance_travelled_intersection(layout1, layout2)
