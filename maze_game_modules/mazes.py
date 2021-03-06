import numpy as np

# Some temporary mazes until I decide to implement a 3D generator.
maze_0 = np.array([[[0, 2, 0, 1, 1, 1, 1],
                    [0, 1, 1, 0, 0, 0, 1],
                    [1, 1, 1, 0, 0, 0, 1],
                    [0, 1, 0, 0, 1, 0, 1],
                    [0, 1, 1, 0, 1, 0, 1],
                    [0, 1, 0, 1, 1, 0, 1],
                    [0, 1, 1, 1, 1, 1, 1]],

                   [[0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0],
                    [0, 0, 1, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]],

                   [[0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]],

                   [[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 0]],

                   [[0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 1, 0],
                    [0, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0],
                    [1, 0, 0, 1, 0, 0, 0],
                    [1, 1, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]],

                   [[0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 3, 0, 1, 1, 0],
                    [0, 0, 1, 0, 0, 0, 0]],

                   [[0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0],
                    [0, 1, 0, 1, 1, 1, 0],
                    [0, 1, 1, 0, 0, 0, 0]]])

maze_1 = np.array([[[1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 0],
                    [2, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]],
                   [[0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]],
                   [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 3],
                    [0, 0, 1, 1, 1]]])

maze_2 = np.array([[[0, 0, 1, 1, 1],
                    [0, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0]],
                   [[0, 0, 1, 0, 1],
                    [0, 0, 1, 0, 1],
                    [0, 1, 2, 0, 1],
                    [0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0]],
                   [[1, 0, 0, 3, 0],
                    [1, 0, 0, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0]]])

maze_3 = np.array([[[0, 1, 1, 0, 0],
                    [0, 0, 1, 2, 0],
                    [1, 1, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0]],
                   [[0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 1],
                    [1, 1, 0, 1, 1],
                    [1, 0, 0, 1, 0],
                    [1, 0, 1, 1, 0]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 0, 1, 1],
                    [1, 1, 0, 0, 1],
                    [0, 0, 1, 0, 1],
                    [1, 1, 1, 0, 3]]])

maze_4 = np.array([[[2, 0, 0, 0, 0],
                    [1, 1, 0, 1, 0],
                    [0, 0, 1, 1, 0],
                    [0, 3, 1, 0, 0],
                    [0, 0, 0, 0, 0]],
                   [[0, 1, 1, 0, 0],
                    [0, 1, 0, 1, 1],
                    [1, 1, 0, 0, 1],
                    [0, 0, 1, 1, 0],
                    [1, 1, 1, 0, 0]],
                   [[0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 1],
                    [1, 0, 1, 1, 1]]])

# A tuple for easy accessing through indexing.
maze_tuple = (maze_0, maze_1, maze_2, maze_3, maze_4)
