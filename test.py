import unittest
from GameBoard import GameBoard


class TestGameRules(unittest.TestCase):

    def test_birth(self):
        game = GameBoard(5)
        game.get_cell(1, 1).alive = True
        game.get_cell(1, 2).alive = True
        game.get_cell(1, 3).alive = True
        game.progress()
        self.assertTrue(game.get_cell(0, 2).alive)

    def test_death_by_loneliness(self):
        game = GameBoard(5)
        game.get_cell(2, 2).alive = True
        game.get_cell(1, 2).alive = True
        game.progress()
        self.assertFalse(game.get_cell(2, 2).alive)

    def test_survive(self):
        game = GameBoard(5)
        test_cell = game.get_cell(2, 2)
        test_cell.alive = True
        game.get_cell(2, 1).alive = True
        game.get_cell(2, 3).alive = True
        game.progress()
        self.assertTrue(test_cell.alive)

    def test_death_by_overpopulation(self):
        game = GameBoard(5)
        test_cell = game.get_cell(2, 2)
        test_cell.alive = True
        game.get_cell(2, 3).alive = True
        game.get_cell(1, 2).alive = True
        game.get_cell(3, 3).alive = True
        game.get_cell(1, 1).alive = True
        game.progress()
        self.assertFalse(test_cell.alive)

    def test_count_one_neighbour(self):
        game = GameBoard(5)
        game.get_cell(0, 0).alive = True
        count = game.count_living_neighbours(game.get_cell(1, 1))
        self.assertEqual(1, count)

    def test_count_two_neighbours(self):
        game = GameBoard(5)
        game.get_cell(0, 0).alive = True
        game.get_cell(0, 1).alive = True
        count = game.count_living_neighbours(game.get_cell(1, 1))
        self.assertEqual(2, count)

    def test_count_four_neighbours(self):
        game = GameBoard(5)
        game.get_cell(0, 0).alive = True
        game.get_cell(0, 1).alive = True
        game.get_cell(0, 2).alive = True
        game.get_cell(1, 0).alive = True
        count = game.count_living_neighbours(game.get_cell(1, 1))
        self.assertEqual(4, count)

    def test_count_eight_neighbours(self):
        game = GameBoard(5)
        game.get_cell(0, 0).alive = True
        game.get_cell(0, 1).alive = True
        game.get_cell(0, 2).alive = True
        game.get_cell(1, 0).alive = True
        game.get_cell(1, 2).alive = True
        game.get_cell(2, 0).alive = True
        game.get_cell(2, 1).alive = True
        game.get_cell(2, 2).alive = True
        count = game.count_living_neighbours(game.get_cell(1, 1))
        self.assertEqual(8, count)


