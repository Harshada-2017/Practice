text = input("Enter a string: ")

left = 0
right = len(text) - 1
palindrome = True

while left < right:
    if text[left] != text[right]:
        palindrome = False
        break

    left = left + 1
    right = right - 1

if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")