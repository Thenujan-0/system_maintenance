# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_cache.ui'
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
        MainWindow.resize(522, 403)
        MainWindow.setAcceptDrops(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(500, 75))
        self.label.setMaximumSize(QSize(1213, 16777215))
        self.label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_size = QLabel(self.centralwidget)
        self.label_size.setObjectName(u"label_size")

        self.verticalLayout.addWidget(self.label_size)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 35)
        self.btn_remove_manually = QPushButton(self.centralwidget)
        self.btn_remove_manually.setObjectName(u"btn_remove_manually")
        self.btn_remove_manually.setMinimumSize(QSize(0, 30))
        self.btn_remove_manually.setStyleSheet(u"margin-left:150px;margin-right:150px;")
        self.btn_remove_manually.setFlat(False)

        self.horizontalLayout.addWidget(self.btn_remove_manually)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(True)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.btn_clear = QPushButton(self.groupBox)
        self.btn_clear.setObjectName(u"btn_clear")

        self.horizontalLayout_2.addWidget(self.btn_clear)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.btn_cancel = QPushButton(self.centralwidget)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout_4.addWidget(self.btn_cancel)

        self.btn_clear_all = QPushButton(self.centralwidget)
        self.btn_clear_all.setObjectName(u"btn_clear_all")

        self.horizontalLayout_4.addWidget(self.btn_clear_all)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 522, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"The hidden .cache folder in your home   directory is used by many parts of your system. This includes downloads,  thumbnails, desktop resources, and more. While it is generally safe to remove everything in your ~/.cache folder, it may be more advisable to inspect its contents and selectively remove items instead.'", None))
        self.label_size.setText("")
        self.btn_remove_manually.setText(QCoreApplication.translate("MainWindow", u"remove manually", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"remove unaccessed cache", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"You can also delete the cache that wasnt accesed in certain number of days", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"months", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"days", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"hours", None))

        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.btn_cancel.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.btn_clear_all.setText(QCoreApplication.translate("MainWindow", u"Clear ALL", None))
    # retranslateUi

