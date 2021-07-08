import time
from colors import *


def shell_sort(data, draw_data, time_tick):
    gap = len(data) // 2
    while gap > 0:
        i = 0
        j = gap
        while j < len(data):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            i += 1
            j += 1
        while i - gap != -1:
            if data[i - gap] > data[i]:
                data[i - gap], data[i] = data[i], data[i - gap]
            i -= 1
        gap //= 2
        draw_data(data, [PURPLE for x in range(len(data))])
        time.sleep(time_tick)
    return draw_data(data, [BLUE for x in range(len(data))])