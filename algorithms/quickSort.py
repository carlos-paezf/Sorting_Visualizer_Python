import time
from colors import *


def partition(data, start, end, draw_data, time_tick):
    i = start + 1
    pivot = data[start]
    for j in range(start+1, end+1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[start], data[i-1] = data[i-1], data[start]
    return i - 1


import random 
def rand_partition(data, start, end, draw_data, time_tick):
    rand = start + random.randrange(end - start + 1)
    data[rand], data[start] = data[start], data[rand]
    return partition(data, start, end, draw_data, time_tick)


def quick_sort(data, start, end, draw_data, time_tick):
    if start < end:
        #pivot_position = partition(data, start, end, draw_data, time_tick)
        pivot_position = rand_partition(data, start, end, draw_data, time_tick)
        quick_sort(data, start, pivot_position-1, draw_data, time_tick)
        quick_sort(data, pivot_position+1, end, draw_data, time_tick)
        draw_data(data, [PURPLE if x >= start and x < pivot_position else YELLOW if x ==
                            pivot_position else DARK_BLUE if x > pivot_position and x <= end else BLUE for x in range(len(data))])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])