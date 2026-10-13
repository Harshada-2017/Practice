def isArmstrong(n):
    original = n
    temp = n
    count = 0
    total = 0

    if n == 0:
        count = 1

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n

    while temp > 0:
        digit = temp % 10
        total = total + digit ** count
        temp = temp // 10

    return total == original

print(isArmstrong(153))