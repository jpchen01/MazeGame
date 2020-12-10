import sys

import numpy as np
from PyQt5 import QtWidgets, QtCore

from maze_game_modules import maze_game


def test_get_position():
    """Tests for MazeGame.get_position() method."""
    # Sets up game object
    game = get_maze_game_object()
    game.maze = np.zeros([5, 5, 5])

    # Seeing if function can find the assigned start position
    game.maze[1, 1, 1] = 2
    assert game.get_position('start') == (1, 1, 1)
    # Sanity check to make sure not all inputs are valid
    assert game.get_position('start') != (1, 2, 3)

    # Seeing if function can find the assigned end position
    game.maze[4, 4, 4] = 3
    assert game.get_position('end') == (4, 4, 4)
    # Sanity to check to make sure not all inputs are valid
    assert game.get_position('end') != (4, 2, 1)


def test_get_absolute_position():
    """Tests for MazeGame.get_absolute_position method"""
    # Sets up current
    game = get_maze_game_object()
    game.maze = game.maze = np.zeros([5, 5, 5])
    game.current_position = (2, 2, 2)
    game.current_direction = 'North'

    abs_pos_dict = game.get_absolute_positions()

    # Verify all 6 directions behave as intended
    assert all(abs_pos_dict['left'] == np.array([2, 2, 1]))
    assert all(abs_pos_dict['up'] == np.array([3, 2, 2]))
    assert all(abs_pos_dict['forward'] == np.array([2, 1, 2]))
    assert all(abs_pos_dict['right'] == np.array([2, 2, 3]))
    assert all(abs_pos_dict['down'] == np.array([1, 2, 2]))
    assert all(abs_pos_dict['backward'] == np.array([2, 3, 2]))


def test_update_position():
    """Tests for maze_game.update_position function, very broken."""
    game = maze_game.MazeGame()
    game.maze = game.maze = np.zeros([5, 5, 5])
    game.current_position = (2, 2, 2)
    game.current_direction = 'North'

    button = game.button_forwards
    game.update_position(button)
    assert all(game.current_position == np.array([2, 1, 2]))
    print('runs')


def test_update_direction():
    """Tests for maze_game.update_direction"""
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


def get_maze_game_object():
    """Variation on the maze_game.run_game() function, to get access to a
    MazeGame object without crashing everything because of it's special
    circumstances.
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
    test_update_direction()
    # test_update_position()
