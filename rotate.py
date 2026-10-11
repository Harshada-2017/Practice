numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation count: "))

n = len(numbers)

if n > 0:
    k = k % n

    for i in range(k):
        last = numbers[n - 1]

        for j in range(n - 1, 0, -1):
            numbers[j] = numbers[j - 1]

        numbers[0] = last

print(numbers)