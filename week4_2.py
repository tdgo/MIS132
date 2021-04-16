# MIS132 - April 16
# Rock, Paper, Scissors Game

import random
accepted_answers = ["rock", "paper", "scissors"]

def generate_random_number():
    random_number = random.randint(1,3)
    #random_choice = random.choice(accepted_answers)
    return random_number

def get_computer_choice(random_number=0):
    if random_number in range(1,4):
        if random_number == 1:
            computer_choice = "rock"
        elif random_number == 2:
            computer_choice = "paper"
        elif random_number == 3:
            computer_choice = "scissors"
        return computer_choice
    else:
        return "The given number is not in range 1-3"

#get_computer_choice(generate_random_number())

def get_user_choice():
    user_choice = ""
    while user_choice not in accepted_answers:
        user_choice = input("Enter your choice (rock, paper or scissors): ").lower()
    return user_choice

#get_user_choice()

def determine_winner(user_choice, computer_choice):
    global game_on
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
        game_on = True
        print("The game continues.")
    else:
        if user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper wraps rock! You lose.")
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper wraps rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
        game_on = False
        print("The game ends.")


game_on = True
while game_on:
    determine_winner(get_user_choice(), get_computer_choice(generate_random_number()))
    if not game_on:
        play_again = input("Do you want to play again (Y or N): ").lower()
        if play_again == "y":
            print("The game continues.")
            game_on = True
        else:
            game_on = False


