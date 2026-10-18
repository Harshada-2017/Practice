numbers = list(map(int, input().split()))
result = []
zeros = 0

for num in numbers:
    if num == 0:
        zeros += 1
    else:
        result.append(num)

for i in range(zeros):
    result.append(0)

print(result)