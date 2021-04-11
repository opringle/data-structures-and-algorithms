# Sorting

Merge sort, quick sort and bucket sort are the most common sorting algorithms used in interviews.

## Bubble Sort

O(n^2) runtime & O(1) memory. In bubble sort, we start from the first index in the array. If the value is less than the next value we leave them, else we swap. We stop when we are at the penultimate element in the array. This process repeats on the next index until the array is sorted. The smaller items 'bubble' up to the top of the list.

## Selection Sort

O(n^2) runtime & O(1) memory. Scan the list for the smallest element, then swap it with the first value. Then find the second smallest and move it. Repeat for all indices.

## Merge Sort

O(nlogn) average & worst case runtime & O(n) memory. This algorithm divides the array in half repeatedly until each element is in a separate list. It then merges pairs of lists and sorts them.

## Quick Sort

O(nlogn) ave runtime & O(n^2) worst case. O(log(n)) memory. 

- Choose a pivot
- Swap pivot with last value
- Initialize two pointers
- itemFromLeft = first item from left > pivot
- itemFromRight = first item from right < pivot 
- Swap itemFromLeft and itemFromRight
- Move pointers in
- Stop when pointers cross
- Swap itemFromLeft with pivot. Now all items to the left of pivot are smaller and all items from right are larger. Pivot is in the right place. 

# Searching

## Binary Search

Sort the array. Compare target to middle of array. If less than, binary search elements before the middle, else binary search elements from middle onwards. Repeat until target is found or subarray has no length.

```python
def binary_search(array, start: int, end: int, target: int):
    if len(array) == 0:
        return -1

    mid_idx = (end - start + 1) // 2
    if target < array[mid_idx]:
        return self.binary_search(array, start, mid_idx - 1, target)
    elif target == array[mid_idx]:
        return mid_idx
    else:
        return self.binary_search(array, mid_idx+1, end, target)

```





