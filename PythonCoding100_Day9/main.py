#Dictionaries and Nesting

# {key: value} # format of a dictionary

# To add more values into dictionary
# EX:
# {"Bug": "An error in programing", "Function": "A piece of code that can be called over again",
 # "Loop": "The action of doing something repetitively "}

#Format of dictionary:
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
# }
# Retrieving value from a dictionary
#print(programming_dictionary["Bug"])

# Add new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
#print(programming_dictionary)

# Create an empty dictionary
#empty_dictionary = {}

# Wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#     print(key) # prints the key
#     print(programming_dictionary[key]) # retrieves and prints values associated with key

# Exercise 1 Grading Program
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores: # for each student in the dictionary
#     score = student_scores[student] # get hold of value by tapping into dictionary by giving it the key
#     if score == 100 or score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score == 90 or score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score == 80 or score >= 71:
#         student_grades[student] = "Acceptable"
#     elif score <= 70:
#         student_grades[student] = "Fail"
#
# # 🚨 Don't change the code below 👇
# print(student_grades)

#Nesting Lists and Dictionaries

# {
#     key: [List]
#     key2: {Dict} # nesting list and dictionaries in dictionary
# }

# Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# Nesting a list in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"], # can also nest list in list, but this is a lot easier to work with!
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

# Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"places_pooped": ["Berlin", "Hamburg", "Stuttgart"], "total_poop": 48},
# }

# Nesting Dictionary in a List:
# [{
#     key: [List],
#     key2:{Dict},
# },
#     {
#         key: Value,
#         key2: Value,
#     }]

# travel_log = [ # switching from {} to [] puts the dictionary in a list that you can iterate through!
#     {"country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# ]

# Seperating for readability:
# travel_log = [
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12
#      },
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visits": 5
#      },
# ]

#Exercise 2
# You are going to write a program that adds to a travel_log.
# You can see a travel_log which is a List that contains 2 Dictionaries.
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# You've visited Russia 2 times.
# You've been to Moscow and Saint Petersburg.
# DO NOT modify the travel_log directly. You need to create a function that modifies it.

# travel_log = [ # First thing to notice is that this is a dictionary inside a list!
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries to be added to the travel_log. 👇

# def add_new_country(country_visited, times_visited, cities_visited): #create a function using the same name below with all inputs needed.
#     new_country = {} #in order to add to list of dictionaries, create a new dictionary.
#     new_country["country"] = country_visited # add each piece of data to the dictionary
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country) #use append to add the new dictionary to travel_log list



#🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

#Final Coding Project: Secret Auction Program
#from replit import clear
from art import logo
# HINT: You can call clear() to clear the output in the console.
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    # bidding_record = {"Angela": 123, "James": 321}
    highest_bid = 0 #number used to check against current bid
    winner = ""
    for bidder in bidding_record: #loops through keys
        bid_amount = bidding_record[bidder] #use key to get the value
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?\n").lower()
    bid_price = float(input("What is your bid price?\n$"))
    bids[name] = bid_price
    more_bid = input('Are there any other bidders? If yes, enter "yes", if no, enter "no".\n').lower()
    if more_bid == "no":
        bidding_finished = True
        find_highest_bidder(bids) # pass in all bids you've kept track of
    elif more_bid == "yes":
        clear() #function to clear the screen for next user inputs. I didn't implement because I don't have acces to the replit



