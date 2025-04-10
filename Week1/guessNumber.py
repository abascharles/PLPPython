import random
secret_number = random.randint(1, 100)

guess = int(input("Guess a number (1-100): "))

if guess < secret_number:
    print("Too Low")

elif guess < secret_number:
    print("Too High")
else:
    print("Correct")