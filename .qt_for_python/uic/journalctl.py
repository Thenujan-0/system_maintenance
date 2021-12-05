# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'journalctl.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(559, 187)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_size = QLabel(self.centralwidget)
        self.lbl_size.setObjectName(u"lbl_size")

        self.verticalLayout.addWidget(self.lbl_size)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ledt_time = QLineEdit(self.groupBox)
        self.ledt_time.setObjectName(u"ledt_time")
        self.ledt_time.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.ledt_time)

        self.comboBoxTime = QComboBox(self.groupBox)
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.setObjectName(u"comboBoxTime")

        self.horizontalLayout_2.addWidget(self.comboBoxTime)

        self.btn_clear_time = QPushButton(self.groupBox)
        self.btn_clear_time.setObjectName(u"btn_clear_time")

        self.horizontalLayout_2.addWidget(self.btn_clear_time)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.ledt_size = QLineEdit(self.groupBox)
        self.ledt_size.setObjectName(u"ledt_size")
        self.ledt_size.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_2.addWidget(self.ledt_size)

        self.comboBoxSize = QComboBox(self.groupBox)
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.setObjectName(u"comboBoxSize")

        self.horizontalLayout_2.addWidget(self.comboBoxSize)

        self.btn_clear_size = QPushButton(self.groupBox)
        self.btn_clear_size.setObjectName(u"btn_clear_size")

        self.horizontalLayout_2.addWidget(self.btn_clear_size)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 559, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_size.setText(QCoreApplication.translate("MainWindow", u"Current size of journal ctl is", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"remove all but the most recent entries by size or time", None))
        self.ledt_time.setText(QCoreApplication.translate("MainWindow", u"12", None))
        self.comboBoxTime.setItemText(0, QCoreApplication.translate("MainWindow", u"months", None))
        self.comboBoxTime.setItemText(1, QCoreApplication.translate("MainWindow", u"weeks", None))
        self.comboBoxTime.setItemText(2, QCoreApplication.translate("MainWindow", u"days", None))
        self.comboBoxTime.setItemText(3, QCoreApplication.translate("MainWindow", u"hours", None))
        self.comboBoxTime.setItemText(4, QCoreApplication.translate("MainWindow", u"minutes", None))
        self.comboBoxTime.setItemText(5, QCoreApplication.translate("MainWindow", u"seconds", None))

        self.btn_clear_time.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.ledt_size.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBoxSize.setItemText(0, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBoxSize.setItemText(1, QCoreApplication.translate("MainWindow", u"G", None))

        self.btn_clear_size.setText(QCoreApplication.translate("MainWindow", u"clear", None))
    # retranslateUi

