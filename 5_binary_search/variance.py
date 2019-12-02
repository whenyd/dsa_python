def binary_search_first(arr, e):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        val = arr[mid]
        if val >= e:
            high = mid - 1
        else:
            low = mid + 1

    # 当查找的值不存在, 且大于最大值时, low==len(arr)
    if low < len(arr) and arr[low] == e:  #
        return low
    else:
        return -1


def binary_search_last(arr, e):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        val = arr[mid]
        if val <= e:
            low = mid + 1
        else:
            high = mid - 1

    # 当查找的值不存在, 且比最小元素小时, high==-1
    # 不过, Python中索引-1是最后一个元素, 可以省略 high>=0
    if high >= 0 and arr[high] == e:
        return high
    else:
        return -1


def binary_search_first_readable(arr, e):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        val = arr[mid]
        if val > e:
            high = mid - 1
        elif val < e:
            low = mid + 1
        else:
            if mid == 0 or arr[mid-1] < e:
                return mid
            else:
                high = mid - 1

    return -1


def binary_search_last_readable(arr, e):
    highest = len(arr) - 1
    low = 0
    high = highest

    while low <= high:
        mid = low + (high-low)//2
        val = arr[mid]
        if val > e:
            high = mid - 1
        elif val < e:
            low = mid + 1
        else:
            if mid == highest or arr[mid + 1] > e:
                return mid
            else:
                low = mid + 1

    return -1


def first_more_or_equal(arr, e):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high-low)//2
        val = arr[mid]
        if val < e:
            low = mid + 1
        else:
            if mid == 0 or arr[mid-1] < e:
                return mid
            else:
                high = mid - 1

    return -1


def last_less_or_equal(arr, e):
    highest = len(arr) - 1
    low = 0
    high = highest

    while low <= high:
        mid = low + (high-low)//2
        val = arr[mid]
        if val > e:
            high = mid - 1
        else:
            if mid == highest or arr[mid+1] > e:
                return mid
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':
    arr = [1, 3, 5, 6, 6]
    print(first_more_or_equal(arr, 4))
    print(last_less_or_equal(arr, 5))
