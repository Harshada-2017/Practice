arr = list(map(int, input("Enter elements: ").split()))

sorted_array = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("Array is sorted")
else:
    print("Array is not sorted")