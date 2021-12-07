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
        MainWindow.resize(559, 297)
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

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ledt_max_size = QLineEdit(self.groupBox_2)
        self.ledt_max_size.setObjectName(u"ledt_max_size")
        self.ledt_max_size.setMinimumSize(QSize(0, 0))
        self.ledt_max_size.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.ledt_max_size)

        self.comboBoxMaxSize = QComboBox(self.groupBox_2)
        self.comboBoxMaxSize.addItem("")
        self.comboBoxMaxSize.addItem("")
        self.comboBoxMaxSize.setObjectName(u"comboBoxMaxSize")

        self.horizontalLayout.addWidget(self.comboBoxMaxSize)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.lbl_max_size = QLabel(self.groupBox_2)
        self.lbl_max_size.setObjectName(u"lbl_max_size")

        self.gridLayout_3.addWidget(self.lbl_max_size, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"remove journalctl logs", None))
        self.lbl_size.setText(QCoreApplication.translate("MainWindow", u"Current size of journal ctl is", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"remove all but the most recent entries by size or time", None))
        self.ledt_time.setText(QCoreApplication.translate("MainWindow", u"3", None))
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
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"set a maximum size for the journal ", None))
        self.ledt_max_size.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBoxMaxSize.setItemText(0, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBoxMaxSize.setItemText(1, QCoreApplication.translate("MainWindow", u"G", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"set", None))
        self.lbl_max_size.setText(QCoreApplication.translate("MainWindow", u"maximum size is not set for the journal", None))
    # retranslateUi

