def anagram(a, b):
    if sorted(a) == sorted(b):
        return "Anagram"
    else:
        return "Not Anagram"

print(anagram("listen", "silent"))