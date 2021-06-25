import time
from colors import *


def insertion_sort(data, draw_data, time_tick):
    for i in range(len(data)):
        temp = data[i]
        j = i
        while j > 0 and temp < data[j-1]:
            data[j] = data[j-1]
            j -= 1
        data[j] = temp
        draw_data(data, [LIGHT_GREEN if x == j or x == i else BLUE for x in range(len(data))])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])