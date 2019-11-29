def _quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array if x < pivot]
        more_than_pivot = [x for x in array if x > pivot]

        return _quick_sort(less_than_pivot)+[pivot]+_quick_sort(more_than_pivot)


def quick_sort(arr):
    q_sort(arr, 0, len(arr))


def q_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        q_sort(arr, low, pivot_index)
        q_sort(arr, pivot_index+1, high)


def partition(arr, low, high):
    """
    for each (unsorted) partition
    set first element as pivot
      storeIndex = pivotIndex + 1
      for i = pivotIndex + 1 to rightmostIndex
        if element[i] < element[pivot]
          swap(i, storeIndex); storeIndex++
      swap(pivot, storeIndex - 1)
    """
    pivot = arr[low]
    store_index = low + 1

    for i in range(low+1, high):
        if arr[i] < pivot:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1

    # 交换pivot和store_index-1的值, 使得pivot之前的元素小于等于pivot
    arr[low], arr[store_index - 1] = arr[store_index - 1], arr[low]

    return store_index - 1


if __name__ == '__main__':
    # arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    arr = [5, 9, 1, 11, 6, 7, 2, 4]
    quick_sort(arr)
    print(arr)
