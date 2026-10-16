def solution(nums):
    max_count = 0
    answer = nums[0]

    for i in nums:
        count = 0

        for j in nums:
            if i == j:
                count += 1

        if count > max_count:
            max_count = count
            answer = i
        elif count == max_count and i < answer:
            answer = i

    return answer