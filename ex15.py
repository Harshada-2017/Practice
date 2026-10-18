n = int(input("Enter a number: "))
n = abs(n)
digits = {}

if n == 0:
    digits[0] = 1

while n > 0:
    digit = n % 10

    if digit in digits:
        digits[digit] += 1
    else:
        digits[digit] = 1

    n = n // 10

for digit in digits:
    print(digit, "appears", digits[digit], "times")