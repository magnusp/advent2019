from dec2 import SantaVM
import pytest


@pytest.mark.parametrize(
    'input, expectation',
    [
        ("1,0,0,0,99", "2,0,0,0,99"),
        ("2,3,0,3,99", "2,3,0,6,99"),
        ("2,4,4,5,99,0", "2,4,4,5,99,9801"),
        ("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")
    ]
)
def test_expectations(input, expectation):
    vm = SantaVM(input)
    vm.run()
    assert expectation == vm.core_dump()


def test_off_by_one():
    input = "2,4,4,5,99,0"
    expectation = "2,4,4,5,99,9801"
    vm = SantaVM(input)
    vm.run()
    assert expectation == vm.core_dump()