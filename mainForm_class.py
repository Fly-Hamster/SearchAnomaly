from mainForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import helpForm_class
import errorForm_class
class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit_output_field.setReadOnly(True)
        self.progressBar.setProperty("value", None)
        self.progressBar.setEnabled(False)
        # start help
        self.label_info_1.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Загрузите файл *.csv..</span></p></body></html>')
        self.label_info_2.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Нажмите кнопку "Начать поиск".</span></p></body></html>')
        # mute start button and button for save result
        self.button_play.setEnabled(False)
        self.saveFile.setEnabled(False)
        # connect menu's actions with functions
        self.loadFile.triggered.connect(self.openDoc)
        self.saveFile.triggered.connect(self.saveResult)
        self.openHelp.triggered.connect(self.open_help)

    def openDoc(self):
        self.fileName, val = QtWidgets.QFileDialog.getOpenFileName()
        # checkin the selected file's type
        if 'csv' in self.fileName:
            # сделать вывод количества столбцов и считать ввод номера, только потом открыть кнопку
            self.button_play.setEnabled(True)
        else:
            f_err = open('error_text.txt', 'w', encoding='utf-8')
            f_err.write(' Ошибка при открытии файла.\n Возможно, выбран другой формат.\n Откройте файл с расширением .csv.')
            f_err.close()
            win = errorForm_class.ErrorForm()
            win.setFixedSize(640, 302)
            win.show()


    def saveResult(self):
        print("save")

    def open_help(self):
        print('help')
        win = helpForm_class.HelpForm()
        win.setFixedSize(628, 336)
        win.show()

    def start(self):
        print('start')
        # открыть прогресс бар

        # в конце открыть кнопку сохранить


