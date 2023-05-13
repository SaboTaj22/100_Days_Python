#Control Flow with if/else and Conditional Operators

#Problem 1
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
#
# if height >= 120: #If you want to include 120 use = sign
# #just an = alone is assigning a value to a variable.
# # if == it's checking to see if left and right are equal
#   print("You can ride the roller coaster!")
# else: #If condition is not met, move to this.
#   print("Sorry, you can't ride the roller coaster.")

#Challenge 1 Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# if number % 2 == 0: #To check if something evenly divided ==0
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

#Problem 2
#Nested if/else statement
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

#if/elif/else
# if condition1:
#     do A
# elif condition2: #elif used to go through numerous conditions
#     do B
# else:
#     do this

# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm?"))
# if height >= 120:
#     print("You can ride this roller coaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     elif age < 22:
#         print("Please pay $10.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you can't ride the roller coaster.")

#Coding Challenge 2
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
#
# 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆
#
# #Write your code below this line 👇
# BMI = round(weight / height**2)
# if BMI <= 18.5:
#     print("you are underweight.")
# elif BMI <= 25:
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI <= 30:
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI <= 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")

#Leap Year Challenge 3
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap years have 366, with an extra day in February.

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

# year = int(input("What year do you want to check?\n"))
#
# if year % 4 == 0:  # Then it is a leap year, if false, it is not
#     if year % 100 == 0:     # Then it isn't a leap year, if false, it is
#         if year % 400 == 0:  # Then it is a leap year, if false, it is not
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# if/elif/else # only 1 can be true
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# Multiple if # all conditions could be true
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

# Multiple if statements
# print("Welcome to the roller coaster!")
# height = int(input("What is your height in cm?\n"))
# bill = 0 #Need a variable for bill to be referenced in wants_photo
#
# if height >= 120:
#     print("You can ride this roller coaster!")
#     age = int(input("What is your age?\n"))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#         #Using and to implement another conditional comparison
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N.\n")
#     if wants_photo == "Y":
#         bill += 3
#     print(f"Your final bill is {bill}")
#
# else:
#     print("Sorry, you can't ride the roller coaster.")

#Coding Challenge 4
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
#
# Based on a user's order, work out their final bill.
#
# Small Pizza: $15
#
# Medium Pizza: $20
#
# Large Pizza: $25
#
# Pepperoni for Small Pizza: +$2
#
# Pepperoni for Medium or Large Pizza: +$3
#
# Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆
#
# # Write your code below this line 👇
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")

#Logical Operators
# A and B = Either both True to be True, or if 1 of them is false overall false.
# C or D = If one or other is True, it evaluates to True. ONLY when C and D are both false does it evaluate to False
# not = Reverses the output. I.E. True to False and False to True.

#Coding Challenge 5
# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.

# 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# combined_names = name1 + name2 #first step is to add the names together then convert to lower so we can count input
# lower_case_names = combined_names.lower()
# t = lower_case_names.count("t") # once added we count the inputs of each letter.
# r = lower_case_names.count("r")
# u = lower_case_names.count("u")
# e = lower_case_names.count("e")
#
# true = t + r + u + e # add up the amount of times each letter appears in true and then love
#
# l = lower_case_names.count("l")
# o = lower_case_names.count("o")
# v = lower_case_names.count("v")
# e = lower_case_names.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love)) # needed to add strings together then convert to int to throw into if/else
# print(love_score)
#
# if love_score < 10 or love_score > 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your score is {love_score}.")

# Final Project
#Create treasure island game that has 3 levels with varying outcomes. Each choice will determine whether the player
#progressed or gets a "Game Over". If the player chooses correctly, they will find the treasure!
#Level 1: Left or right?
#Level 2: Wait or swim?
#Level 3: Blue, Red, or Yellow Door?

print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
print("\n")
left_right = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower() #use backslash to bypass extra '.
# I used .lower() to convert any case entry to lower case for manipulation in the program.
if left_right == "left":
    wait_swim = input('You\'ve come to a lake. There is an island in the middle of the lake.\nType "wait" to wait for boat. Type "swim" to swim across.\n').lower()
    if wait_swim == "wait":
        color = input('You arrive at the island unharmed. There is a house with 3 doors.\nOne "red", one "yellow", and one "blue". Which color do you choose?\n').lower()
        if color == "yellow":
            print("You found the treasure! You Win!")
        elif color == "red":
            print("Burned by fire! Game Over")
        elif color == "blue":
            print("Eaten by lions. Game Over")
        else:
            print("Game Over")
    else:
        print("Eaten by lake monster. Game Over")
else:
    print("Eaten by cannibals. Game Over")