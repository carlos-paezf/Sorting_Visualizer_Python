import time
from colors import *


def bucket_sort(data, n_buckets, draw_data, time_tick):
    max_element = max(data)
    min_element = min(data)
    ran = (max_element - min_element) / n_buckets
    temp = []
    for i in range(n_buckets):
        temp.append([])
    for i in range(len(data)):
        diff = (data[i] - min_element) / ran - int((data[i] - min_element) / ran)
        if diff == 0 and data[i] != min_element:
            temp[int((data[i] - min_element) / ran) - 1].append(data[i])
        else:
            temp[int((data[i] - min_element) / ran)].append(data[i])
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                data[k] = i
                k += 1
                draw_data(data, [LIGHT_GREEN for x in range(len(temp))])
                time.sleep(time_tick)
    return draw_data(data, [BLUE for x in range(len(data))])