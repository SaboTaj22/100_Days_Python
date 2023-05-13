#For Loops
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits: #For, name for a single item, in , list name, :
    # print(fruit) # one time in a list
    # print(fruit + " Pie") #prints "fruit" + pie
    #print(fruits) #prints as many times as the loop runs
#print(fruits) #prints once

#Exercise 1
# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
# e.g.
#
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
# There are a total of 7 heights in student_heights
#
# 1146 ÷ 7 = 163.71428571428572
#
# Average height rounded to the nearest whole number = 164
#
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.
    # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
    # 🚨 Don't change the code above 👆

    # Write your code below this row 👇

#Easy way:
# average = sum(student_heights)/len(student_heights)
# print(round(average))

#Way that it was asked:
# sum
# total_height = 0
# for height in student_heights:
#     total_height += height #total_height = total_height + height (Adds inputs as many times as there are inputs)
# #print(total_height)
#
# # len
# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1 #For as many time as there are inputs, add that amount of times
# #print(number_of_students)
#
# average_height = total_height/number_of_students
# print(round(average_height))

# I wrote this code again to try to make sense of it. The biggest thing to remember is that whatever you put
# after "for" represents an item in the list
# sum_list = 0
# for i in student_heights:
#     sum_list += i #Here we're adding the items together!
# #print(sum_list)
#
# length_list = 0
# for i in student_heights:
#     length_list += 1 #Here we're adding the number of items in the list together!
# #print(length_list)
#
# average = print(f"The student height average is: {round(sum_list/length_list)}\n")

#Exercise 2
# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#Easy Way
# print(f"The highest score in the class is: {max(student_scores)}\n")

#Asked way to do it
# highest_score = 0
# for score in student_scores:
#   if score > highest_score: # is current score greater than highest score?
#     highest_score = score # runs through list until highest value = highest score!
# print(f"The highest score in the class is: {highest_score}\n")

#Range function:
# Format
# for number in range(a, b): # Creates a range from a to b and poops out a number for you to manipulate
# When printed, it doesn't include b! EX a range from 1-10 would be written (1, 11)
#   print(number)
# adding c to the range: (a, b, c) c specifies how large you want a step to be.
# total = 0 # Accumulator
# for number in range(1, 101):
#     total += number # adds every number in this range!
# print(total)

#Exercise 3:
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100.
# Thus, the first even number would be 2 and the last one is 100:
#
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
#
# Important, there should only be 1 print statement in your console output.
# It should just print the final total and not every step of the calculation.

#Write your code below this row 👇
# sum = 0
# for i in range(2, 101, 2): # Putting 1 at beginning makes step 1 + 2 = 3. So switch to 2 to get +2 so all number even!
#     sum += i
# print(sum)

# Another way to solve:
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print(total)

#Coding Interview Question Exercise:
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
#
# Your program should print each number from 1 to 100 in turn.
#
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

#Write your code below this row 👇
# i = 0 # i refers to number in this code
# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 5 == 0:
#         print("Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     else:
#         print(i)

#Coding Challenge:
#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
#
# for character in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for character in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for character in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

for character in range(1, nr_letters + 1):
    password_list.append(random.choice(letters)) # append does the same thing that += is doing!
for character in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for character in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# print(password_list) # Version before shuffle
random.shuffle(password_list)
# print(password_list) # Version after shuffle

password = ""
for character in password_list:
    password += character
print(f"Your password is: {password}")

