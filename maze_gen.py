from PyQt5 import QtWidgets, uic
import sys


class MazeGen(QtWidgets.QWidget):

    temp_maze = np.array([[[2, 1, 0, 0, 0],
                           [0, 1, 0, 0, 0],
                           [0, 1, 0, 1, 0],
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

    def __init__(self):
        super(MazeGen, self).__init__()
        uic.loadUi('maze_gui.ui', self)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MazeGen()
    app.exec_()
