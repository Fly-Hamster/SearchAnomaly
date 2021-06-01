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



