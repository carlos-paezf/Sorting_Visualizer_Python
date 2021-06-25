import time
from colors import *


def bubble_sort(data, draw_data, time_tick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw_data(data, [YELLOW if x == j or x == j+1 else BLUE for x in range(len(data))])
                time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])