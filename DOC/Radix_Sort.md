# Radix Sort

Quick Sort, Merge Sort, Heap Sort is comparison-based sorting algorithms. Count Sort is not a comparison-based algorithm. It has the complexity of *O(n+k)*, where *k* is the maximum element of the input array. 

So, if *k* is *O(n)*, Count Sort becomes linear sorting, which is better than comparison-based sorting algorithms that have *O(N log N)* time complexity. The idea is to extend the Count Sort algorithm to get a better time-complexity when *k* goes *O(n^2)*. Here comes the idea of Radix Sort.

## Algorithm

For each digit i where i varies from the least significant digit to the most significant digit of a number. Sort input array using count sort algorithm according to ith digit. We used count sort because it is a stable sort.

<p align="center">
    <img src="../images/radix_sort.png" />
</p>

## Example

Assume the input array is `A = [10, 21, 17, 34, 44, 11, 654, 123]`. Based on the algorithm, we will sort the input array according to the one's digit (least significant digit).

|||||
|---|---|---|---|
|0:|10|
|1:|21|11|
|2:|
|3:|123|
|4:|34|44|654|
|5:|
|6:|
|7:|17|
|8:|
|9:|

So, the array becomes `A = [10, 21, 11, 123, 24, 44, 654, 17]`. Now, we'll sort according to the ten's digit:

|||||
|---|---|---|---|
|0:|
|1:|10|11|17|
|2:|21|123|
|3:|34|
|4:|44|
|5:|654|
|6:|
|7:|
|8:|
|9:|

Now, the array becomes: `A = [10, 11, 17, 21, 123, 34, 44, 654]`. Finally, we sort according to the hundred's digit (most significant digit):

||||||||
|---|---|---|---|---|---|---|
|0:|010|011|017|021|034|044|
|1:|123|
|2:|
|3:|
|4:|
|5:|
|6:|654|
|7:|
|8:|
|9:|

The array becomes: `A = [10, 11, 17, 21, 34, 44, 123, 654]` which is sorted. This is how our algorithm works.


## Implementation

```python
def count_sort(data, place, draw_data, time_tick):
    n = len(data)
```

The output array elements that will have sorted array.
```python
    output = [0] * (n)
```

Initialize count array as 0
```python
    count = [0] * (10)
```

Store count of occurences in count[]
```python
    for i in range(n):
        index = (data[i]/place)
        count[int(index % 10)] += 1
```

Change count[i] so that count[i] now contains actual position of this digit is output array. 
```python
    for i in range(1, 10):
        count[i] += count[i-1]
```

Build the output array.
```python
    i = n - 1
    while i >= 0:
        index = (data[i] / place)
        output[count[int(index%10)] - 1] = data[i]
        count[int(index % 10)] -= 1
        i -= 1
```

Copying the output array to data[], so that array now contains sorted numbers.
```python
    i = 0
    for i in range(len(data)):
        data[i] = output[i]
```

Method to do Radix Sort
```python
def radix_sort(data, draw_data, time_tick):
```

Find the maximum number to know number of digits.
```python
    maxi = max(data)
```

Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i where i is current digit number. 
```python
    exp = 1
    while maxi/exp > 0:
        count_sort(data, exp, draw_data, time_tick)
        exp *= 10
```

Draw the data being compared and the finalized.
```python
        draw_data(data, [LIGHT_GRAY for x in range(len(data))])
        time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])
```

