numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]
second = None

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num != largest:
        if second is None or num > second:
            second = num

if second is None:
    print("No second-largest number")
else:
    print("Second largest:", second)