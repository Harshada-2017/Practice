numbers = list(map(int, input().split()))
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

maximum = 0
answer = numbers[0]

for num in frequency:
    if frequency[num] > maximum:
        maximum = frequency[num]
        answer = num

print("Element:", answer)
print("Frequency:", maximum)