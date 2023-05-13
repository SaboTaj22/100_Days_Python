# #Problem 1, Subscripting
# print("Hello"[0]) #Pulling out specific letters using [] and a place indicator

#P2 Pull out o form Hello?
# print("Hello"[4])

#P3 Integers (Whole numbers)
# print(123 + 345) #Adding integers
# 123_456_789 #writing big numbers that need commas

#P4 Float
# 3.1459 #Decimal in number. point can float around number

#P5 Boolean
# True
# False

#P6 Not sure what data type it is?
# num_char = len(input("What is your name?"))
# print(type(num_char)) #Prints what data type it is

#P7 Converting to new data type
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.") #Prints what data type it is

#Challenge 1
# Write a program that adds the digits in a 2 digit number. e.g.
# if the input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))
# Had to figure out how to get the 1st and second position of a 2 digit number
# Needed to add them together
# Found out the data type was a str using type(), I needed to convert both to int

#Challenge 2
# 🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# y = float(height) # I converted both string values to floats in case there were disproportionate measurements entered
# x = float(weight)
# print(int(x/y**2))
#I entered the formula for BMI. We needed it to be a whole rounded number so I used int.
#Using // instead could work as well, but you would still need int because it would print a float.

#P8
# print(round(8/3, 2)) #round will round it to the nearest whole number.
# By putting , then a number after division, this enables you to set the rounding to a specific decimal place.

#P9 User score points
#score += 1 #same as (score = score + 1)

#P10 f-string: Combines multiple different data types into a string
# score = 0
# height = 1.8
# isWinning = True
#f-string
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#Challenge 3
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# 🚨 Don't change the code below 👇
#age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# days = 90*365-(int(age)*365)
# weeks = 90*52-(int(age)*52)
# months = 90*12-(int(age)*12)
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# My improved version of Challenge 3 to make it more accurate at age 90
# 🚨 Don't change the code below 👇
# age = float(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# days_remaining = 90*365-(float(age)*365)
# weeks_remaining = 90*52-(float(age)*52)
# months_remaining = 90*12-(float(age)*12)
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#P11
# a = int("5") / int(2.7)
# print(type(a)) # int("5") is 5, int(2.7) is 2, so the code becomes: a = 5 ÷ 2 which equals 2.5, which is a float.

# age = 12
# print(f"You are {age} years old")

# name = input("What is your name?")
# print(f"Hello, {name}")

# name = input("What is your name?")
# print(f"Hello, " + name)

# Final Challenge, Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!") # Welcome note
bill_amount = float(input("What is your bill?\n $")) #Bill amount input on following line. Float enables any number
percentage_tip = float(input("What percentage tip would you like to give? 10%, 12%, or 15%?\n")) #percent tip input
number_people = int(input("How many people to split the bill?\n")) #Used int because not calculating parts of people
total_amount = bill_amount * (percentage_tip / 100 + 1) #Calculation for total amount short hand way
payment_distribution = round(total_amount/number_people, 2) #round answer to the 2 decimals
payment_distribution = "{:.2f}".format(payment_distribution) #formatted so we get .0 at end for full 2 decimals
print(f"Each person should pay: ${payment_distribution}") #Give amount each person should pay
