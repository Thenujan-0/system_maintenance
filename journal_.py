from PyQt5 import QtCore , QtGui ,uic,QtWidgets
import sys
import os

 
class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('journalctl_.ui',self)
    
if __name__ == '__main__':
        
    app =QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()