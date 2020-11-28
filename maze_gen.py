from PyQt5 import QtWidgets, uic
import sys
import numpy as np


class MazeGen(QtWidgets.QWidget):

    maze_dict = {'wall': 0, 'open': 1, 'start': 2, 'end': 3}
    direction_dict = {'North': 0, 'South': 1, 'East': 2, 'West': 3}

    temp_maze = np.array([[[0, 1, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [2, 1, 0, 1, 0],
                           [0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0]],
                          [[0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0],
                           [0, 1, 0, 1, 0],
                           [0, 1, 1, 1, 0],
                           [0, 0, 0, 0, 0]],
                          [[0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0],
                           [0, 1, 1, 1, 3],
                           [0, 0, 0, 0, 0]]])

    def __init__(self, length, width, height):
        # Set up GUI portion of the code
        super(MazeGen, self).__init__()
        uic.loadUi('maze_gui.ui', self)  # Loads all widgets of UI as
        self.buttons_dict = {self.button_down: 'down',
                             self.button_forwards: 'forwards',
                             self.button_up: 'up',
                             self.button_left: 'left',
                             self.button_backwards: 'backwards',
                             self.button_right: 'right',
                             self.button_turn_left: 'turn_left',
                             self.button_turn_right: 'turn_right'}

        # Connect GUI buttons to functions using signal/slot system
        for button in self.buttons_dict:
            button.clicked.connect(self.update_position)

        # Set up the game
        self.current_position = self.get_start_position()
        self.current_direction = self.direction_dict['North']
        self.maze = self.generate_maze(length, width, height)

        self.show()  # Displays the GUI

    def get_start_position(self):
        """Finds the starting position of the maze.

        Returns
        -------
        tuple
            The indexes of the start position in the 3D maze matrix.
        """
        pos_tuple = np.where(self.maze == self.maze_dict['start'])
        return pos_tuple[0][0], pos_tuple[1][0], pos_tuple[2][0]

    def generate_maze(self, length, width, height):
        return self.temp_maze

    def update_position(self):
        pass

    def update_visual(self):
        pass




def run_game():
    app = QtWidgets.QApplication(sys.argv)
    window = MazeGen()
    app.exec_()
    print(window.get_start_position())


run_game()

