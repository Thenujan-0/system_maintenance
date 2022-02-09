from PyQt5 import QtCore , QtGui ,QtWidgets,uic

from time import sleep
import subprocess
import sys
import os

PATH= os.path.dirname(os.path.realpath(__file__))


class MirrorsUi(QtGui.QWidget):
    def __init__(self):
        super(Mirrors, self).__init__()
        uic.loadUi(f"{PATH}/mirrors.ui",self)

if __name__ == "__main__":
    app= QtWidgets.QApplication(sys.argv)
    window=MirrorsUi()
    window.show()
    app.exec_()

