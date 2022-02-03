from PyQt5 import QtWidgets, uic ,QtCore
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('Main3.ui',self)
        self.show()
        
        self.btn_swap.clicked.connect(self.btn_swap_callback)
        self.btn_cache.clicked.connect(self.btn_cache_callback)
        self.btn_mirrors.clicked.connect(self.btn_mirrors_callback)
        self.btn_journalctl.clicked.connect(self.btn_journalctl_callback)
                
                
        self.swap_wid=None
        self.cache_wid=None
        self.journal_wid=None
        
    def btn_mirrors_callback(self):
        pass

    def btn_cache_callback(self):
        if self.cache_wid is None:
            import cache
            self.cache_wid=cache.Ui()
            self.cache_wid.btn_mainmenu.clicked.connect(self.btn_mainmenu_callback)
            #gridLayout_4 is in page2
            self.gridLayout_4.addWidget(self.cache_wid)
        self.stackedWidget.setCurrentIndex(1)
        
    def btn_swap_callback(self):
        if self.swap_wid is None:
            import swap
            self.swap_wid =swap.Ui()
            self.swap_wid.btn_mainmenu.clicked.connect(self.btn_mainmenu_callback)
            
            #for page3
            self.gridLayout_9.addWidget(self.swap_wid)
        self.stackedWidget.setCurrentIndex(3)
        
    def btn_mainmenu_callback(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def btn_journalctl_callback(self):
        if self.journal_wid is None:
            import journal
            #grid lyout_6 is in page3
            self.journal_wid=journal.Ui()
            self.gridLayout_6.addWidget(self.journal_wid)
            
            
            self.journal_wid.btn_mainmenu.clicked.connect(self.btn_mainmenu_callback)

        self.stackedWidget.setCurrentIndex(2)
# class CacheUi(QtWidgets.QWidget):
#     def __init__(self):
#         super(CacheUi, self).__init__()
#         uic.loadUi('home_cache_wid.ui',self)

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()