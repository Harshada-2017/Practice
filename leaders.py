def leaders(arr):
    result = []
    largest = arr[-1]
    result.append(largest)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > largest:
            largest = arr[i]
            result.append(largest)

    result.reverse()
    return result

print(leaders([16, 17, 4, 3, 5, 2]))