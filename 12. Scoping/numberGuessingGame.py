#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5 

#function to check user's guess against actual ans
def check_answer(guess, answer, turns):
    """checks answer agains guess and update turns """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

#Make a function to set difficulties
def set_difficulty():
    level = input("Choose difficulty - Type 'easy' or 'hard' :")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    # choosing random number btw 1-100
    print('Welcome to the Guessing game')
    print("I'm thinking of a number btw 1 - 100 : ")
    answer = randint(1,100)
    # print(f"The answer is {answer}")

    turns=set_difficulty()

    guess = 0
    #Repeat the guessing
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #let the user guess a number
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess Again!")



game()










