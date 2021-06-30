import time
from colors import *


def counting_sort(data, draw_data, time_tick):
    n = max(data) + 1
    aux = [0] * n
    for item in data:
        aux[item] += 1
    k = 0
    for i in range(n):
        for j in range(aux[i]):
            data[k] = i
            draw_data(data, [DARK_BLUE for x in range(len(data))])
            time.sleep(time_tick)
            k += 1
    draw_data(data, [BLUE for x in range(len(data))])