def move_zeros(numbers):
    result = []
    count = 0

    for i in numbers:
        if i == 0:
            count = count + 1
        else:
            result.append(i)

    while count > 0:
        result.append(0)
        count = count - 1

    return result

print(move_zeros([0, 1, 0, 3, 12]))