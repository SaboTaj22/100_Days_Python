#Functions with Inputs & Arguments and Parameters
# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

#Simple Function
# def greet():
#     print("Hello")
#     print("Hi")
#     print("How are you?")
#
# greet()

#Function that allows for input
# def greet_with_name(name): # name = parameter is the name of data that is used inside the function. (Name of data)
#     print(f"Hello {name}")
#     print(f"Hi {name}")
#     print(f"How are you {name}?")
#
# greet_with_name("Billie") #Argument is the actual piece of data that is going to be passed over. (Actual value)

#Functions with more than 1 input
# def greet_with(name, location):
#     print(f"My name is {name}")
#     print(f"I am from {location}")

# greet_with("Bill", "San Francisco") #Order of arguments matters to fit function! (Positional argument)

#if you assign each parameter and argument a variable name, then they will line up!
#def my_function(a, b ,c):
    #Do this
    #and this
    #and this

# my_function(a = 1, b = 2, c = 3)

#Using key word arguments
# def greet_with(name, location):
#     print(f"My name is {name}")
#     print(f"I am from {location}")
#
# greet_with(name="Bill", location="San Francisco") #Now regardless of order it'll still give the name and location correctly!

#Coding Challenge 1
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#
# number of cans = (wall height x wall width) ÷ coverage per can.
#
# e.g. Height = 2, Width = 4, Coverage = 5
#
# number of cans = (2 * 4) / 5
#
#                            = 1.6
#
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
#
# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
# import math
# #Write your code below this line 👇
# def paint_calc(height, width, cover):
#     calculation = math.ceil(height*width/cover)
#     print(f"You'll need {calculation} cans of paint.")
#
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)

#Prime Number Checker Challenge
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.

# Write your code below this line 👇
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number): # All numbers are divisible by 1 so we have to use 2
#         if number % i == 0: # Not a prime number because primes can only be divided by self and 1
#             is_prime = False
#     if is_prime: # Same as if is_prime == True
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")
#
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)

#Caesar Cipher Encryption Part-1
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter) #find the index of the letter that we're looping through in the alphabet
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")
#
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(plain_text = text, shift_amount = shift)

#Caesar Cipher Decryption Part-2
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount # shift position
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
# # Then call the correct function based on that 'direction' variable.
# # You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(cipher_text=text, shift_amount=shift)

#Caesar Cipher Part 3 - Reorganizing code
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# def caesar(start_text, shift_amount, cipher_direction):
#   end_text = ""
#   if cipher_direction == "decode": #could also use if cipher_direction == "encode": #new_position = position + shift_amount
#     shift_amount *= -1 # if decode moves backwards #Pulled if out of for loop to prevent a mismatch in decoding
#   for letter in start_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount # if encode move forwards
#     end_text += alphabet[new_position]
#   print(f"The {cipher_direction}d text is {end_text}") #put a d so it says encode-d and decode-d
#
# #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

#Caesar Cipher Part 4 - User Experience Improvements and Final touches

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char # only encodes letters everything else is left alone.
    # TODO-3: What happens if the user enters a number/symbol/space?
    # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    # e.g. start_text = "meet me at 3"
    # end_text = "•••• •• •• 3"
    # position = alphabet.index(char)
    # new_position = position + shift_amount
    # end_text += alphabet[new_position]

  print(f"Here's the {cipher_direction}d result: {end_text}")


# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
# if direction != 'encode' or 'decode':
#   print("Your entry is invalid!")
  # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  # Try running the program and entering a shift number of 45.
  # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
  # Hint: Think about how you can use the modulus (%).
  shift = shift % 26 #Shifts number down to fit into alphabet!
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == 'no':
    should_continue = False
    print("Goodbye!")