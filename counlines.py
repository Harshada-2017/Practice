def solve():
    f = open("data.txt", "r")
    lines = f.readlines()

    print("Total lines:", len(lines))

    f.close()

solve()