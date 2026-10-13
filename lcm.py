def lcm(a, b):
    i = 1

    while True:
        if i % a == 0 and i % b == 0:
            return i

        i = i + 1

print(lcm(4, 6))