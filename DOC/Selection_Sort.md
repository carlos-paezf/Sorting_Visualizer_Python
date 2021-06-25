# Selection Sort

The selection sort algorithm is based on the idea of finding the minimum or maximum element in an unsorted array and then putting it in its correct position in a sorted array. 

Assume that the array A = [7, 5, 4, 2] needs to be sorted in ascending order. 

The minimum element in the array i.e. 2 is searched for and then swapped with the element that is currently located at the first position, i.e. 7. Now the minimum element in the remaining unsorted array is searched for and put in the second position, and so on. 

<p align="center">
    <img src="../images/selection_sort.png" />
</p>

Let's take a look at the implementation. 

```python
def selection_sort(data, draw_data, time_tick):
    size = len(data)
```

Reduces the effective size if the array by one in each iteration. 
```python
    for i in range(size-1):
```

Assuming the first element to be the minimum of the unsorted array.
```python
        minimum = i
```

Gives the effective size of the unsorted array.
```python
        for j in range(i+1, size):
```

Finds the minimum element
```python
            if data[j] < data[minimum]:
                minimum = j
```

Putting minimum element on its proper position
```python
        data[minimum], data[i] = data[i], data[minimum]
```

Draw the data being compared and the finalized.
```python
        draw_data(data, [YELLOW if x == minimum or x == 1 else BLUE for x in range(size)])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(size)])
```