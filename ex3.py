def solution(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    highest = 0
    lowest = len(arr)

    for i in freq:
        if freq[i] > highest:
            highest = freq[i]

        if freq[i] < lowest:
            lowest = freq[i]

    return highest + lowest