from PyQt5 import QtWidgets, uic, QtCore
import sys
from time import sleep
import threading



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('Main.ui',self)
        self.show()
        
        self.journalWindow=None
        self.cacheWindow=None
        self.swapWindow=None
        
        self.btn_rm_cache.clicked.connect(self.btn_rm_cache_callback)
        self.btn_rm_journal.clicked.connect(self.btn_rm_journal_callback)
        self.btn_swap.clicked.connect(self.btn_swap_callback)
        
    def btn_rm_cache_callback(self):
        import cache
        if not self.cacheWindow:
            self.cacheWindow=cache.Ui()
            self.cacheWindow.show()
        else:
            self.cacheWindow.activateWindow()
            self.cacheWindow.raise_()
    def btn_rm_journal_callback(self):
        import journal
        
        if not self.journalWindow:
            self.journalWindow=journal.Ui()
            self.journalWindow.show()

        else:
            print(self.journalWindow)
            
            if not self.journalWindow.isVisible():
                self.journalWindow=journal.Ui()
                self.journalWindow.show()
            else:
                self.journalWindow.activateWindow()
                self.journalWindow.raise_()
                
    def btn_swap_callback(self):
        import swap
        
        if not self.journalWindow:
            self.journalWindow=swap.Ui()
            self.journalWindow.show()

        else:
            print(self.journalWindow)
            
            if not self.journalWindow.isVisible():
                self.journalWindow=swap.Ui()
                self.journalWindow.show()
            else:
                self.journalWindow.activateWindow()
                self.journalWindow.raise_()
    

app =QtWidgets.QApplication(sys.argv)
window= Ui()
app.exec_()
 