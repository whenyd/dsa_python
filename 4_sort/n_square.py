def bubble_sort(arr):
    size = len(arr)
    if size < 2:
        return arr

    for i in range(size - 1):
        for j in range(i + 1, size):
            left = arr[i]
            right = arr[j]
            # 比较相邻的两个元素, 较小元素向上冒泡
            # 实际效果是每次循环之后, 最大元素都被移动到最后
            if left > right:
                arr[i], arr[j] = right, left


def selection_sort(arr):
    size = len(arr)
    if size < 2:
        return arr

    for i in range(size-1):
        min_index = i
        for j in range(i+1, size):
            # 选择未排序元素中的最小元素
            if arr[j] < arr[min_index]:
                min_index = j

        # 将最小元素置于已排序部分的末尾
        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    size = len(arr)
    if size < 2:
        return arr

    # 从1开始
    for i in range(1, size):
        pre_index = i - 1
        current = arr[i]  # 存储current

        # 从已排序部分的末尾开始, 往前移动当前元素
        # 直到当前元素正确排序
        while pre_index >= 0 and current < arr[pre_index]:
            arr[pre_index+1] = arr[pre_index]  # 移动较大元素
            pre_index -= 1
        arr[pre_index+1] = current  # 插入current


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    insertion_sort(arr)
    print(arr)
