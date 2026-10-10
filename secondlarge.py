def second_largest(a):
    largest = a[0]
    second = None

    for i in a:
        if i > largest:
            second = largest
            largest = i
        elif i < largest:
            if second == None or i > second:
                second = i

    return second

print(second_largest([10, 40, 20, 40, 30]))