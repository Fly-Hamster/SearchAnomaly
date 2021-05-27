from errorForm import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator, QPainter, QPen, QTransform
class ErrorForm(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button_Ok.clicked.connect( lambda: self.close())
        self.pixmap = QPixmap('error_img.png')
        self.pixmap = self.pixmap.scaled(200, 200)
        self.label_img.setPixmap(self.pixmap)
        self.file()

    def file(self):
        print('file')
        f=open('error_text.txt', 'r', encoding='utf-8')
        error_text = f.read()
        self.label_text_err.setText(error_text)
        f.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ErrorForm()
    ui.setFixedSize(640, 302)
    ui.show()
    sys.exit(app.exec_())
