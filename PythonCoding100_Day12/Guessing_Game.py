from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns = 0
# Compare user guess with actual answer with a function.
def check_answer(guess, answer, turns):
    """Checks answer against guess. Returns number of turns remaining."""
    if guess > answer:
        print("Too high. Guess again!")
        return turns - 1
    elif guess < answer:
        print("Too low. Guess again!")
        return turns - 1
    else:
        print(f"You got it! The answer is {answer}!")

# Make function to set difficulty.
def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # Choose a random number between 1 and 100.
    print(logo)
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    answer = randint(1, 100)
    # print(f"The correct answer is {answer}!")

    turns = difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
    #Let the user guess a number.
        guess = int(input("Make a guess:\n"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("YOU LOSE! GAME OVER")
            return
    # Track the number of turns and reduce by 1 if they get it wrong.
game()