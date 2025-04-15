import random
secret_number = random.randint(1, 100)
print(secret_number)

guess = int(input("Guess a number (1-100): "))

if guess < secret_number:
    print("Too Low")

elif guess < secret_number:
    print("Too High")
else:
    print("Correct")

attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number: 
        print("Too High")
    else:
        print("Correct! Attempts: ", attempts)
        break
