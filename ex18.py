a = input("Enter first word: ").lower()
b = input("Enter second word: ").lower()

if sorted(a) == sorted(b):
    print("Anagrams")
else:
    print("Not anagrams")