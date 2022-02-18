from PyQt5 import QtWidgets, uic
import sys
import subprocess
from time import sleep
import threading
import re
import os

PATH= os.path.dirname(os.path.realpath(__file__))

class Ui(QtWidgets.QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(f'{PATH}/ui/home_cache_wid.ui', self)
        
        self.btn_clear.clicked.connect(self.clear_btn_callback)
        self.btn_remove_manually.clicked.connect(self.remove_manually_btn_callback)
        self.btn_clear_all.clicked.connect(self.clear_all_btn_callback)
        self.lineEdit.returnPressed.connect(self.btn_clear.click)
        
        #edit the default value of comboBoxes as they default to zero index
        self.comboBox.setCurrentIndex(1)


        # self.lineEdit.clicked.connect(self.lineEdit.selectAll())
    # def clear_btn_callback(self):
    #     print('clicked')

        threading.Thread(target=self.refreshSize).start()
        
    def refreshSize(self):
        """ blocking call from thread"""
        while True:
            sleep(0.5)
            self.label_size.setText('Current size of cache in home directory is : '+str(self.getCacheSize()))
        
    
        
    def getCacheSize(self):
        exceptionCount=0
        
        try:
            temp = subprocess.check_output(['du -sh ~/.cache/'],shell=True).decode()
            
        except Exception as e:
            print(e)
            print(str(e)[0:10])
            # sleep(exceptionCount*3)
            return 0
            exceptionCount+=1
                    
        if exceptionCount==5:
            return 0
        values =re.findall('\d+.',temp)
        # print(values)
        
        if len(values)>0:
            if '.' not in values[0]:
                return values[0]
            else:
                values =re.findall('\d+\.\d.',temp)
                try:
                    return values[0]
                except:
                    print('coudnt get value of cache')
                    pass

        else:
             return ''
         
         
    def clear_all_btn_callback(self):
        
        # value = self.getCacheSize()
        print('clear all executed')
        subprocess.Popen(['rm -rf ~/.cache'],shell=True)
        

    def clear_btn_callback(self):
        number=self.lineEdit.text()
        try:
            int(number)
            
            if self.comboBox.currentText()=='days':   
                print(f'find ~/.cache/ -type f -atime +{number} -delete')
                subprocess.Popen([f'find ~/.cache/ -type f -atime +{number} -delete'],shell=True)
            elif self.comboBox.currentText()=='hours':
                print(f'find ~/.cache/ -type f -amin +{int(number)*60} -delete')
                subprocess.Popen([f'find ~/.cache/ -type f -amin +{int(number)*60} -delete'],shell=True)
                
            elif self.comboBox.currentText()=='months':
                print(f'find ~/.cache/ -type f -atime +{int(number)*30} -delete')
                subprocess.Popen([f'find ~/.cache/ -type f -atime +{int(number)*30} -delete'],shell=True)
            else:print(self.comboBox.currentText())

        except Exception as e:
            print(str(e))
            self.lineEdit.setText('please enter a number')
            self.lineEdit.selectAll()
            self.lineEdit.setFocus()
        
    def remove_manually_btn_callback(self):
        subprocess.Popen(['xdg-open ~/.cache'],shell=True)


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    
    app.exec_()