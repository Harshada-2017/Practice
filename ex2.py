def solution(arr):
    freq = {}

    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    counts = sorted(set(freq.values()), reverse=True)

    if len(counts) < 2:
        return -1

    second = counts[1]
    answer = float('inf')

    for i in freq:
        if freq[i] == second and i < answer:
            answer = i

    return answer