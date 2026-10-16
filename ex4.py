def solution(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    return freq

print(solution([1, 2, 2, 3, 3, 3]))