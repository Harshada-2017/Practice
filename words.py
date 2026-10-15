def solve():
    f = open("data.txt", "r")
    data = f.read()
    words = data.split()
    return len(words)