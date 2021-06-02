import math

import search_main_charact
import random
def startSearch():
    print('start search')
    count_anomaly = 0
    return count_anomaly

def firstType():
    print('first')
    column = search_main_charact.open_file()
    number_lines = search_main_charact.number_lines()
    # если на интервале равному 4% одинаковые значение - аномалия
    part = round(number_lines*0.04)

    pair_start = column[0]
    pair_end = column[0]

    list_with_anomaly = []

    # если count == part - фномальный отрезок
    count = 0

    work_val = float(column[0][1])
    count_anomaly = 0
    for i in column:
        if work_val == float(i[1]):
            count+=1
            pair_end = i
            if count >= part:
                print('anomaly')
                str = pair_start[0] + ' - ' + pair_end[0]
                print(str)
                count_anomaly+=1
        else:
            count = 1
            work_val = float(i[1])
            pair_start = i
            pair_end = i
    print(count_anomaly)
    print('end')

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
            print('anomaly')
            print(column[index_end])
            anom += 1

    print(anom)
    print('sec end')


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
            print('anomaly')
            print(column[index_end])
            anom += 1

    print(anom)
    print('th end')


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
        print(y_pr, ' ', column[i+1][1])
        err_y = y_pr - float(column[i+1][1])
        err_h = 0
        for j in range(4):
            err_h += (err_y*h[j]*(1-h[j])+w1[j])
        print(err_h)

        w1_re = w1
        w2_re = w2
        T_re = T
        for j in range(4):
            w1[j] = w1_re[j] - alpha * err_h * y_pr * (1 - y_pr) * h[j]
            # w2[j] = w2_re[j] - alpha * err_h * y_pr * (1 - y_pr)
            T[j] = T_re[j] - alpha * err_h * y_pr * (1 - y_pr)




def NN():
    print('start nn')
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
    print(w1, ' ', w2)

    part = round(len(column) *0.2)
    average = search_main_charact.average()
    Err = average *0.05

    train(w1, w2, column, part, Err, T, T_out)


    print('end nn')





