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
    max = float(column[0][1])
    for i in column:
        if float(i[1])> max:
            max = float(i[1])
    return max

def min():
    column = open_file()
    min = float(column[0][1])
    for i in column:
        if float(i[1]) < min:
            min = float(i[1])
    return min

def number_lines():
    column = open_file()
    N = len(column)
    return N

def average():
    column = open_file()
    N = number_lines()
    sum = 0
    for i in column:
        sum += float(i[1])
    aver = round(sum/N, 3)
    return aver


