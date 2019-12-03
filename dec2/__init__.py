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

    def execute(self):
        instruction_pointer = 0
        halt = False
        while not halt:
            instructions = list(chunks(self.core, 4))
            try:
                instruction, parameter1, parameter2, parameter3 = instructions[instruction_pointer]
                if instruction is 1:
                    result = self.core[parameter1] + self.core[parameter2]
                    self.core[parameter3] = result
                elif instruction is 2:
                    result = self.core[parameter1] * self.core[parameter2]
                    self.core[parameter3] = result
                elif instruction is 99:
                    halt = True
                instruction_pointer = instruction_pointer + 1
            except ValueError:
                if self.core[instruction_pointer][0] is 99:
                    halt = True

    def core_dump(self):
        return ",".join([str(intcode) for intcode in self.core])



