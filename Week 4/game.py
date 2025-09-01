

import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        print("Error")

num = random.randint(1, level)
while True:
    guess_input = input("Guess: ")
    try:
        guess = int(guess_input)
        if guess > 0:
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")
                break
        else:
            print("Error")
    except ValueError:
        continue
