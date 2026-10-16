def solution(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    highest = max(freq.values())
    answer = min(i for i in freq
                 if freq[i] == highest)

    return answer

print(solution([1, 2, 2, 3, 3, 3]))