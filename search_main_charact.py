import csv
def open_file():
    fileForWork = open('csvForWork.csv', 'r')
    text = csv.reader(fileForWork, delimiter=";")
    all_columns = []
    for i in text:
        all_columns.append(i)
    return all_columns

def max():
    column = open_file()

    # sum = 0
    # for i in range(column):
    #     print(type(column[1]))
    #
    #     sum+=int(column[1])
    # print(sum)

def min():
    column = open_file()
    print('min')

def average():
    column = open_file()
    print(average)

def number_lines():
    column = open_file()
    print('lines')
