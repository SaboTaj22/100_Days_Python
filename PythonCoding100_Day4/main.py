# Generate Random Integers
import random
import my_module #how to call your other file into the main body.

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.pi) #how to call your other file into the main body.

#Float 0.0000000 - 0.9999999...
# random_float = random.random() # Doesn't include 1!
# print(random_float)

# random_float = random.random() * 5
# print(random_float) # How to expand range to 0.00000...4.9999...

# love_score = random.randint(1, 100) #random range of numbers
# print(f"Your love score is {love_score}")

#Coding Exercise 1
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
#
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
#
# e.g. 1 means Heads 0 means Tails

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇
# import random
#
# Heads_Tails = random.randint(0, 1) # First I needed to create an output of either heads or tails
# if Heads_Tails == 0: # I created a conditional statement to represent heads or tails based ont the outcome
#     print("Heads")
# else:
#     print("Tails")

#Lists
# fruits = [item1, item2] # Example lists
# fruits = ["Cherry", "Banana", "Apple"]

# state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# #Order is determined by order in list
#
# print(state_of_america[2]) #Print specific item you want in list
# # Using negative indices will start counting from the back of the list!
# #EX
# print(state_of_america[-1])
#
# #Changing something in a list
# state_of_america[1] = "Transylvania" # Changes a specified item in the list.
# print(state_of_america)
#
# #add an item to the list
# state_of_america.append("Angelaland") #append adds single item to the end of a list
# print(state_of_america)
#
# #adding multiple items to a list
# state_of_america.extend(["Angelaland", "Jack Bauer Land"]) #tons of other useful function

#Coding Exercise 2
# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
#
# Important: You are not allowed to use the choice() function.
#
# Line 8 splits the string names_string into individual names and puts them inside a List called names.
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Import the random module here
import random
# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# sucker = random.choice(names) # Solution using choice function
# print(f"{sucker} is going to buy the meal today!")

#Solution for this problem
# num_items = len(names) # Get total number of items in list
# random_choice = random.randint(0, num_items - 1) # Select randomly from list. This will return an integer
# # Need one less than count since we begin at 0!
# sucker = names[random_choice] # Converts integer to name of person paying
# print(f"{sucker} is going to buy the meal today!") # Prints name of person paying

#Nested List
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes"] #original list

# fruits = ["strawberries", "Nectarines", "Apples", "Grapes"] # Seperate lists
# vegetables = ["Spinach", "Kale"]

# dirty_dozen = [fruits, vegetables] # Combined nested list
# print(dirty_dozen)

#Quiz
# 1
# fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears",]
# print(fruits[-5]) # prints apples!

# 2
# fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
# fruits[-1] = "Melons" # switches last item in list for melons.
# fruits.append("Lemons") # adds Lemons to end of list.
# print(fruits)

# 3
# fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery" "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])
# printing dirty_dozen by itself will give both lists combined
# printing (dirty_dozen[0]) gives first list, and print(dirty_dozen[1] gives second list.
# By printing (dirty_dozen[1][1]) you specify first which list, then second which item in the list.
# Answer is Kale!

#Coding Exercise 3
# You are going to write a program that will mark a spot with an X.
#
# In the starting code, you will find a variable called map.
#
# This map contains a nested list. When map is printed this is what the nested list looks like:
#
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
#
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line.
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
#
# ['⬜️', '⬜️', '⬜️']
# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
#
# The first digit in the input will specify the column (the position on the horizontal axis).
#
# The second digit in the input will specify the row number (the position on the vertical axis).
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "x".
# Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# # input = column, row
# horizontal = int(position[0])
# vertical = int(position[1])
# # row = map[vertical - 1]
# # row[horizontal - 1] = "X"
#
# #Another simpler solution
# map[vertical - 1][horizontal - 1] = "X"
#
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# Final Project: Rock, Paper, Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#My Coding solution
# user_choice = input("Let's play Rock, Paper, Scissors! Enter your move here: \n").lower()
# move = ["rock", "paper", "scissors"]
# computer_choice = random.choice(move)
# print(computer_choice)
#
# if user_choice == "rock" and computer_choice == "paper":
#     print("You Lose")
# elif user_choice == "paper" and computer_choice == "scissors":
#     print("You Lose")
# elif user_choice == "scissors" and computer_choice == "rock":
#     print("You Lose")
# elif user_choice == "rock" and computer_choice == "rock":
#     print("It's a draw!")
# elif user_choice == "paper" and computer_choice == "paper":
#     print("It's a draw!")
# elif user_choice == "scissors" and computer_choice == "scissors":
#     print("It's a draw!")
# else:
#     print("You Win!")

#Given solution
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("Error! You typed an invalid number.")
else:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose!")
    elif computer_choice > user_choice:
        print("You Lose!")
    elif user_choice > computer_choice:
        print("You Win!")
    elif computer_choice == user_choice:
        print("It's a draw!")

