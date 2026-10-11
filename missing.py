numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers) + 1

expected_sum = n * (n + 1) // 2

actual_sum = 0

for i in range(len(numbers)):
    actual_sum = actual_sum + numbers[i]

missing = expected_sum - actual_sum

print("Missing number:", missing)