f = open("file.txt", "r")

content = f.read()

words = content.split()

print(len(words))

unique = set(words)

print(unique)

f.close()