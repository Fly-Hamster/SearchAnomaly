import math

import search_main_charact
import random
def startSearch():
    print('start search')
    count_anomaly = 0
    return count_anomaly

def firstType():
    column = search_main_charact.open_file()
    number_lines = search_main_charact.number_lines()
    # если на интервале равному 4% одинаковые значение - аномалия
    part = round(number_lines*0.04)
    pair_start = column[0]
    pair_end = column[0]
    list_with_anomaly = []
    # если count == part - фномальный отрезок
    count = 0
    file = open("RESULT.txt", 'w', encoding='utf-8')
    file.write('Повторяющиеся значения: \n')
    file.close()
    work_val = float(column[0][1])
    count_anomaly = 0
    for i in column:
        file = open("RESULT.txt", "a")
        if work_val == float(i[1]):
            count+=1
            pair_end = i
            if count >= part:
                str = pair_start[0] + ' - ' + pair_end[0] + ': ' + pair_start[1] +'\n'
                file.write(str)
                count_anomaly+=1
        else:
            count = 1
            work_val = float(i[1])
            pair_start = i
            pair_end = i
        file.close()
    if count_anomaly==0:
        file = open("RESULT.txt", "a", encoding='utf-8')
        file.write('Данного типа аномалий не обнаружено. \n')
        file.close()
    print(count_anomaly)
    return count_anomaly


def count_average(start, end, size, column):
    sum = 0
    for i in range(start, end):
        sum += float(column[i][1])
    aver = sum/size
    return aver

def second():
    print('sec')
    column = search_main_charact.open_file()
    average = search_main_charact.average()
    number = search_main_charact.number_lines()
    confidence_interval = average *0.2
    part = round(number*0.05)
    print(part)
    index_start = 0
    index_end = part
    file = open("RESULT.txt", 'a', encoding='utf-8')
    file.write('Увеличение среднего значения в течении времени: \n')
    file.close()
    start = True
    anom = 0
    for i in column:
        if start:
            start = False
            continue
        if index_end+1 == len(column):
            break
        index_start += 1
        index_end += 1
        intermidiate_average = count_average(index_start, index_end, part, column)

        if intermidiate_average - average > confidence_interval:
            file = open("RESULT.txt", 'a', encoding='utf-8')
            str = column[index_end][0] + ': ' + column[index_end][1] + '\n'
            file.write(str)
            file.close()
            print('anomaly')
            print(column[index_end])
            anom += 1
    if anom==0:
        file = open("RESULT.txt", "a", encoding='utf-8')
        file.write('Данного типа аномалий не обнаружено. \n')
        file.close()
    print(anom)
    print('sec end')
    return anom


def third():
    print('th')
    column = search_main_charact.open_file()
    average = search_main_charact.average()
    number = search_main_charact.number_lines()
    confidence_interval = average *0.2
    part = round(number*0.05)
    print(part)
    index_start = 0
    index_end = part
    file = open("RESULT.txt", 'a', encoding='utf-8')
    file.write('Уменьшение среднего значения в течении времени: \n')
    file.close()
    start = True
    anom = 0
    for i in column:
        if start:
            start = False
            continue
        if index_end+1 == len(column):
            break
        index_start += 1
        index_end += 1
        intermidiate_average = count_average(index_start, index_end, part, column)

        if average - intermidiate_average > confidence_interval:
            file = open("RESULT.txt", 'a', encoding='utf-8')
            str = column[index_end][0] + ': ' + column[index_end][1] + '\n'
            file.write(str)
            file.close()
            print('anomaly')
            print(column[index_end])
            anom += 1
    if anom==0:
        file = open("RESULT.txt", "a", encoding='utf-8')
        file.write('Данного типа аномалий не обнаружено. \n')
        file.close()
    print(anom)
    print('th end')
    return anom


def func_activation(x):
    exp_in_mx = math.exp(x)
    res = 1/(1+exp_in_mx)
    return res


def train(w1, w2, column, part, Err, T, T_out):
    alpha = 0.1 #step for learning
    w1_re = []
    w2_re = []
    T_re = []
    h = [0, 0, 0, 0] # hidden
    for i in range(part):
        if i==len(column)-1: break
        for j in range(4):
            h[j] = float(column[i][1]) * w1[j] - T[j]
        sum_for_activaite = 0
        for j in range(4):
            sum_for_activaite=(h[j]*w2[j])
        sum_for_activaite -= T_out
        y_pr = func_activation(sum_for_activaite)
        err_y = y_pr - float(column[i+1][1])
        err_h = 0
        for j in range(4):
            err_h += (err_y*h[j]*(1-h[j])+w1[j])


        w1_re = w1
        w2_re = w2
        T_re = T
        for j in range(4):
            w1[j] = w1_re[j] - alpha * err_h * y_pr * (1 - y_pr) * h[j]
            # w2[j] = w2_re[j] - alpha * err_h * y_pr * (1 - y_pr)
            T[j] = T_re[j] - alpha * err_h * y_pr * (1 - y_pr)




def NN():

    column = search_main_charact.open_file()
    # 1 - input, output, 4 - hidden
    w1 = [] # input-hidden
    w2 = [] # hidden - output
    T = []
    T_out = 0
    for i in range(4):
        w1.append(round(random.uniform(0, 0.01), 3))
        w2.append(round(random.uniform(0, 0.01), 3))
        T.append(round(random.uniform(0, 0.01), 3))


    part = round(len(column) *0.2)
    average = search_main_charact.average()
    Err = average *0.05

    # train(w1, w2, column, part, Err, T, T_out)
    anom()


def anom():
    column = search_main_charact.open_file()
    aver = search_main_charact.average()
    part = aver * 0.03
    file = open("RESULT.txt", 'a', encoding='utf-8')
    file.write('Выход из доверительного интервала: \n')
    file.close()
    anom = 0
    for i in range(len(column)):
        if i == len(column) - 1: break
        val = abs(float(column[i][1])-float(column[i+1][1]))
        if val >part:
            file = open("RESULT.txt", 'a', encoding='utf-8')
            str = column[i+1][0] + ': ' + column[i+1][1] + '\n'
            file.write(str)
            file.close()
            anom +=1
            print('anomaly')
    if anom==0:
        file = open("RESULT.txt", "a", encoding='utf-8')
        file.write('Данного типа аномалий не обнаружено. \n')
        file.close()
    print('end')
    return anom


