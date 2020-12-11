import sys

import numpy as np
from PyQt5 import QtWidgets, QtCore

from maze_game_modules import maze_game


def test_get_position():
    """Tests for MazeGame.get_position() method."""
    # Sets up fresh game object
    game = get_maze_game_object()
    game.maze = np.zeros([5, 5, 5])

    # Sets up starting and end positions respectively.
    game.maze[1, 1, 1] = 2
    game.maze[4, 4, 4] = 3

    assert callable(game.get_position)
    assert isinstance(game.get_position('start'), tuple)

    # Seeing if function can find the assigned start position
    assert game.get_position('start') == (1, 1, 1)
    # Sanity check to make sure not all inputs are valid
    assert game.get_position('start') != (1, 2, 3)

    # Seeing if function can find the assigned end position
    assert game.get_position('end') == (4, 4, 4)
    # Sanity to check to make sure not all inputs are valid
    assert game.get_position('end') != (4, 2, 1)


def test_get_absolute_position():
    """Tests for MazeGame.get_absolute_position method"""
    # Sets up fresh game object
    game = get_maze_game_object()
    game.maze = np.zeros([5, 5, 5])
    game.current_position = (2, 2, 2)
    game.current_direction = 'North'

    assert callable(game.get_absolute_positions)

    abs_pos_dict = game.get_absolute_positions()

    assert isinstance(abs_pos_dict, dict)

    # Verify all 6 directions behave as intended
    assert all(abs_pos_dict['left'] == np.array([2, 2, 1]))
    assert all(abs_pos_dict['up'] == np.array([3, 2, 2]))
    assert all(abs_pos_dict['forward'] == np.array([2, 1, 2]))
    assert all(abs_pos_dict['right'] == np.array([2, 2, 3]))
    assert all(abs_pos_dict['down'] == np.array([1, 2, 2]))
    assert all(abs_pos_dict['backward'] == np.array([2, 3, 2]))


def test_check_valid_square():
    """Tests for maze_game.update_position.check_valid_square
    function.
    """
    # Sets up fresh game object
    game = get_maze_game_object()
    game.maze = np.zeros([5, 5, 5])
    game.current_position = (2, 2, 2)
    game.current_direction = 'North'

    game.maze[2, 2, 2] = 2
    game.maze[2, 1, 2] = 1

    assert callable(game.check_valid_square)
    assert isinstance(game.check_valid_square((0, 0, 0)), bool)

    # Checks starting position and pathways are valid (2 and 1 in matrix).
    assert game.check_valid_square((2, 2, 2))
    assert game.check_valid_square((2, 1, 2))

    # Check a wall is not valid (0).
    assert not game.check_valid_square((2, 3, 2))


def test_get_dimensions():
    """Tests for maze_game.update_position.get_shape() function."""
    game = get_maze_game_object()

    game.maze = np.zeros(shape=[3, 4, 5])

    assert callable(game.get_dimensions)
    assert isinstance(game.get_dimensions(), tuple)

    # Checks if function returns desired shapes
    assert game.get_dimensions() == (3, 4, 5)

    game.maze = np.zeros(shape=[1, 1, 1])
    assert game.get_dimensions() == (1, 1, 1)


def get_maze_game_object():
    """Variation on the maze_game.run_game() function, to get access to a
    MazeGame object without crashing everything because of its special
    circumstances or starting a window and getting in an infinite loop.
    """
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    # Creates a new UI window using the MazeGame object
    window = maze_game.MazeGame()

    return window


if __name__ == '__main__':
    test_get_position()
    test_get_absolute_position()
    test_check_valid_square()
    test_get_dimensions()
