import os
import sys
import numpy as np
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap


class MazeGen(QtWidgets.QWidget):
    # Define words as numbers for readability

    maze_dict = {'wall': 0, 'open': 1, 'start': 2, 'end': 3}
    # direction coordinates of (left, forwards) relative to matrix respectively
    direction_dict = {'North': ((0, 0, -1), (0, -1, 0), (0, 0, 1)),
                      'South': ((0, 0, 1), (0, -1, 0), (0, 0, -1)),
                      'East': ((0, -1, 0), (0, 0, 1), (0, -1, 0)),
                      'West': ((0, 1, 0), (0, 0, -1), (0, 1, 0))}
    temp_maze = np.array([[[0, 1, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 0, 1, 1, 1],
                           [0, 1, 0, 1, 0],
                           [0, 0, 0, 0, 0]],
                          [[0, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0],
                           [0, 1, 2, 0, 0],
                           [1, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0]],
                          [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 3],
                           [0, 0, 0, 0, 0]]])

    def __init__(self, length, width, height):
        # Set up GUI portion of the code
        super(MazeGen, self).__init__()
        uic.loadUi('maze_gui.ui', self)  # Adds widgets to class instance
        self.buttons_dict = {}
        self.image_grid = ()
        self.image_strings = {}
        self.setup_ui()  # Populates above data structures.

        # Connect GUI buttons to functions using signal/slot system
        for button in self.buttons_dict:
            button.clicked.connect(self.update_position)

        # Set up the game
        self.maze = self.generate_maze(length, width, height)
        self.current_position = self.get_start_position()
        self.current_direction = 'West'
        self.update_visual()
        # self.show()  # Displays the GUI

    def get_start_position(self):
        """Finds the starting position of the maze.

        Returns
        -------
        tuple
            The indexes of the start position in the 3D maze matrix.
        """
        pos_tuple = np.where(self.maze == self.maze_dict['start'])
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
                             self.button_forwards: 'forwards',
                             self.button_up: 'up',
                             self.button_left: 'left',
                             self.button_backwards: 'backwards',
                             self.button_right: 'right',
                             self.button_turn_left: 'turn_left',
                             self.button_turn_right: 'turn_right'}
        # Strings for file paths to different images with matrix index as key.
        self.image_strings = {'10': ('images/open2_1.jpg',
                                     'images/square2_1.jpg'),
                              '12': ('images/open2_3.jpg',
                                     'images/square2_3.jpg'),
                              '01': ('images/open1_2.jpg',
                                     'images/square1_2.jpg'),
                              '21': ('images/open3_2.jpg',
                                     'images/square3_2.jpg'),
                              '11': ('images/open2_2.jpg',
                                     'images/square2_2.jpg')}

        # Creates array of labels to display images
        self.image_grid = ((self.image_11, self.image_12, self.image_13),
                           (self.image_21, self.image_22, self.image_23),
                           (self.image_31, self.image_32, self.image_33))

    def generate_maze(self, length, width, height):
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
        return self.temp_maze

    def update_position(self):
        pass

    def update_visual(self):
        """Is called every time the player makes a valid movement.
        The function holds 2 dictionaries and a local function and uses them to
        present the player with an accurate representation of the matrix in
        a first person perspective.

        rel_coord
            It uses the current direction to determine what the matrix looks
            like in a first person view and stores it in a dictionary with
            the relative directions as keys

        image_pos
            A dictionary using the same key values as rel_coord that stores the
            positions of the labels/images in self.image_grid that need to be
            modified depending on the direction.
        """

        rel_coord = dict(left=self.direction_dict[self.current_direction][0],
                         forward=self.direction_dict[self.current_direction][
                             1],
                         right=self.direction_dict[self.current_direction][2],
                         up=(1, 0, 0), down=(-1, 0, 0))
        image_pos = dict(up=(0, 1), left=(1, 0), forward=(1, 1), right=(1, 2),
                         down=(2, 1))

        def update_directional_view(relative_direction):
            """Update the image in the specified relative direction. It works
            by finding the coordinate of the square in the relative direction
            and check for the value, if it's value is equal to 1 and not out of
            bounds, it will display an open square, or it will display a wall.

            Parameters
            ----------
            relative_direction : string
                It takes the string keys of the two dictionaries which specify
                one of five relative directions that the function needs to
                change the image for. Valid inputs are up, left, forward,
                right, down as strings.
            """

            new_coord = np.add(rel_coord[relative_direction],
                               self.current_position)

            row = image_pos[relative_direction][0]
            col = image_pos[relative_direction][1]

            if self.maze[new_coord[0], new_coord[1], new_coord[2]] != 0 \
                    and not any(coord < 0 for coord in new_coord):

                self.image_grid[row][col].setPixmap(QPixmap(
                                   self.image_strings[str(row) + str(col)][0]))
            else:
                self.image_grid[row][col].setPixmap(QPixmap(
                                   self.image_strings[str(row) + str(col)][1]))

        for direction in image_pos:
            update_directional_view(direction)


def run_game():
    """Creates a version of the game object to start the ui, does a check to
    see if there's already an instance so it doesn't crash the Jupyter
    Notebook kernel if a cell is rerun.
    """
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    window = MazeGen(5, 5, 3)
    window.show()
    print(window.current_position)
    app.exec_()


run_game()
