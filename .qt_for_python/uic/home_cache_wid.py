# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/thenujan/Desktop/Code/system_maintenance_pyqt/home_cache_wid.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 350)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(500, 75))
        self.label.setMaximumSize(QtCore.QSize(1213, 16777215))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_size = QtWidgets.QLabel(Form)
        self.label_size.setText("")
        self.label_size.setObjectName("label_size")
        self.verticalLayout.addWidget(self.label_size)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 35)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_remove_manually = QtWidgets.QPushButton(Form)
        self.btn_remove_manually.setMinimumSize(QtCore.QSize(0, 30))
        self.btn_remove_manually.setStyleSheet("margin-left:150px;margin-right:150px;")
        self.btn_remove_manually.setFlat(False)
        self.btn_remove_manually.setObjectName("btn_remove_manually")
        self.horizontalLayout.addWidget(self.btn_remove_manually)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet("")
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.btn_clear = QtWidgets.QPushButton(self.groupBox)
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_mainmenu = QtWidgets.QPushButton(Form)
        self.btn_mainmenu.setObjectName("btn_mainmenu")
        self.horizontalLayout_4.addWidget(self.btn_mainmenu)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_4.addWidget(self.btn_cancel)
        self.btn_clear_all = QtWidgets.QPushButton(Form)
        self.btn_clear_all.setObjectName("btn_clear_all")
        self.horizontalLayout_4.addWidget(self.btn_clear_all)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "The hidden .cache folder in your home   directory is used by many parts of your system. This includes downloads,  thumbnails, desktop resources, and more. While it is generally safe to remove everything in your ~/.cache folder, it may be more advisable to inspect its contents and selectively remove items instead.\'"))
        self.btn_remove_manually.setText(_translate("Form", "remove manually"))
        self.groupBox.setTitle(_translate("Form", "remove unaccessed cache"))
        self.label_2.setText(_translate("Form", "You can also delete the cache that wasnt accesed in certain number of days"))
        self.lineEdit.setText(_translate("Form", "0"))
        self.comboBox.setItemText(0, _translate("Form", "months"))
        self.comboBox.setItemText(1, _translate("Form", "days"))
        self.comboBox.setItemText(2, _translate("Form", "hours"))
        self.btn_clear.setText(_translate("Form", "clear"))
        self.btn_mainmenu.setText(_translate("Form", "Main menu"))
        self.btn_cancel.setText(_translate("Form", "cancel"))
        self.btn_clear_all.setText(_translate("Form", "Clear ALL"))