#Functions with Outputs

# def format_name(first_name, last_name):
#     print(first_name.title()) # title converts the first letter in an input into a capital letter
#     print(last_name.title())
#
# format_name("angela", "bauer") # calling function with names for inputs

#Can also store the inputs within a variable
# def format_name(first_name, last_name):
#     formated_f_name = first_name.title()
#     formated_l_name = last_name.title()
#     # print(f"{formated_f_name} {formated_l_name}") # could also return it instead by replacing "print" with "return"
#     return(f"{formated_f_name} {formated_l_name}")
# print(format_name("AnGeLA", "yU"))

#Save some time if input wasn't valid
# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return "You didn't provide valid inputs!"
#     formated_f_name = first_name.title()
#     formated_l_name = last_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# print(format_name(input("What is your first name?"), input("What is your last name?")))

#Exercise 1
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     if month > 12 or month < 1: # if the month we are that the user entered is incorrect, raise error.
#         return"Invalid month!"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2: # if month is february and it meets all the criteria for a leap year
#         return 29 # Since it is a leap year
#     return month_days[month - 1] # if it's not a leap year, return the amount of days in the month
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

#Docstrings
# def isleap():
# """Finds out if a year is a leap year or not.""" # Use 3 brackets. It creates a definition bar for what the function does.

from art import logo
#Calculator

# Add
def add(n1, n2):
    return n1 + n2
# Subtract
def subtract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary where the keys are the symbols and the values are the names of the functions.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)

    num1 = float(input("What's the first number?:\n"))
    for symbol in operations:  # Loop through operations for symbols
        print(symbol)
    continues_if = True

    while continues_if:  # continues to run through operations
        num2 = float(input("What's the next number?:\n"))
        operation_symbol = input("Pick an operation:\n")
        calculation_function = operations[operation_symbol]  # passes in operation symbol given by user,
        # loops through to get the correct function.
        answer = calculation_function(num1, num2)  # passes in inputs to function to perform calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")  # prints the calculation and answer
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation:\n") == "y":
            num1 = answer
        else:
            continues_if = False  # Ends calculation
            #clear() # Clear function would enable you to start fresh, unfortunately I can't implement the replit for this project.
            calculator() # Calling calculator function within calculator function. (Recursion)
calculator()
# Print VS Return
# Print statements to display the final output of a code on the console,
# whereas the return statement returns a final value of a function execution which may be used further in the code.

#Adding a second calculation
# Here we select "*" which overides the "+" we selected on line 26.
# operation_symbol = input("Pick another operation:\n")
# num3 = int(input("What's the next number?:\n"))
#
# # Here the calculation_function selected will be the multiply() function
# calculation_function = operations[operation_symbol]
#
# # Here the code will be:
# # second_answer = multiply(multiply(num1, num2), num3)
# # second_answer = calculation_function(calculation_function(num1, num2), num3)
# # second_answer = 2 * 3 * 3 = 18
# # To fix this bug we need to change the code on line 42 to:
# second_answer = calculation_function(first_answer, num3)
# # In the next lesson, we will delete all the code from line 34-48 so don't worry
# # It won't affect your final project.
# # But it's a good opportunity to practice debugging. 🐞
#
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

