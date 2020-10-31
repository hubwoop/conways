from time import sleep
from GameBoard import GameBoard


def add_glider(game) -> GameBoard:
    game.get_cell(1, 0).alive = True
    game.get_cell(2, 1).alive = True
    game.get_cell(0, 2).alive = True
    game.get_cell(1, 2).alive = True
    game.get_cell(2, 2).alive = True
    return game


def fancy_pattern(game) -> GameBoard:
    game.get_cell(15, 10).alive = True
    game.get_cell(15, 11).alive = True
    game.get_cell(15, 12).alive = True
    game.get_cell(16, 10).alive = True
    game.get_cell(17, 10).alive = True
    game.get_cell(17, 11).alive = True
    game.get_cell(17, 12).alive = True

    game.get_cell(15, 14).alive = True
    game.get_cell(15, 15).alive = True
    game.get_cell(15, 16).alive = True
    game.get_cell(16, 16).alive = True
    game.get_cell(17, 16).alive = True
    game.get_cell(17, 15).alive = True
    game.get_cell(17, 14).alive = True
    return game


def glider_demo():
    a_game = GameBoard(8)
    a_game = add_glider(a_game)
    for i in range(50):
        print(a_game)
        sleep(1)
        a_game.progress()


def fancy_pattern_demo():
    # https://de.wikipedia.org/wiki/Conways_Spiel_des_Lebens#Andere_Objekte
    a_game = GameBoard(33)
    a_game = fancy_pattern(a_game)
    for i in range(55):
        print(a_game)
        sleep(0.1)
        a_game.progress()


if __name__ == '__main__':
    glider_demo()
    # fancy_pattern_demo()


