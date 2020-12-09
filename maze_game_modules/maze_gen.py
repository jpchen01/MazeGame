import numpy as np
import random


class MazeGen:
    size_dict = {
        'small': (1, 3, 3),
        'medium': (3, 5, 5),
        'large': (5, 10, 10),
        'giant': (7, 15, 15),
    }

    def __init__(self, size):
        """Creates a 3D np array to use as a board. Uses default sizes to make
        my life easier

        Parameters
        ----------
        size : string
            Valid inputs small, medium, large, giant. Sets preset size for maze so
            I can actually attempt to code it.
        """

        height, length, width = self.size_dict[size]
        self.board = np.ones(shape=(height, length, width))

    def generate_start_end_points(self):
        """Adds start and end points to the maze, ideally on different places
        on the lowest and highest floors respectively.
        """
        # Gets dimensions of board
        shape = self.board.shape
        start_length = random.randint(0, shape[1]-1)
        start_width = random.randint(0, shape[2]-1)

        end_length = random.randint(0, shape[1]-1)
        end_width = random.randint(0, shape[2]-1)

        # print(0, start_length, start_width)
        # print(shape[0]-1, end_length, end_width)

        self.board[0, start_length, start_width] = 2
        self.board[shape[0]-1, end_length, end_width] = 3

    def floor_to_maze(self, floor_num):
        pass

    def add_wall(self, orientation):
        """Adds a wall in the specified orientation
        Parameters
        ----------
        orientation : string
            Adds a wall to the specified orientation on the board
        """
        pass

    def check_valid_index(self, index_tuple):
        """Takes in the board and a location, if valid, return True.
        Parameters
        ----------
        index_tuple: tuple
            Tuple of ints specifying indexes of a possible position in board.

        Returns
        -------
        bool
            True if square is valid location, else False.
        """
        try:
            # unpack index_tuple
            height, length, width = index_tuple
            # if it throws an error, return false
            self.board[height, length, width]
            return True
        except IndexError:
            return False


def generate_maze(size):
    """Creates a maze.
    """
    maze = MazeGen(size)
    print(maze.board)


if __name__ == '__main__':
    generate_maze('small')
