import itertools
from typing import List

class SantaVM:
    def __init__(self, punchcard: str) -> None:
        super().__init__()
        self.core = [int(code) for code in punchcard.split(",")]
        self.opCodes = []
        buffer = []

        for intcode in self.core:
            if intcode is 99 and len(self.opCodes) is 0:
                self.opCodes.append(OpCode(self, buffer))
                self.opCodes.append(OpCode(self, [99]))
            elif intcode is 99 and self.opCodes[-1].is_instruction():
                self.opCodes.append(OpCode(self, buffer))
                self.opCodes.append(OpCode(self, [99]))
                buffer.clear()
            else:
                buffer.append(intcode)
        self.opCodes.append(OpCode(self, buffer))

    def __getitem__(self, item):
        return self.core[item]

    def run(self):
        try:
            [opCode() for opCode in self.opCodes]
        except StopIteration:
            pass

    def core_dump(self):
        return ','.join([str(intcode) for intcode in self.core])


class OpCode:
    def __init__(self, vm: SantaVM, value: List[int]) -> None:
        super().__init__()
        self.vm = vm
        self.value = value[:]

    def is_instruction(self):
        if self.value[0] is 99:
            return True
        return len(self.value) == 4

    def __call__(self, *args, **kwargs):
        if self.value[0] is 1:
            return self.execute_addition(self.value[1], self.value[2], self.value[3])
        elif self.value[0] is 2:
            return self.execute_multiplication(self.value[1], self.value[2], self.value[3])
        elif self.value[0] is 99:
            raise StopIteration
        raise RuntimeError(f"{self.value[0]}: not acceptable")

    def __repr__(self) -> str:
        return repr(self.value)

    def execute_addition(self, value1_location, value2_location, result_reference):
        result = self.vm.core[value1_location] + self.vm.core[value2_location]
        self.vm.core[result_reference] = result

    def execute_multiplication(self, value1_location, value2_location, result_reference):
        result = self.vm.core[value1_location] * self.vm.core[value2_location]
        self.vm.core[result_reference] = result
