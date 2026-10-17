n = int(input("Enter n: "))
count = 0

for num in range(2, n + 1):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
        count += 1

print("Total prime numbers:", count)