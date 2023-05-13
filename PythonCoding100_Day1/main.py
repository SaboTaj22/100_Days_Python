#Problem 1
#print("Hello world!") #print puts stuff in terminal, strings tell computer that stuff in parenthesis are not commands
# Pay attention to syntax color!

#Problem 2
#print("Hello world!\nHello world!\nHello world!") #Can't have space in between or it will bug

#Problem 3
#print("Hello"+" "+"Angela") #Adding space in between words. (you can also put a space after hello or before angela

#Problem 4
#print("Hello " + input("What is your name?")) #input requires you to enter something like a name before code continues

#Problem 5
# Write a program that prints the number of characters in a user's name.
# You might need to Google for a function that calculates the length of a string.
#print(len(input("What is your name?")))

#Problem 6
#name = input("What is your name?") #Defining a variable
#print(name)

#Problem 7
#name = input("What is your name") #more written out version of line 12
#length = len(name)
#print(length)

#Problem 8
# Write a program that switches the values stored in the variables a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a, b = b, a



#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Final Project
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")

#2. Ask the user for the city that they grew up in.
City = input("What's the name of the city you grew up in?\n")

#3. Ask the user for the name of a pet.
Pet = input("What's your pet's name?\n")

#4. Combine the name of their city and pet and show them their band name.
Name_of_Band = City + " " + Pet
print("Your band name could be "+ Name_of_Band)

#5. Make sure the input cursor shows on a new line:



