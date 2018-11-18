from typing import List
import Cell


class GameBoard:

    def __init__(self, size: int):
        self.size = size
        self.board = [[Cell.Cell(self, x, y) for x in range(size)] for y in range(size)]
        self.flat_board = [item for row in self.board for item in row]

    def get_cell(self, x, y) -> Cell.Cell:
        return self.board[y % self.size][x % self.size]

    def progress(self) -> None:
        self.decide_fates()
        self.fulfill_fates()

    def decide_fates(self) -> None:
        for cell in self.flat_board:
            cell.decide_fate()

    def fulfill_fates(self) -> None:
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

    def aggregate_symbols(self) -> List[List[str]]:
        return [['X' if self.get_cell(x, y).alive else '.'
                for x in range(self.size)]
                for y in range(self.size)]
