def sumDigits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total

print(sumDigits(1234))