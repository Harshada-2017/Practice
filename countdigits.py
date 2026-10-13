def countDigits(n):
    count = 0

    if n == 0:
        return 1

    while n > 0:
        count = count + 1
        n = n // 10

    return count

print(countDigits(58321))