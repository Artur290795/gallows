from enum import Enum


class GuessResult(Enum):
    CORRECT = 1
    INCORRECT = 2
    ALREADY_USED = 3
    INVALID = 4
    WIN = 5
    LOSE = 6
