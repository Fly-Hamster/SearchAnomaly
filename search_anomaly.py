import search_main_charact
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
