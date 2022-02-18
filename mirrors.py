from PyQt5 import QtCore , QtGui ,QtWidgets,uic

from time import sleep
import subprocess
import sys
import os

PATH= os.path.dirname(os.path.realpath(__file__))


class MirrorsUi(QtWidgets.QWidget):
    def __init__(self):
        super(MirrorsUi, self).__init__()
        uic.loadUi(f"{PATH}/ui/mirrors.ui",self)

        self.checkBox_limit_number_of_mirrors.clicked.connect(self.checkBox_limit_number_of_mirrors_callback)

    def checkBox_limit_number_of_mirrors_callback(self):
        if   self.checkBox_limit_number_of_mirrors.isChecked():
            self.ledit_number_of_mirrors.setEnabled(True)
        else:
            self.ledit_number_of_mirrors.setEnabled(False)
        
if __name__ == "__main__":
    app= QtWidgets.QApplication(sys.argv)
    window=MirrorsUi()
    window.show()
    app.exec_()

