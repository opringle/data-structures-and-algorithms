def bubble_sort(array):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def selection_sort(array):
    for i in range(0, len(array) - 1):
        smallest_value = float('inf')
        for j in range(i, len(array)):
            value = array[j]
            if value < smallest_value:
                smallest_value = value
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]
    return array

def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

def quick_sort(arr):
    if len(arr) == 1:
        return arr

    # select a pivot at random
    pivot_idx = random.choice([i for i in range(arr)])

    # move pivot to the end
    arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]

    # intialize pointers
    left_pointer, right_pointer = 0, len(arr) - 1

    item_from_left, item_from_right = None, None
    while left_pointer <= right_pointer or item_from_left and item_from_right:
        if arr[left_pointer] > arr[pivot_idx]:
            item_from_left = arr[left_pointer]
            item_from_left_idx = left_pointer
        else:
            left_pointer += 1

        if arr[right_pointer] < arr[pivot_idx]:
            item_from_right = arr[right_pointer]
            item_from_right_idx = right_pointer
        item_from_left += 1
        item_from_right -= 1
    
    
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
  
    for j in range(low, high):
  
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
  
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
  
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
  
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
  
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


if __name__ == '__main__':
    arr = [3,2,4,21,1,90,-5]
    print('arr = {}'.format(arr))
    bubble_sorted_arr = bubble_sort(arr)
    print('bubble_sorted_arr = {}'.format(bubble_sorted_arr))

    arr = [3,2,4,21,1,90,-5]
    print('arr = {}'.format(arr))
    selection_sorted_arr = selection_sort(arr)
    print('selection_sorted_arr = {}'.format(selection_sorted_arr))

    arr = [3,2,4,21,1,90,-5]
    print('arr = {}'.format(arr))
    merge_sort(arr, left_index=0, right_index=len(arr))
    print('merge_sorted_array = {}'.format(arr))

    arr = [3,2,4,21,1,90,-5]
    print('arr = {}'.format(arr))
    quickSort(arr, low=0, high=len(arr)-1)
    print('quick_sort = {}'.format(arr))
