
# import librarys
from mainForm import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import csv
import numpy as np

# import files
import helpForm_class
import errorForm_class
import search_main_charact

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
        self.label_info_2.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\"> </span></p></body></html>')
        # mute start button and button for save result
        self.button_play.setEnabled(False)
        self.saveFile.setEnabled(False)
        self.lineEdit_number_column.setEnabled(False)
        # connect menu's actions with functions
        self.loadFile.triggered.connect(self.openDoc)
        self.saveFile.triggered.connect(self.saveResult)
        self.openHelp.triggered.connect(self.open_help)

        # connect button_ply with start
        self.button_play.clicked.connect(self.start)

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
            self.number_columns = all_columns[0][0].count(';')

            if self.number_columns<1:
                f_err = open('error_text.txt', 'w', encoding='utf-8')
                f_err.write(' Файл содержит меньше 2 столбцов. \n Должно быть минимум 2:\n -временной показатель;\n -ряд.')
                f_err.close()
                win = errorForm_class.ErrorForm()
                win.setFixedSize(640, 302)
                win.show()
            elif self.number_columns>=1:
                text = 'Количество столбцов _'+str(self.number_columns)+'_'
                # output information about number columns and user can chooese
                self.label_number_column.setText(text)
                self.label_number_column.setFont(QtGui.QFont("Times", 10))
                self.label_info_1.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Введите столбец.</span></p></body></html>')
                self.label_info_2.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Нажмите кнопку "Начать поиск".</span></p></body></html>')
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
        self.count = self.lineEdit_number_column.text()
        print(type(self.count))
        print(self.number_columns)
        if int(self.count)<1 or int(self.count)> self.number_columns:
            print('here')
            f_err = open('error_text.txt', 'w', encoding='utf-8')
            f_err.write(' Неверное количество столбцов.')
            f_err.close()
            win = errorForm_class.ErrorForm()
            win.setFixedSize(640, 302)
            win.show()
            self.lineEdit_number_column.setText("")
            self.label_info_1.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Введите столбец.</span></p></body></html>')
            self.label_info_2.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Нажмите кнопку "Начать поиск".</span></p></body></html>')

            return 0

        # сделать проверку введенного числа
        self.label_info_1.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Обработка документа может занять некоторое время.</span></p></body></html>')
        self.label_info_2.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Пожалуйста, подождите.</span></p></body></html>')

        # открыть прогресс бар
        self.progressBar.setEnabled(True)

        # считать в отдельный документ временной интервал и нужный столбец
        self.createNewFileForWork()
        # вызов функции для поиска основных характеристик
        search_main_charact.search_main_char()
        # Вызов НС

        # в конце открыть кнопку сохранить
        self.saveFile.setEnabled(True)

    def createNewFileForWork(self):
        print('newFile')
        fileForWork = open(self.fileName, 'r')
        text = csv.reader(fileForWork, delimiter = ";")
        all_columns = []
        for i in text:
            all_columns.append(i)
        dataForWork = []
        for i in range(len(all_columns)):
            pair = []
            pair.append(all_columns[i][0])
            pair.append(all_columns[i][int(self.count)])
            dataForWork.append(pair)

        file = open('csvForWork.csv', 'w', newline='')
        print('here1')
        writer = csv.writer(file, delimiter = ";")
        print('here')
        # запись нескольких строк
        writer.writerows(dataForWork)


