secret = 7
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        print("Attempts:", attempts)