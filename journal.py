from PyQt5 import QtWidgets, uic ,QtCore
import sys
import subprocess
from time import sleep
import threading
import re

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('journalctl.ui', self)
        
    
        threading.Thread(target=self.setSizeLabel).start()
        self.btn_clear_time.clicked.connect(self.btn_clear_time_callback)
        self.btn_clear_size.clicked.connect(self.btn_clear_size_callback)
        
        self.btn_show_details =QtWidgets.QPushButton()
        self.btn_show_details.setText('Show details')
        self.btn_show_details.clicked.connect(self.btn_show_details_callback)
        
        self.showDetails=False
        self.scrollLabel=False
        
        #adds scroll area with label
        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 533, 162))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
            
    def btn_show_details_callback(self):
        if not self.scrollLabel:
            self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
            self.scrollLabel=True
            self.btn_show_details.setText('Hide details')
        
        else:
            self.scrollArea.setParent(None)
            self.btn_show_details.setText('Show details')
            self.scrollLabel=False
     

    def initShowDetails(self):
        if not self.showDetails:
            
            self.verticalLayout.addWidget(self.btn_show_details)
            self.showDetails=True
    def setSizeLabel(self):
        while True:
            self.lbl_size.setText('Current size of journal ctl is '+self.getSize())
            sleep(0.5)
        
    def getSize(self):
        temp =subprocess.check_output(['journalctl --disk-usage'],shell=True).decode()
        temp2 = re.findall('\d+\.\d.',temp)
        # print(temp2)
        return temp2[0] 
   
    def btn_clear_time_callback(self):
        try:
            combo_value=self.comboBoxTime.currentText()
            number = int(self.ledt_time.text())
            self.initShowDetails()
            if combo_value=='months' or combo_value=='weeks':
                self.label.setText(self.label.text()+'\n'+f'journalctl --vacuum-time={number}{combo_value}')
                out = subprocess.check_output([f'journalctl --vacuum-time={number}{combo_value} 2>&1'],shell=True).decode()
                print('out start'+out,'out')
                
                self.label.setText(self.label.text()+'\n'+out)
                
            elif combo_value=='days':
                self.label.setText(self.label.text()+'\n'+f'journalctl --vacuum-time={number*24}h')
                out = subprocess.check_output([f'journalctl --vacuum-time={number*24}h 2>&1'],shell=True).decode()
                self.label.setText(self.label.text()+'\n'+out)
                
                
            elif combo_value=='hours':
                self.label.setText(self.label.text()+'\n'+f'journalctl --vacuum-time={number}h ')
                out = subprocess.check_output([f'journalctl --vacuum-time={number}h 2>&1'],shell=True).decode()
                self.label.setText(self.label.text()+'\n'+out)
                
            elif combo_value=='minutes':
                self.label.setText(self.label.text()+'\n'+f'journalctl --vacuum-time={number}m ')
                out = subprocess.check_output([f'journalctl --vacuum-time={number}m 2>&1'],shell=True).decode()
                self.label.setText(self.label.text()+'\n'+out)
                
            elif combo_value=='seconds':
                self.label.setText(self.label.text()+'\n'+f'journalctl --vacuum-time={number}s ')
                out = subprocess.check_output([f'journalctl --vacuum-time={number}s 2>&1'],shell=True).decode()
                self.label.setText(self.label.text()+'\n'+out)
                
            
                
            

        except:
            self.ledt_time.setText('enter a number')
            self.ledt_time.selectAll()
            self.ledt_time.setFocus()
            
            
    def btn_clear_size_callback(self):
        try:
            combo_value=self.comboBoxSize.currentText()
            number = int(self.ledt_size.text())
            self.initShowDetails()
            
            print(f'journalctl --vacuum-size={number}{combo_value}')
            self.label.setText(self.label.text()+'\n'+f'journalctl --vacuum-size={number}{combo_value}')
            # out = subprocess.check_output([f'journalctl --vacuum-size={number}{combo_value}']).decode()
            # self.label.setText(self.label.text()+'\n'+out)
            

        except:
            self.ledt_size.setText('enter a number')
            self.ledt_size.selectAll()
            self.ledt_size.setFocus()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    app.exec_()