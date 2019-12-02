def binary_search_recursive(arr, e):
    return bsearch(arr, e, 0, len(arr)-1)


def bsearch(arr, e, low, high):
    mid = low + (high - low) // 2  # (low+high)/2可能溢出

    val = arr[mid]
    if val == e:
        return mid
    elif val > e:
        return bsearch(arr, e, low, mid - 1)
    else:                                                                                                                                                                                                                                                                                                                                   
        return bsearch(arr, e, mid + 1, high)


def binary_search_loop(arr, e):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        val = arr[mid]
        if val == e:
            return mid
        elif val > e:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    arr = [1, 3, 5, 6, 7]
    print(binary_search_loop(arr, 5))
