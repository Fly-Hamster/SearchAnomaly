
# import librarys
from mainForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import csv

# import files
import helpForm_class
import errorForm_class
class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png'))
        self.textEdit_output_field.setReadOnly(True)
        self.progressBar.setProperty("value", None)
        self.progressBar.setEnabled(False)
        # start help
        self.label_info_1.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Загрузите файл *.csv..</span></p></body></html>')
        self.label_info_2.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Нажмите кнопку "Начать поиск".</span></p></body></html>')
        # mute start button and button for save result
        self.button_play.setEnabled(False)
        self.saveFile.setEnabled(False)
        self.lineEdit_number_column.setEnabled(False)
        # connect menu's actions with functions
        self.loadFile.triggered.connect(self.openDoc)
        self.saveFile.triggered.connect(self.saveResult)
        self.openHelp.triggered.connect(self.open_help)

    def openDoc(self):
        self.fileName, val = QtWidgets.QFileDialog.getOpenFileName()
        # checkin the selected file's type
        if 'csv' in self.fileName:
            # сделать вывод количества столбцов и считать ввод номера, только потом открыть кнопку
            fileForWork = open(self.fileName, 'r')
            text = csv.reader(fileForWork)
            all_columns = []
            for i in text:
                all_columns.append(i)
            # count the number of columns (number delimeters + 1)
            number_columns = all_columns[0][0].count(';')+1

            if number_columns<2:
                f_err = open('error_text.txt', 'w', encoding='utf-8')
                f_err.write(' Файл содержит меньше 2 столбцов. \n Должно быть минимум 2:\n -временной показатель;\n -ряд.')
                f_err.close()
                win = errorForm_class.ErrorForm()
                win.setFixedSize(640, 302)
                win.show()
            elif number_columns>=2:
                text = 'Количество столбцов _'+str(number_columns)+'_'
                # output information about number columns and user can chooese
                self.label_number_column.setText(text)
                self.label_number_column.setFont(QtGui.QFont("Times", 10))
                self.lineEdit_number_column.setEnabled(True)
                self.lineEdit_number_column.setInputMask('999')
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


