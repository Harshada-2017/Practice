n = int(input())
a = list(map(int, input().split()))

visited = []

for i in range(n):
    if a[i] not in visited:
        count = 0

        for j in range(n):
            if a[i] == a[j]:
                count += 1

        print(a[i], count)
        visited.append(a[i])