# from art import logo, vs
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """ Check the user if correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate a random account from data

    # Making account in position B become account in position A
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    # print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask the user to guess
    guess = input("Who has more followers A or B ? ").lower()

    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give feedback to user:
    # Score keeping
    if is_correct:
        score += 1
        print(f"you're right.Current score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry, you're wrong. Final score is {score}")
