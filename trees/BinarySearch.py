def binary_search(array, target):
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2
        if array[middle] < target:
            start = middle + 1
        elif array[middle] > target:
            end = middle - 1
        else:
            return middle

    return None


def binary_search_recur(array, target, left, right):
    if left > right:
        return None

    mid = (left + right) // 2

    if array[mid] > target:
        return binary_search_recur(array, target, left, mid - 1)
    elif array[mid] < target:
        return binary_search_recur(array, target, mid + 1, right)
    else:
        return mid


data = [i**2 for i in range(1, 10)]

target = 9
idx = binary_search(data, target)
# idx = binary_search_recur(data, target, 0, len(data) - 1)

if idx:
    print(f'index : {idx}, data : {data[idx]}')
else:
    print(f'Failed to find the data of {target}')
