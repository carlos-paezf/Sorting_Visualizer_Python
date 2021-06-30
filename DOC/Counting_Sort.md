# Counting Sort

In Counting Sort, the frequencies of distinct elements of the array to be sorted are counted and stored in an auxiliary array, by mapping its values as an index of the auxiliary array. 

Let's assume that, array A of size N needs to be sorted.

- Initialize the auxiliary array Aux[] as 0. 
  >*Note:* The size of this array should be >= max(A[])
- Traverse array A and store the count of occurrence of each element in the appropriate index of the Aux array, which means, execute Aux[A[i]]++ for each i, where i ranges from [0, N-1]
- Initialize the empty array sortedA[]
- Traverse array Aux and copy i into sortedA for Aux[i] number of times where 0 <= i <= max(A[]).

The array A can be sorted by using this algorithm only if the maximum value in array A is less than the maximum size of the array Aux. Usually, it is possible to allocate memory up to the order of a million (10^6). If the maximum value of A exceeds the maximum memory allocation size, it is recommended that you do not use this algorithm. Use either the quick sort or merge sort algorithm. 


```python
def counting_sort(data, draw_data, time_tick):
```

First, find the maximun value in data or A[].
```python
    n = max(data) + 1
```

Initialize the elements of auxiliary array with 0.
```python
    aux = [0] * n
```

Store the frequencies of each distinct element of data, by mapping its value as the index of the auxiliary array
```python
    for item in data:
        aux[item] += 1
```

The auxiliary array store which element occurs how many times, add i in data sorted according to the number of times i occurred in data or A[]
```python
    k = 0
    for i in range(n):
        for j in range(aux[i]):
            data[k] = i
            k += 1
```

Draw the data being compared and the finalized.
```python
            draw_data(data, [BLUE for x in range(len(data))])
            time.sleep(time_tick)
    draw_data(data, [BLUE for x in range(len(data))])
```

Example: 

Say `A = [5, 7, 5, 2, 1, 1]`. 

Aux will be of the size 7+1 i.e. 8. `Aux = [0, 2, 1, 0, 0, 2, 0, 1]`. 

Notice that `Aux[1] = 2` which represents the number of ocurrences of 1 in A[]. Similarly `Aux[5] = 2` which represents the number occurrences of 5 in A[]. 

After applying the counting sort algorithm, sortedA[] will be `sortedA = [1, 1, 2, 5, 5, 7]`.

<p align="center">
    <img src="../images/counting_sort.png" />
</p>