s = input("Enter a string: ")

found = False

for i in range(len(s)):
    frequency = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            frequency = frequency + 1

    if frequency == 1:
        print("First non-repeating character:", s[i])
        found = True
        break

if found == False:
    print("No non-repeating character")