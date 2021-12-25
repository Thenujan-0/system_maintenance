import subprocess
from time import sleep
from PyQt5 import QtWidgets , uic, QtCore
from PyQt5.QtCore import Qt
import sys
import threading

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('swap.ui',self)
        self.show()

        import subprocess

        out =subprocess.check_output(['swapon'],shell=True).decode()

        linesCount = len(out.splitlines())
        print('linesCount',linesCount)
        self.label
        out = subprocess.check_output([f'swapon | tail -n -{linesCount-1}'],shell=True).decode()
        print(out)
        lines = out.splitlines()
        for j in range(len(lines)):
            words = lines[j].split()
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)

            
            for i in range(len(words)):
                
                
                item = QtWidgets.QTableWidgetItem()
                item.setText(words[i])
                self.tableWidget.setItem(j, i, item)
        
        
        

        header = self.tableWidget.horizontalHeader()
        header.setMinimumSectionSize(100)      
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)       
        
        
        
        
        self.btn_add.clicked.connect(self.btn_add_callback)

        
    def btn_add_callback(self,btn):
        btn=self.sender()
        point=btn.pos()
        print(self.pos())
        self.win = add_btn_window()
        self.win.setGeometry(point.x()+self.win_pos.x() ,self.win_pos.y()+ point.y()+20,100,50)
        self.win.setFocus()
        self.win.show()
        
    def moveEvent(self, e):
        self.win_pos =self.pos()
        super(Ui, self).moveEvent(e)
        
        
class add_btn_window(QtWidgets.QWidget):
    def __init__(self):
        super(add_btn_window, self).__init__()
        uic.loadUi('swap_add.ui',self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(0, 0, 100, 100)
        self.setFocusPolicy(Qt.StrongFocus)
        
    def focusOutEvent(self, event):
        self.hide()
        super(add_btn_window,self).focusOutEvent(event)
    
    

    
app= QtWidgets.QApplication(sys.argv)
window= Ui()
app.exec_()