from .operations import addition
from enum import Enum

class Operation(Enum):
    ADDITION = 0

def calculator(op, *args):
    if op == Operation.ADDITION:
        return addition(*args)
