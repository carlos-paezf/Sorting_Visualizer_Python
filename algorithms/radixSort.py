import time
from colors import *


def count_sort(data, place, draw_data, time_tick):
    n = len(data)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(n):
        index = (data[i]/place)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i-1]
    i = n - 1
    while i >= 0:
        index = (data[i] / place)
        output[count[int(index%10)] - 1] = data[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    for i in range(len(data)):
        data[i] = output[i]


def radix_sort(data, draw_data, time_tick):
    maxi = max(data)
    exp = 1
    while maxi/exp > 0:
        count_sort(data, exp, draw_data, time_tick)
        exp *= 10
        draw_data(data, [LIGHT_GRAY for x in range(len(data))])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])