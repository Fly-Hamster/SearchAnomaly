from mainForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from mainForm_class import MainForm

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainForm()
    ui.setFixedSize(720, 552)
    ui.show()
    sys.exit(app.exec_())