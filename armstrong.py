def armstrong(n):
    original = n
    temp = n
    count = 0
    total = 0

    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n

    while temp > 0:
        digit = temp % 10
        total = total + digit ** count
        temp = temp // 10

    if total == original:
        return "Armstrong"
    else:
        return "Not Armstrong"

print(armstrong(153))