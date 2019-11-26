def bubble_sort(arr):
    size = len(arr)
    if size < 2:
        return arr

    for i in range(size - 1):
        for j in range(i + 1, size):
            left = arr[i]
            right = arr[j]
            if left > right:
                arr[i], arr[j] = right, left


def selection_sort(arr):
    size = len(arr)
    if size < 2:
        return arr

    for i in range(size-1):
        min_index = i
        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    size = len(arr)
    if size < 2:
        return arr

    for i in range(1, size):
        pre_index = i - 1
        current = arr[i]  # 存储current

        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index+1] = arr[pre_index]  # 移动较大元素
            pre_index -= 1
        arr[pre_index+1] = current  # 插入current


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    insertion_sort(arr)
    print(arr)
