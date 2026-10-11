s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()

if len(s1) != len(s2):
    print("Not Anagrams")
else:
    visited = []
    anagram = True

    for i in range(len(s1)):
        if s1[i] not in visited:
            count1 = 0
            count2 = 0

            for j in range(len(s1)):
                if s1[i] == s1[j]:
                    count1 = count1 + 1

                if s1[i] == s2[j]:
                    count2 = count2 + 1

            if count1 != count2:
                anagram = False
                break

            visited.append(s1[i])

    if anagram:
        print("Anagrams")
    else:
        print("Not Anagrams")