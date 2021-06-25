# Merge Sort

Merge Sort is a divide-and-conquer algorithm based on the idea of breaking down a list into several sub-list until each sublist consists of a single element and merging those sublists in a manner that results in a sorted list.

- Divide the unsorted list into N sublists, each containing 1 element.
- Take adjacent pairs of two singleton lists and merge them to form a list of 2 elements.
- Repeat the process till a single list of obtained. 

While comparing two sublists for merging, the first element of both lists is taken into consideration. While sorting is ascending order, the element that is of a lesser value becomes a new element of the sorted list. This procedure is repeated until both the smaller sublists are empty and the new combined sublist comprises all the elements of both the sublists. 

<p align="center">
    <img src="../images/merge_sort.jpg"/>
</p>

As one may understand from the image above, at each step a list of size M is being divided into 2 sublists of size M/2, until no further division can be done. To understand better, consider a smaller array A containing the elements (9, 7, 8). 

At the first step, this list of size 3 is divided into 2 sublists the first consisting of elements (9, 7) and the second one being (8). Now, the first list consisting of elements (9, 7) is further divided into 2 sublists consisting of elements (9) and (7) respectively. 

As no further breakdown of this list can be done, as each sublist consists of a maximum of 1 element, we now start to merge these lists. The 2 sub-list formed in the last step are then merged together in sorted order using the procedure mentioned above leading to a new list (7, 9). Backtracking further, we then need to merge the list consisting of element (8) too with this list, leading to the new sorted list (7, 8, 9). 

```python
def merge(data, start, mid, end, draw_data, time_tick):
```

Stores the starting position of both parts in temporary variables.
```python
    p = start
    q = mid + 1
    temp_array = []
```

- Checks if the first part comes to an end or not
- Checks if the second part comes to an end or not
- Checks which part has a smaller element
```python
    for i in range(start, end+1):
        if p > mid:
            temp_array.append(data[q])
            q += 1
        elif q > end:
            temp_array.append(data[p])
            p += 1
        elif data[p] < data[q]:
            temp_array.append(data[p])
            p += 1
        else:
            temp_array.append(data[q])
            q += 1
```

Now the real array has elements in a sorted manner including both parts.
```python
    for p in range(len(temp_array)):
        data[start] = temp_array[p]
        start += 1
```

Here, in the merge function, we will merge two parts of the arrays where one part has starting and ending positions from start to mid respectively and another part has positions from `mid+1` to the end. 

A beginning is made from the starting parts of both arrays, i.e. p and q. Then the respective elements of both the parts are compared and the one with the smaller value will be stored in the auxiliary array. If at some condition, one part comes to end, then all the elements of another part of the array are added in the auxiliary array in the same order the exist. 

Now consider the following 2 branched recursive function:

```python
def merge_sort(data, start, end, draw_data, time_tick):
    if start < end:
```

Defines the current array in 2 parts. 
```python
        mid = int((start + end) / 2)
```

Sort the first part of the array.
```python
        merge_sort(data, start, mid, draw_data, time_tick)
```

Sort the second part of the array.
```python
        merge_sort(data, mid+1, end, draw_data, time_tick)
```

Merge the both parts by comparing elements of both the parts
```python
        merge(data, start, mid, end, draw_data, time_tick)
```

Draw the data being compared and the finalized.
```python
        draw_data(data, [PURPLE if x >= start and x < mid else YELLOW if x ==
                        mid else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])
```

