# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_maket_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 552)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 290, 321, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_number_line = QtWidgets.QLabel(self.groupBox)
        self.label_number_line.setGeometry(QtCore.QRect(10, 30, 301, 21))
        self.label_number_line.setObjectName("label_number_line")
        self.label_max_val = QtWidgets.QLabel(self.groupBox)
        self.label_max_val.setGeometry(QtCore.QRect(10, 60, 301, 21))
        self.label_max_val.setObjectName("label_max_val")
        self.label_min_val = QtWidgets.QLabel(self.groupBox)
        self.label_min_val.setGeometry(QtCore.QRect(10, 90, 301, 21))
        self.label_min_val.setObjectName("label_min_val")
        self.label_aver_val = QtWidgets.QLabel(self.groupBox)
        self.label_aver_val.setGeometry(QtCore.QRect(10, 120, 301, 21))
        self.label_aver_val.setObjectName("label_aver_val")
        self.label_number_anomaly = QtWidgets.QLabel(self.groupBox)
        self.label_number_anomaly.setGeometry(QtCore.QRect(10, 150, 301, 21))
        self.label_number_anomaly.setObjectName("label_number_anomaly")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(430, 50, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_play.setFont(font)
        self.button_play.setObjectName("button_play")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(50, 250, 111, 31))
        self.label_result.setObjectName("label_result")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 20, 311, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_number_column = QtWidgets.QLabel(self.groupBox_2)
        self.label_number_column.setGeometry(QtCore.QRect(10, 10, 221, 21))
        self.label_number_column.setObjectName("label_number_column")
        self.label_search_column = QtWidgets.QLabel(self.groupBox_2)
        self.label_search_column.setGeometry(QtCore.QRect(10, 40, 251, 21))
        self.label_search_column.setObjectName("label_search_column")
        self.lineEdit_number_column = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_number_column.setGeometry(QtCore.QRect(250, 40, 41, 20))
        self.lineEdit_number_column.setObjectName("lineEdit_number_column")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 120, 621, 121))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_info_1 = QtWidgets.QLabel(self.groupBox_3)
        self.label_info_1.setGeometry(QtCore.QRect(110, 30, 421, 21))
        self.label_info_1.setObjectName("label_info_1")
        self.label_info_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_info_2.setGeometry(QtCore.QRect(110, 70, 421, 31))
        self.label_info_2.setObjectName("label_info_2")
        self.textEdit_output_field = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_output_field.setGeometry(QtCore.QRect(380, 300, 291, 181))
        self.textEdit_output_field.setObjectName("textEdit_output_field")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 26))
        self.menubar.setObjectName("menubar")
        self.work_with_file = QtWidgets.QMenu(self.menubar)
        self.work_with_file.setObjectName("work_with_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loadFile = QtWidgets.QAction(MainWindow)
        self.loadFile.setObjectName("loadFile")
        self.saveFile = QtWidgets.QAction(MainWindow)
        self.saveFile.setObjectName("saveFile")
        self.openHelp = QtWidgets.QAction(MainWindow)
        self.openHelp.setObjectName("openHelp")
        self.work_with_file.addAction(self.loadFile)
        self.work_with_file.addAction(self.saveFile)
        self.menu_help.addAction(self.openHelp)
        self.menubar.addAction(self.work_with_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anomal-Time"))
        self.groupBox.setTitle(_translate("MainWindow", "???????????????? ????????????????????:"))
        self.label_number_line.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">?????????? ___ ??????????.</span></p></body></html>"))
        self.label_max_val.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">???????????????????????? ???????????????? ___.</span></p></body></html>"))
        self.label_min_val.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">?????????????????????? ???????????????? ___.</span></p></body></html>"))
        self.label_aver_val.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">?????????????? ???????????????? ___.</span></p></body></html>"))
        self.label_number_anomaly.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">?????????? ???????????????????? ???????????????? ___ .</span></p></body></html>"))
        self.button_play.setText(_translate("MainWindow", "???????????? ??????????"))
        self.label_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">??????????????????</span></p></body></html>"))
        self.label_number_column.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">???????????????????? ???????????????? ___</span></p></body></html>"))
        self.label_search_column.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">?????????????????????? ?????????? ?? ??????????????: </span></p></body></html>"))
        self.label_info_1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">?????????????????? ?????????????????? ?????????? ???????????? ?????????????????? ??????????. </span></p></body></html>"))
        self.label_info_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">????????????????????, ??????????????????.</span></p></body></html>"))
        self.work_with_file.setTitle(_translate("MainWindow", "????????"))
        self.menu_help.setTitle(_translate("MainWindow", "??????????????"))
        self.loadFile.setText(_translate("MainWindow", "??????????????????"))
        self.saveFile.setText(_translate("MainWindow", "??????????????????"))
        self.openHelp.setText(_translate("MainWindow", "??????????????"))
