from collections.__init__ import namedtuple
from time import sleep
Fates = namedtuple('Fates', ['dies', 'lives'])
FATES = Fates(False, True)


class GameBoard:

    def __init__(self, size: int):
        self.size = size
        self.board = [[Cell(self, x, y) for x in range(size)] for y in range(size)]
        self.flat_board = [item for row in self.board for item in row]

    def get_cell(self, x, y):
        return self.board[y % self.size][x % self.size]

    def progress(self):
        self.decide_fates()
        self.fulfill_fates()

    def decide_fates(self):
        for cell in self.flat_board:
            cell.decide_fate()

    def fulfill_fates(self):
        for cell in self.flat_board:
            cell.alive = cell.fate

    def __str__(self):
        symbols = self.aggregate_symbols()
        out = ''
        for row in symbols:
            for symbol in row:
                out += symbol
            out += '\n'
        return out

    def aggregate_symbols(self):
        return [['X' if self.get_cell(x, y).alive else '.'
                for x in range(self.size)]
                for y in range(self.size)]


class Cell:

    def __init__(self, game, x, y):
        self.alive = False
        self.x = x
        self.y = y
        self.game = game
        self.fate = None

    def living_neighbours(self) -> int:
        neighbours_alive = 0
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                neighbour = self.game.get_cell(self.x + x, self.y + y)
                if not x == y == 0 and neighbour.alive:
                    neighbours_alive += 1
        return neighbours_alive

    def decide_fate(self):
        if self.living_neighbours() == 3:
            self.fate = FATES.lives
        elif self.living_neighbours() < 2:
            self.fate = FATES.dies
        elif self.living_neighbours() > 3:
            self.fate = FATES.dies
        else:
            self.fate = self.alive


def add_glider(game):
    game.get_cell(1, 0).alive = True
    game.get_cell(2, 1).alive = True
    game.get_cell(0, 2).alive = True
    game.get_cell(1, 2).alive = True
    game.get_cell(2, 2).alive = True
    return game


if __name__ == '__main__':
    game = GameBoard(8)
    game = add_glider(game)
    for i in range(50):
        print(game)
        sleep(1)
        game.progress()


