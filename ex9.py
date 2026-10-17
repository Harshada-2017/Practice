numbers = list(map(int, input().split()))
highest = 0
answer = numbers[0]

for num in numbers:
    frequency = 0

    for item in numbers:
        if item == num:
            frequency += 1

    if frequency > highest:
        highest = frequency
        answer = num

print("Element:", answer)
print("Frequency:", highest)