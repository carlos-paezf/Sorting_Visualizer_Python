import time
from colors import *


def selection_sort(data, draw_data, time_tick):
    size = len(data)
    for i in range(size-1):
        minimum = i
        for j in range(i+1, size):
            if data[j] < data[minimum]:
                minimum = j
        data[minimum], data[i] = data[i], data[minimum]
        draw_data(data, [YELLOW if x == minimum or x == 1 else BLUE for x in range(size)])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(size)])