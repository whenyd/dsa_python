def merge_sort(arr):
    """O(nlogn)"""
    size = len(arr)
    if size < 2:
        return arr

    middle = size // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    together = merge(left, right)

    return together


def merge(left, right):
    size_left = len(left)
    size_right = len(right)
    result = []

    i, j = 0, 0
    while i < size_left and j < size_right:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < size_left:
        result.extend(left[i:])

    if j < size_right:
        result.extend(right[j:])

    return result


if __name__ == '__main__':
    arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    ans = merge_sort(arr)
    print(ans)
