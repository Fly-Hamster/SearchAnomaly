from mainForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit_output_field.setReadOnly(True)
        self.progressBar.setProperty("value", None)
