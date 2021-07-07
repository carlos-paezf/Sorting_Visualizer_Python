from tkinter import *
from tkinter import ttk
import random

from colors import *
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort
from algorithms.quickSort import quick_sort
from algorithms.countingSort import counting_sort
from algorithms.radixSort import radix_sort
from algorithms.heapSort import heap_sort


root = Tk()
root.title('Sorting Algorithms Visualization')
root.maxsize(1000, 700)
root.config(bg = WHITE)


algorithm_name = StringVar()
algorithm_list = [
    'Bubble Sort', 
    'Merge Sort', 
    'Selection Sort', 
    'Insertion Sort', 
    'Quick Sort', 
    'Counting Sort', 
    'Radix Sort', 
    'Heap Sort'
]

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []


def draw_data(data, colorArray):
    canvas.delete('all')
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 3
    normalizedData = [i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 395
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    root.update_idletasks()


def generate():
    global data
    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)
    draw_data(data, [BLUE for x in range(len(data))])


def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


def sort():
    global data
    time_tick = set_speed()
    if algorithm_menu.get() == 'Bubble Sort':
        bubble_sort(data, draw_data, time_tick)
    elif algorithm_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, draw_data, time_tick)
    elif algorithm_menu.get() == 'Selection Sort':
        selection_sort(data, draw_data, time_tick)
    elif algorithm_menu.get() == 'Insertion Sort':
        insertion_sort(data, draw_data, time_tick)
    elif algorithm_menu.get() == 'Quick Sort':
        quick_sort(data, 0, len(data)-1, draw_data, time_tick)
    elif algorithm_menu.get() == 'Counting Sort':
        counting_sort(data, draw_data, time_tick)
    elif algorithm_menu.get() == 'Radix Sort':
        radix_sort(data, draw_data, time_tick)
    elif algorithm_menu.get() == 'Heap Sort':
        heap_sort(data, draw_data, time_tick)
    else: 
        pass


UI_frame = Frame(root, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)


l1 = Label(UI_frame, text='Algorithm: ', bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algorithm_menu = ttk.Combobox(UI_frame, textvariable=algorithm_name, values=algorithm_list)
algorithm_menu.grid(row=0, column=1, padx=5, pady=5)
algorithm_menu.current(0)


l2 = Label(UI_frame, text='Sorting Speed: ', bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)


b1 = Button(UI_frame, text='Generate Array', command=generate, bg=LIGHT_GRAY, width=20)
b1.grid(row=2, column=0, padx=5, pady=5)

b2 = Button(UI_frame, text='Sort', command=sort, bg=LIGHT_GRAY, width=20)
b2.grid(row=2, column= 1, padx=5, pady=5)


canvas = Canvas(root, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


root.mainloop()