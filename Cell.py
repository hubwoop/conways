import GameBoard
from collections import namedtuple

Fates = namedtuple('Fates', ['dies', 'lives'])
FATES = Fates(False, True)


class Cell:

    def __init__(self, board: GameBoard, x: int, y: int):
        self.alive = False
        self.x = x
        self.y = y
        self.game = board
        self.fate = None

    def living_neighbours(self) -> int:
        neighbours_alive = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                neighbour = self.game.get_cell(self.x + x, self.y + y)
                if not x == y == 0 and neighbour.alive:
                    neighbours_alive += 1
        return neighbours_alive

    def decide_fate(self) -> None:
        if self.living_neighbours() == 3:
            self.fate = FATES.lives
        elif self.living_neighbours() < 2:
            self.fate = FATES.dies
        elif self.living_neighbours() > 3:
            self.fate = FATES.dies
        else:
            self.fate = self.alive
