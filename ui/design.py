# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(677, 455)
        self.frame_left = QtWidgets.QFrame(Dialog)
        self.frame_left.setGeometry(QtCore.QRect(0, 60, 191, 341))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.label_time = QtWidgets.QLabel(self.frame_left)
        self.label_time.setGeometry(QtCore.QRect(10, 260, 47, 13))
        self.label_time.setObjectName("label_time")
        self.label_2 = QtWidgets.QLabel(self.frame_left)
        self.label_2.setGeometry(QtCore.QRect(10, 280, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_left)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 47, 13))
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(self.frame_left)
        self.widget.setGeometry(QtCore.QRect(10, 20, 181, 242))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.executeBtn = QtWidgets.QPushButton(self.widget)
        self.executeBtn.setObjectName("executeBtn")
        self.verticalLayout.addWidget(self.executeBtn)
        self.frame_top = QtWidgets.QFrame(Dialog)
        self.frame_top.setGeometry(QtCore.QRect(0, 0, 671, 61))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.label_load_from_file = QtWidgets.QLabel(self.frame_top)
        self.label_load_from_file.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_load_from_file.setObjectName("label_load_from_file")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_top)
        self.lineEdit.setGeometry(QtCore.QRect(110, 20, 321, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(self.frame_top)
        self.line.setGeometry(QtCore.QRect(0, 50, 671, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.frame_top)
        self.label_4.setGeometry(QtCore.QRect(440, 10, 61, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_top)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 10, 41, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_top)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 30, 41, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.frame_top)
        self.label_5.setGeometry(QtCore.QRect(440, 30, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_load_from_file.raise_()
        self.lineEdit.raise_()
        self.line.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.frame_bottom = QtWidgets.QFrame(Dialog)
        self.frame_bottom.setGeometry(QtCore.QRect(0, 400, 671, 61))
        self.frame_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom.setObjectName("frame_bottom")
        self.label_status = QtWidgets.QLabel(self.frame_bottom)
        self.label_status.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_status.setObjectName("label_status")
        self.line_2 = QtWidgets.QFrame(self.frame_bottom)
        self.line_2.setGeometry(QtCore.QRect(0, 0, 671, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(200, 60, 461, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_load_from_file.setBuddy(self.listWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.listWidget)
        Dialog.setTabOrder(self.listWidget, self.executeBtn)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_time.setText(_translate("Dialog", "Time:"))
        self.label_2.setText(_translate("Dialog", "Edges:"))
        self.label_3.setText(_translate("Dialog", "Vertex:"))
        self.label.setText(_translate("Dialog", "Avalible Actions:"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "Generate graph"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "Alg push_flow"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "Alg Dinica"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "Draw Circle"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "Draw"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.executeBtn.setText(_translate("Dialog", "Execute"))
        self.label_load_from_file.setText(_translate("Dialog", "Load graph from file:"))
        self.label_4.setText(_translate("Dialog", "Vertex cnt:"))
        self.label_5.setText(_translate("Dialog", "Edges cnt:"))
        self.label_status.setText(_translate("Dialog", "Status:"))
