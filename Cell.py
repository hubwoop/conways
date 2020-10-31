import GameBoard
from collections import namedtuple

Fates = namedtuple('Fates', ['dies', 'lives'])
FATES = Fates(False, True)


class Cell:

    def __init__(self, x: int, y: int):
        self.alive = False
        self.x = x
        self.y = y
        self.fate = None

    def decide_fate(self, living_neighbours: int) -> None:
        if living_neighbours == 3:
            self.fate = FATES.lives
        elif living_neighbours < 2 or living_neighbours > 3:
            self.fate = FATES.dies
        else:
            self.fate = self.alive
