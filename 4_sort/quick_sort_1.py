def quick_sort(arr):
    q_sort(arr, 0, len(arr) - 1)


def q_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)

        q_sort(arr, left, pivot_index - 1)
        q_sort(arr, pivot_index + 1, right)


def partition(arr, left, right):
    pivot = arr[left]

    while left < right:
        # 如果列表后边的数比基准数大或相等, 则前移一位直到有比基准数小的数出现
        while left < right and arr[right] >= pivot:
            right -= 1
        # 如找到, 则把第 right 个元素赋值给 left 位置,此时表中 left 和 right 的元素相等
        arr[left] = arr[right]
        # # 减少下一个循环的一次比较
        # if left < right:
        #     left += 1

        # 同样的方式比较前半区
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
        # if left < right:
        #     right -= 1

    # 做完一轮比较之后, 列表被分成了两个半区, 并且 left=right , 需要将这个数设置回 pivot
    arr[left] = pivot
    return left


def partition_1(arr, low, high):
    pivot = arr[high]
    store_index = low  # 位置 store_index 存储较小元素

    for i in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[i] < pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]

    return store_index


if __name__ == '__main__':
    # arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    arr = [5, 9, 1, 11, 6, 7, 2, 4]
    quick_sort(arr)
    print(arr)
