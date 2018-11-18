from time import sleep
from GameBoard import GameBoard


def add_glider(game) -> GameBoard:
    game.get_cell(1, 0).alive = True
    game.get_cell(2, 1).alive = True
    game.get_cell(0, 2).alive = True
    game.get_cell(1, 2).alive = True
    game.get_cell(2, 2).alive = True
    return game


if __name__ == '__main__':
    a_game = GameBoard(8)
    a_game = add_glider(a_game)
    for i in range(50):
        print(a_game)
        sleep(1)
        a_game.progress()


