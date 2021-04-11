def binary_search(array, start: int, end: int, target: int):
    if start > end:
        return -1

    mid_idx = (end + start + 1) // 2
    if target < array[mid_idx]:
        return binary_search(array, start, mid_idx - 1, target)
    elif target == array[mid_idx]:
        return mid_idx
    else:
        return binary_search(array, mid_idx+1, end, target)

if __name__ == '__main__':
    arr = sorted([1,3,2,5,4,6,7,8,9,10])
    target = 4
    print('{} exists at index {} in {}'.format(
        target, binary_search(arr, 0, len(arr)-1, target), arr
    ))