# Hangman Project
# import random
# #Step 1
#
# word_list = ["aardvark", "baboon", "camel"]
#
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#
# chosen_word = random.choice(word_list) #Need to choose a random word from a list
# #print(chosen_word) #Testing Code
# guess = input("Guess a letter: ").lower() # Input for user guess of what letter is in the word.
#
# for letter in chosen_word: # Need to interate through word in list to check if letter is actually in it
#     if guess == letter: # if the letter "a variable in chosen_word" is in the word, print "right"
#         print("Right")
#     elif guess != letter: # if the letter isn't in it, print "wrong".
#         print("Wrong")

#Phase 2:
#Step 2

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display = [] # Create a list
# for _ in range(len(chosen_word)):
#     display += "_" # displays "_" per letter
# guess = input("Guess a letter: ").lower()
#
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#
# for position in range(len(chosen_word)): # for as many times as there are letters in the word,
#     # get hold of position where letter == guess.
#     letter = chosen_word[position] # get hold of current letter
#     if letter == guess:
#         display[position] = letter
#
# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)

#Phase 3
#Step 3

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# end_game = False
# while not end_game: # until everything in our for loop = false, keep iterating
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     print(display)
#
#     if "_" not in display: #Once all the "_" are full, you win!
#         end_game = True
#         print("You Win!")

#Phase 4
#Step 4

# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
#
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #Set 'lives' to equal 6.
# lives = 6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1.
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True #Need to refer to end_of_game, otherwise the code won't stop for "You Lose"
#             print("You Lose")
#
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives]) #all stages are in order. simple print stages corresponding to lives

#Final Step
#Step 5
import random
from word_list import word_list
from logo import logo
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list) #Can also write word_list.word_list
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}!")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed '{guess}', that's not in the word. You lose a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win!")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from Stages import stages
    print(stages[lives])