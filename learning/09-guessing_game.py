import random

ran_num = random.randint(1, 100)

print("Guess the number between 1 and 100! ")

guess = int(input("Please enter your guess: "))
attempts = 1

if guess < 1 or guess > 100:
    print("Your guess must be between 1 and 100.")
    guess = int(input("Please enter your guess: "))

while ran_num != guess:
    if guess < ran_num:
        print("Too low, try again!")
    elif guess > ran_num:
        print("Too high, try again!")
    guess = int(input("Guess again!: "))
    attempts += 1
print(f"Congratulations! You guessed the number {ran_num} in {attempts} attempts!")



