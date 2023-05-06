from art import logo, vs
from game_data import data
import random

# print(logo)


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


# Generate a random account from data
account_a = random.choice(data)
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
if is_correct:
    print("you're right..")
else:
    print("Sorry, you're wrong")
