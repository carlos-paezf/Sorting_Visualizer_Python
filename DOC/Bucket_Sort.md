# Bucket Sort

Bucket Sort is a comparison sort algorithm that operates on elements by dividing them into different buckets and then sorting these buckets individually. Each bucket is sorted individually using a separate sorting algorithm or by applying the bucket sort algorithm recursively. Bucket sort is mainly useful when the input es uniformly distributed over a range.

Assume one has the following problem in front of them:

One has been given a large array of floating-point integers lying uniformly between the lower and upper bound. This array now needs to be sorted. A simple way to solve this problem would be to use another sorting algorithm such as Merge sort, Heap sort, or Quicksort. However, these algorithms guarantee a best case time complexity of *O(N log N)* However, using bucket sort, the above task can be completed in *O(N)* time. Let's have a closes look at it.

Consider one needs to create an array of lists, i.e of buckets. Elements now need to be inserted into these buckets on the basis of their properties. Each of these buckets can then be sorted individually using Insertion Sort.

## Implementation

Bucket sort for numbers having interger part

```python
def bucket_sort(data, n_buckets, draw_data, time_tick):
    max_element = max(data)
    min_element = min(data)
```

Range for buckets

```python
    ran = (max_element - min_element) / n_buckets
    temp = []
```

Create empty buckets.

```python
    for i in range(n_buckets):
        temp.append([])
```

Scatter the array elements into the correct bucket.

```python
    for i in range(len(data)):
        diff = (data[i] - min_element) / ran - int((data[i] - min_element) / ran)
```

Append the boundary elements to the lower array.

```python
        if diff == 0 and data[i] != min_element:
            temp[int((data[i] - min_element) / ran) - 1].append(data[i])
        else:
            temp[int((data[i] - min_element) / ran)].append(data[i])
```

Sort each bucket individually.

```python
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
```

Gather sorted elements to the original array.

```python
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                data[k] = i
                k += 1
```

Draw the data being compared and the finalized.

```python
                draw_data(data, [LIGHT_GREEN for x in range(len(temp))])
                time.sleep(time_tick)
    return draw_data(data, [BLUE for x in range(len(data))])
```

## Example

<p align="center">
    <img src="../images/bucket_sort.png" />
</p>