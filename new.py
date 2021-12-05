# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'journalctl.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
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
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_size = QtWidgets.QLabel(self.centralwidget)
        self.lbl_size.setObjectName("lbl_size")
        self.verticalLayout.addWidget(self.lbl_size)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ledt_time = QtWidgets.QLineEdit(self.groupBox)
        self.ledt_time.setMaximumSize(QtCore.QSize(70, 16777215))
        self.ledt_time.setObjectName("ledt_time")
        self.horizontalLayout_2.addWidget(self.ledt_time)
        self.comboBoxTime = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxTime.setObjectName("comboBoxTime")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.comboBoxTime.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxTime)
        self.btn_clear_time = QtWidgets.QPushButton(self.groupBox)
        self.btn_clear_time.setObjectName("btn_clear_time")
        self.horizontalLayout_2.addWidget(self.btn_clear_time)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ledt_size = QtWidgets.QLineEdit(self.groupBox)
        self.ledt_size.setMaximumSize(QtCore.QSize(70, 16777215))
        self.ledt_size.setObjectName("ledt_size")
        self.horizontalLayout_2.addWidget(self.ledt_size)
        self.comboBoxSize = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxSize.setObjectName("comboBoxSize")
        self.comboBoxSize.addItem("")
        self.comboBoxSize.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBoxSize)
        self.btn_clear_size = QtWidgets.QPushButton(self.groupBox)
        self.btn_clear_size.setObjectName("btn_clear_size")
        self.horizontalLayout_2.addWidget(self.btn_clear_size)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"))
        self.lbl_size.setText(_translate("MainWindow", "Current size of journal ctl is"))
        self.groupBox.setTitle(_translate("MainWindow", "remove all but the most recent entries by size or time"))
        self.ledt_time.setText(_translate("MainWindow", "12"))
        self.comboBoxTime.setItemText(0, _translate("MainWindow", "months"))
        self.comboBoxTime.setItemText(1, _translate("MainWindow", "weeks"))
        self.comboBoxTime.setItemText(2, _translate("MainWindow", "days"))
        self.comboBoxTime.setItemText(3, _translate("MainWindow", "hours"))
        self.comboBoxTime.setItemText(4, _translate("MainWindow", "minutes"))
        self.comboBoxTime.setItemText(5, _translate("MainWindow", "seconds"))
        self.btn_clear_time.setText(_translate("MainWindow", "clear"))
        self.ledt_size.setText(_translate("MainWindow", "50"))
        self.comboBoxSize.setItemText(0, _translate("MainWindow", "M"))
        self.comboBoxSize.setItemText(1, _translate("MainWindow", "G"))
        self.btn_clear_size.setText(_translate("MainWindow", "clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
