n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    numbers.append(int(input("Enter number: ")))

unique = list(set(numbers))
unique.sort()

if len(unique) >= 2:
    print("Second largest:", unique[-2])
else:
    print("No second largest number")