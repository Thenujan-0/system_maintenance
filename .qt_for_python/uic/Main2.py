# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main2.ui'
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
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 353)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_size_2 = QLabel(self.tab)
        self.lbl_size_2.setObjectName(u"lbl_size_2")

        self.verticalLayout_5.addWidget(self.lbl_size_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAcceptDrops(False)
        self.groupBox_3.setCheckable(True)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ledt_time_2 = QLineEdit(self.groupBox_3)
        self.ledt_time_2.setObjectName(u"ledt_time_2")
        self.ledt_time_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_5.addWidget(self.ledt_time_2)

        self.comboBoxTime_2 = QComboBox(self.groupBox_3)
        self.comboBoxTime_2.addItem("")
        self.comboBoxTime_2.addItem("")
        self.comboBoxTime_2.addItem("")
        self.comboBoxTime_2.addItem("")
        self.comboBoxTime_2.addItem("")
        self.comboBoxTime_2.addItem("")
        self.comboBoxTime_2.setObjectName(u"comboBoxTime_2")

        self.horizontalLayout_5.addWidget(self.comboBoxTime_2)

        self.btn_clear_time_2 = QPushButton(self.groupBox_3)
        self.btn_clear_time_2.setObjectName(u"btn_clear_time_2")

        self.horizontalLayout_5.addWidget(self.btn_clear_time_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.ledt_size_2 = QLineEdit(self.groupBox_3)
        self.ledt_size_2.setObjectName(u"ledt_size_2")
        self.ledt_size_2.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_5.addWidget(self.ledt_size_2)

        self.comboBoxSize_2 = QComboBox(self.groupBox_3)
        self.comboBoxSize_2.addItem("")
        self.comboBoxSize_2.addItem("")
        self.comboBoxSize_2.setObjectName(u"comboBoxSize_2")

        self.horizontalLayout_5.addWidget(self.comboBoxSize_2)

        self.btn_clear_size_2 = QPushButton(self.groupBox_3)
        self.btn_clear_size_2.setObjectName(u"btn_clear_size_2")

        self.horizontalLayout_5.addWidget(self.btn_clear_size_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ledt_max_size_2 = QLineEdit(self.groupBox_4)
        self.ledt_max_size_2.setObjectName(u"ledt_max_size_2")
        self.ledt_max_size_2.setMinimumSize(QSize(0, 0))
        self.ledt_max_size_2.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.ledt_max_size_2)

        self.comboBoxMaxSize_2 = QComboBox(self.groupBox_4)
        self.comboBoxMaxSize_2.addItem("")
        self.comboBoxMaxSize_2.addItem("")
        self.comboBoxMaxSize_2.setObjectName(u"comboBoxMaxSize_2")

        self.horizontalLayout_6.addWidget(self.comboBoxMaxSize_2)

        self.btn_journal_max_size_2 = QPushButton(self.groupBox_4)
        self.btn_journal_max_size_2.setObjectName(u"btn_journal_max_size_2")

        self.horizontalLayout_6.addWidget(self.btn_journal_max_size_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.gridLayout_5.addLayout(self.verticalLayout_8, 0, 0, 1, 1)

        self.lbl_max_size_2 = QLabel(self.groupBox_4)
        self.lbl_max_size_2.setObjectName(u"lbl_max_size_2")

        self.gridLayout_5.addWidget(self.lbl_max_size_2, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 1, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_3)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 628, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_size_2.setText(QCoreApplication.translate("MainWindow", u"Current size of journal ctl is", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"remove all but the most recent entries by size or time", None))
        self.ledt_time_2.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBoxTime_2.setItemText(0, QCoreApplication.translate("MainWindow", u"months", None))
        self.comboBoxTime_2.setItemText(1, QCoreApplication.translate("MainWindow", u"weeks", None))
        self.comboBoxTime_2.setItemText(2, QCoreApplication.translate("MainWindow", u"days", None))
        self.comboBoxTime_2.setItemText(3, QCoreApplication.translate("MainWindow", u"hours", None))
        self.comboBoxTime_2.setItemText(4, QCoreApplication.translate("MainWindow", u"minutes", None))
        self.comboBoxTime_2.setItemText(5, QCoreApplication.translate("MainWindow", u"seconds", None))

        self.btn_clear_time_2.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.ledt_size_2.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.comboBoxSize_2.setItemText(0, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBoxSize_2.setItemText(1, QCoreApplication.translate("MainWindow", u"G", None))

        self.btn_clear_size_2.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"set a maximum size for the journal ", None))
        self.ledt_max_size_2.setText(QCoreApplication.translate("MainWindow", u"500", None))
        self.comboBoxMaxSize_2.setItemText(0, QCoreApplication.translate("MainWindow", u"M", None))
        self.comboBoxMaxSize_2.setItemText(1, QCoreApplication.translate("MainWindow", u"G", None))

        self.btn_journal_max_size_2.setText(QCoreApplication.translate("MainWindow", u"set", None))
        self.lbl_max_size_2.setText(QCoreApplication.translate("MainWindow", u"maximum size is not set for the journal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

