numbers = list(map(int, input("Enter numbers: ").split()))

visited = []

for i in range(len(numbers)):
    if numbers[i] not in visited:
        frequency = 0

        for j in range(len(numbers)):
            if numbers[i] == numbers[j]:
                frequency = frequency + 1

        print(numbers[i], "appears", frequency, "times")
        visited.append(numbers[i])