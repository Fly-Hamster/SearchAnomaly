from helpForm import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator, QPainter, QPen, QTransform
class HelpForm(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_Ok.clicked.connect( lambda: self.close())
        self.textEdit_helpText.setReadOnly(True)
        self.pixmap = QPixmap('help_img.png')
        self.pixmap = self.pixmap.scaled(200, 200)
        self.label_img.setPixmap(self.pixmap)
        self.file()

    def file(self):
        print('file')
        f = open('help_text.txt', 'r', encoding='utf-8')
        help_text = f.read()
        self.textEdit_helpText.setText(help_text)
        f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = HelpForm()
    ui.setFixedSize(628, 336)
    ui.show()
    sys.exit(app.exec_())
