# MIS132 - April 16
# Random Number Guessing Game

import random
num_range = (1,3)
random_num = random.randint(num_range[0], num_range[1])
guess = ""
game_on = True
count_of_guesses = 0

while game_on:
    while guess != random_num:
        guess = int(input("What is your guess: "))
        count_of_guesses += 1
        if guess > random_num:
            print("Too high, try again")
        elif guess < random_num:
            print("To low, try again")
        else:
            print(f"Congratulations! Yes it is {random_num}")
            print(f"You have made {count_of_guesses} guesses.")
            game_on = False
    play_again = input("Do you want to play again (Y or N):").lower()
    if play_again == "y":
        random_num = random.randint(num_range[0], num_range[1])
        game_on = True
        guess = ""

