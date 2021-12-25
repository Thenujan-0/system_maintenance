# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(390, 153)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_rm_journal = QPushButton(self.centralwidget)
        self.btn_rm_journal.setObjectName(u"btn_rm_journal")

        self.gridLayout.addWidget(self.btn_rm_journal, 1, 0, 1, 1)

        self.btn_mirrors = QPushButton(self.centralwidget)
        self.btn_mirrors.setObjectName(u"btn_mirrors")

        self.gridLayout.addWidget(self.btn_mirrors, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        self.btn_rm_cache = QPushButton(self.centralwidget)
        self.btn_rm_cache.setObjectName(u"btn_rm_cache")

        self.gridLayout.addWidget(self.btn_rm_cache, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 390, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Maintenance", None))
        self.btn_rm_journal.setText(QCoreApplication.translate("MainWindow", u"remove journalctl logs", None))
        self.btn_mirrors.setText(QCoreApplication.translate("MainWindow", u"mirrors", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"swap memory", None))
        self.btn_rm_cache.setText(QCoreApplication.translate("MainWindow", u"remove cache in home directory", None))
    # retranslateUi

