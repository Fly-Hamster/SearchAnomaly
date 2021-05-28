from mainForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import helpForm_class
class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit_output_field.setReadOnly(True)
        self.progressBar.setProperty("value", None)

        self.action.triggered.connect(self.openDoc)
        self.action_2.triggered.connect(self.saveResult)
        self.action_3.triggered.connect(self.open_help)

    def openDoc(self):
        print('openDoc')

    def saveResult(self):
        print("save")

    def open_help(self):
        print('help')
        win = helpForm_class.HelpForm()
        win.setFixedSize(628, 336)
        win.show()




