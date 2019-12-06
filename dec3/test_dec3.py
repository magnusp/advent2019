import functools
import itertools
from collections import defaultdict

import pytest
import dec3

@pytest.mark.parametrize(
    'test, expectation',
    [
        (('R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'), 610),
        (('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'), 410),
    ]
)
def test_santas_solver_works(test, expectation):
    wiring1, wiring2 = test
    layout1 = dec3.make_vector_ranges(wiring1)
    dec3.build(layout1)
