# MIS 132 - March 26

# Fundamentals (Values Variables)
# Functions
# Conditionals

num1 = 2
num2 = 10
name = "MIS 132"
# print(f" Welcome to the {name} course!")

# String, integer, float, boolean (True, False)


def lesser_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    elif a%2 == 0:
        return "First number is even, but second is not."
    elif b%2 == 0:
        return "Second number is even, but first is not."
    else:
        return "Both of them are odd."

# print(lesser_two_evens(2,1))


def greet():
    name = input("What is your name, please enter: ")
    print (f" Hello {name}")


def how_are_you():
    users_feeling = int(input("How are you feeling today [1-5]: "))

    if 6 > users_feeling >= 4:
        print("Happy to hear!")
    elif 4 > users_feeling > 1:
        print("Hope you get better.")
    elif users_feeling < 2:
        print("Sorry to hear that")
    else:
        print("You are great.")














