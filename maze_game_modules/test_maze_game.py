import sys

import numpy as np
from PyQt5 import QtWidgets, QtCore

from maze_game_modules import maze_game


def test_get_position():
    """Tests for maze_game.get_position() function."""
    game = maze_game.run_game()
    print('runs')
    game.maze = np.zeros([5, 5, 5])
    print('runs')
    game.maze[1, 1, 1] = 2
    print(game.get_position('start'))
    assert game.get_position('start') == (1, 1, 1)

    game.maze[4, 4, 4] = 3
    assert game.get_position('end') == (4, 4, 4)


def test_update_position():
    """Tests for maze_game.update_position function."""
    pass


def test_check_relative_position():
    """Tests for maze_game.update_position.check_relative_position
    function.
    """
    pass


def test_update_visual():
    """Tests for maze_game.update_position() function."""
    pass


def test_update_directional_view():
    """Tests for maze_game.update_position.update_directional_view()
    function."""
    pass


# def get_maze_game_object():
#     """Variation on the maze_game.run_game() function, to get access to a
#     MazeGame object without crashing everything because of it's special
#     circumstances.
#     """
#     app = QtCore.QCoreApplication.instance()
#     if app is None:
#         app = QtWidgets.QApplication(sys.argv)
#     # Creates a new UI window using the MazeGame object
#     window = maze_game.MazeGame(5, 5, 3)
#     app.exec_()
#     return window


if __name__ == '__main__':
    test_get_position()
