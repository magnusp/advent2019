import itertools
from typing import List


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class SantaVM:
    def __init__(self, punchcard: str) -> None:
        super().__init__()
        self.core = [int(code) for code in punchcard.split(",")]

    def execute(self, input1: int = None, input2: int = None):
        if input1 is not None:
            self.core[1] = input1

        if input2 is not None:
            self.core[2] = input2

        def add(value1_ref, value2_ref):
            return self.core[value1_ref] + self.core[value2_ref]

        def mul(value1_ref, value2_ref):
            return self.core[value1_ref] * self.core[value2_ref]

        for instruction_pointer in range(0, len(self.core), 4):
            try:
                instruction, parameter1, parameter2, parameter3 = self.core[instruction_pointer:instruction_pointer + 4]
                if instruction is 1:
                    result = add(parameter1, parameter2)
                    self.core[parameter3] = result
                elif instruction is 2:
                    result = mul(parameter1, parameter2)
                    self.core[parameter3] = result
                elif instruction is 99:
                    break
            except ValueError:
                if self.core[instruction_pointer] is 99:
                    break

    def core_dump(self):
        return ",".join([str(intcode) for intcode in self.core])
