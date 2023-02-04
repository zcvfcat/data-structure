def binary_search(li, target):
    start = 0
    end = len(li) - 1

    while start <= end:
        middle = (start + end) // 2
        if li[middle] < target:
            start = middle + 1
        elif li[middle] > target:
            end = middle - 1
        else:
            return middle

    return None


data = [i**2 for i in range(1, 10)]

target = 9
idx = binary_search(data, target)

if idx:
    print(f'index : {idx}, data : {data[idx]}')
else:
    print(f'Failed to find the data of {target}')
