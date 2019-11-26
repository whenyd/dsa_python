def counting_sort(arr, maximum):
    count = [0 for i in range(maximum+1)]
    ans = []

    for i in arr:
        count[i] += 1

    for i, val in enumerate(count):
        ans.extend([i]*val)

    return ans


if __name__ == '__main__':
    arr = [2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2]
    ans = counting_sort(arr, 9)
    print(ans)
