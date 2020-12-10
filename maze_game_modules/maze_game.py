import sys
import os
from functools import partial

import numpy as np
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap

from maze_game_modules.mazes import maze_1


class MazeGame(QtWidgets.QWidget):
    """Class that hooks up the GUI event loop and hold functionality for
    running a maze game.

    Attributes
    ----------
    maze_dict : dict
        Dictionary that maps words to represent aspects of maze array
    direction_dict : dict
        Dictionary that holds the relative right and forwards coordinates of
        each cardinal direction.
    image_pos : dict
        Dictionary that holds the row and column positions of images that need
        to be swapped out,
    temp_maze : np.array
        Temporary maze to help me test.

    Methods
    -------
    __init__()
        Loads and imports all GUI elements as class instance objects, calls
        setup_ui function, connects the buttons to the update_position
        function.

    get_position(find_cell)
        Returns either start or end position as a tuple.

    setup_ui()
        Since UI objects are added when the GUI is loaded, this function
        organizes these things.

    generate_maze(length, width, height)
        Returns a 3D maze that is just hardcoded for now.

    update_position(button)
        Slot for the GUI buttons, updates current position, direction and
        visuals after a button is pressed.

    update_direction(button)
        Helper function for update_position, changes the direction if the
        pressed button was used to turn.

    update_visual()
        Checks player's surroundings and renders images to depict open/closed
        walls.

    get_absolute_positions()
        Returns a dictionary of absolute positions around the current position.

    check_valid_square(coord)
        Checks if input square is a position that the player can move to.

    update_label_text()
        Prints some useful player information to screen.

    check_win()
        Prints to screen that the player has won.
    """

    # Define words as numbers for readability
    maze_dict = {'wall': 0, 'open': 1, 'start': 2, 'end': 3}

    # direction coordinates of (left, forwards) relative to matrix respectively
    direction_dict = {'North': ((0, 0, -1), (0, -1, 0)),
                      'East': ((0, -1, 0), (0, 0, 1)),
                      'South': ((0, 0, 1), (0, 1, 0)),
                      'West': ((0, 1, 0), (0, 0, -1),)}

    # Positions of images that changes in a 3x3 grid that need to be changed
    # depending on which path is open or not (grid needs to be generated later)
    image_pos = dict(up=(0, 1), left=(1, 0), forward=(1, 1), right=(1, 2),
                     down=(2, 1))

    def __init__(self):
        """Starts the game object, loads in the .ui file and and sets up
        """

        # Set up GUI portion of the code
        super(MazeGame, self).__init__()
        self.module_path = os.path.dirname(__file__)
        ui_rel_path = '../maze_gui.ui'
        abs_ui_path = os.path.join(self.module_path, ui_rel_path)
        uic.loadUi(abs_ui_path, self)  # Adds ui and widgets to class instance.

        self.buttons_dict = {}  # Dictionary of press-able buttons.
        self.image_grid = ()  # 3x3 Tuple of references to image displays.
        self.image_strings = {}  # Stores positions and file paths to images.

        self.setup_ui()  # Populates above data structures.
        self.steps = 0  # Counter for number of player actions

        # Connect GUI buttons to functions using signal/slot system.
        for button in self.buttons_dict:
            # Uses partial to pass a parameter to a slot function.
            # Cannot pass a function parameter otherwise.
            button.clicked.connect(partial(self.update_position, button))

        # Set up the game and stores essential information.

        self.maze = self.generate_maze()
        self.current_position = self.get_position('start')
        self.end_position = self.get_position('end')
        self.current_direction = 'North'
        self.dimension = self.get_dimensions()

        self.update_visual()

    def get_position(self, find_cell):
        """Finds the start/end position of the maze.

        Parameters
        ----------
        find_cell : string
            Key to self.maze_dict, used to find the start or end position of
            the maze.

        Returns
        -------
        tuple
            The indexes of the start position in the 3D maze matrix.
        """
        pos_tuple = np.where(self.maze == self.maze_dict[find_cell])
        return pos_tuple[0][0], pos_tuple[1][0], pos_tuple[2][0]

    def setup_ui(self):
        """Creates both static dictionaries that are dependent on the .ui file
        that does not exist before the uic.LoadUi() method is called.

        self.buttons_dict : dictionary
            Links buttons to strings that can be passed as function parameters.

        self.image_strings : dictionary
            Stores path to image files, with the key being the position the
            image corresponds to in the array of labels used to display show
            the pictures (self.image_grid).

        self.image_grid : tuple
            Tuple of tuples to store the 3x3 coordinates of the Qt widgets used
            to present the image.
        """
        self.buttons_dict = {self.button_down: 'down',
                             self.button_forwards: 'forward',
                             self.button_up: 'up',
                             self.button_left: 'left',
                             self.button_backwards: 'backward',
                             self.button_right: 'right',
                             self.button_turn_left: 'turn_left',
                             self.button_turn_right: 'turn_right'}
        # Strings for file paths to different images with matrix index as key.
        self.image_strings = {'10': ('../images/open2_1.jpg',
                                     '../images/square2_1.jpg'),
                              '12': ('../images/open2_3.jpg',
                                     '../images/square2_3.jpg'),
                              '01': ('../images/open1_2.jpg',
                                     '../images/square1_2.jpg'),
                              '21': ('../images/open3_2.jpg',
                                     '../images/square3_2.jpg'),
                              '11': ('../images/open2_2.jpg',
                                     '../images/square2_2.jpg')}

        # Creates array of labels to display images
        self.image_grid = ((self.image_11, self.image_12, self.image_13),
                           (self.image_21, self.image_22, self.image_23),
                           (self.image_31, self.image_32, self.image_33))

    def generate_maze(self):
        """Magically creates a maze, though I might not have time to finish,
        so it temporarily returns a hard coded one for testing.

        Parameters
        ----------
        length : int
            Length of the maze
        width : int
            Width of the maze
        height : int
            Height of the maze

        Returns
        -------
        numpy.array
            A 3D matrix representing the maze, refer to self.maze_dict for
            what each value represents
        """
        # return self.temp_maze
        return maze_1

    def update_position(self, button):
        """A slot for the buttons that runs whenever a button is pressed.
        If the button is a turning command, it updates the direction. If the
        button is a directional movement button, then it will attempt to move
        in that direction, and remain in position if it fails.
        Update visuals after it's complete.

        Parameters
        ----------
        button : QPushButton
            Connects the specified button to the function and does movement
            depending on the button.
        """

        # Pressed button is for changing direction
        if self.buttons_dict[button] in ['turn_left', 'turn_right']:
            self.update_direction(button)

        # Pressed button is for movement
        else:
            # Gets a dictionary of the absolute position and if the direction
            # associated with the button is available, move to that location.
            abs_coord = self.get_absolute_positions()
            square_to_move = abs_coord[self.buttons_dict[button]]
            if self.check_valid_square(square_to_move):
                self.current_position = square_to_move

        # Increments step count and updates
        self.steps += 1
        self.update_visual()

    def update_direction(self, button):
        """Using the current direction, turns left or right depending on which
        button was pressed.

        Parameters
        ----------
        button : QPushButton
            The directional changing button that was just pressed.
        """

        # Get a list of cardinal directions in clockwise order
        cardinal_directions = list(self.direction_dict.keys())
        # Get index of the current direction
        direction_index = cardinal_directions.index(self.current_direction)

        # Shifts current direction by 1 index from the directions list
        # depending which direction to turn.
        if self.buttons_dict[button] == 'turn_left':
            self.current_direction = cardinal_directions[
                direction_index - 1]
        else:
            # rotates temporary list and use the same index
            cardinal_directions.append(cardinal_directions.pop(0))
            self.current_direction = cardinal_directions[direction_index]

    def update_visual(self):
        """Updates visuals by changing the squares that give the illusion of
        depth and update the labels. Called every time player issues movement
        commands.
        """
        abs_coord = self.get_absolute_positions()

        # Updates direction for each of 5 changeable squares
        for direction in self.image_pos:
            # Gets coordinates of image associated with that direction
            row = self.image_pos[direction][0]
            col = self.image_pos[direction][1]

            new_square = abs_coord[direction]
            # Picks open or closed image path depending on is square is valid.
            if self.check_valid_square(new_square):
                rel_img_path = self.image_strings[str(row) + str(col)][0]
            else:
                rel_img_path = self.image_strings[str(row) + str(col)][1]

            # Joins the paths and updates desired square.
            image_path = os.path.join(self.module_path, rel_img_path)
            self.image_grid[row][col].setPixmap(QPixmap(image_path))

        # Updates the text at the bottom
        self.update_labels_text()

        # Check win
        self.check_win()

    def get_absolute_positions(self):
        """Returns a dictionary of the coordinates around the current position,
        taking current direction into consideration.

        Returns
        -------
        abs_coord : dict
            Dictionary of the absolute directions around the current position.
        """
        # Uses direction to get relative directions
        rel_coord = dict(left=self.direction_dict[self.current_direction][0],
                         forward=self.direction_dict[self.current_direction][
                                                     1],
                         up=(1, 0, 0),
                         down=(-1, 0, 0))

        # Adds backward and right coordinate to dictionary by reversing known
        # every relative coordinate from forward and left respectively
        rel_coord['backward'] = [-coord for coord in rel_coord['forward']]
        rel_coord['right'] = [-coord for coord in rel_coord['left']]

        # Creates dictionary of absolute positions
        abs_coord = {}
        for keys in rel_coord.keys():
            abs_coord[keys] = np.add(rel_coord[keys], self.current_position)

        return abs_coord

    def check_valid_square(self, coord):
        """Checks if the specified square is a wall or not and is within the
        maze.

        Parameters
        ----------
        coord : tuple
            A position in the maze

        Returns
        -------
        bool
            True is the value in that square is not 0 and in the maze, false if
            invalid or is a wall.
        """

        # Using try, except to make sure indexing out of bounds doesn't crash
        # the program.
        try:
            check_lower_bound = all(coord_part >= 0 for coord_part in coord)
            comp_zip = zip(coord, self.dimension)
            check_upper_bound = all(coord_dim < dim for coord_dim, dim
                                    in comp_zip)
            check_not_wall = self.maze[coord[0], coord[1], coord[2]] != 0
            return all([check_not_wall, check_upper_bound, check_lower_bound])

        except IndexError:
            return False

    def update_labels_text(self):
        """Shows the player important positional information."""
        self.label_steps.setText('Steps: ' + str(self.steps))
        self.label_coordinates.setText('(X,Y,Z):' + str(self.current_position))
        self.label_direction.setText('Direction: '
                                     + str(self.current_direction))

    def check_win(self):
        """Checks if player has won and prints message to screen"""

        # Set center image to string
        if tuple(self.current_position) == self.end_position:
            self.image_grid[1][1].setText("You Win!")

    def get_dimensions(self):
        """Gets the dimensions of the maze
        Returns
        -------
        tuple
            The dimension of the given maze (height, length, width)
        """
        return self.maze.shape


def run_game():
    """Creates a version of the game object to start the ui, does a check to
    see if there's already an instance so it doesn't crash the Jupyter
    Notebook kernel if the cell is rerun.
    """
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    # Creates a new UI window using the MazeGame object
    window = MazeGame()
    window.show()

    # Starts event loop, so GUI runs until you exit it.
    app.exec_()
    return window


if __name__ == '__main__':
    run_game()
