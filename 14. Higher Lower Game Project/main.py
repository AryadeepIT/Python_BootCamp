from art import logo,vs
from game_data import data
import random


def format_data(account):
    """ Takes the account data and returns printable format."""
    account_name=account["name"]
    account_descr=account["description"]
    account_country=account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# make the game repeatable
while game_should_continue:

    # Generate a random account from the game data

    # Making the accounts as position B bacome the account at position A
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}. ")
    print(vs)
    print(f"Compare B: {format_data(account_b)}. ")

    # ask user to guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()



    # check if user is correct
    ## get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    if is_correct:
        # score keeping
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry! that's wrong. Final score : {score}")








# clear the screen btw rounds
