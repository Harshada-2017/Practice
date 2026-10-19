
n = int(input())
a = list(map(int, input().split()))

largest = a[0]
second = None

for i in range(n):
    if a[i] > largest:
        second = largest
        largest = a[i]
    elif a[i] < largest:
        if second is None or a[i] > second:
            second = a[i]

if second is None:
    print(-1)
else:
    print(second)