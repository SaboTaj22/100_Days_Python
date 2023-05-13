#Defining and Calling Python Functions
# def my_function(): # How to define a function
#     print("Hello") # Do this
#     print("Bye") # Then do this
#     # Finally do this
#
# my_function() # Need to call function, otherwise it won't work

#Drawing a square on a grid with a robot:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()

#Coding Challenge 1
#Move robot over 6 hurdles to finish line
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
# i = 0
# for i in range(1, 7):
#     jump() #Loops through jump 6 times to get through obstacle!

#Loops:
# What I've learned so far
# for item in list_of_items:
#    Do Something to each item

# for number in range(a, b):
#     print(number)

#While Loops:
# while something_is_true:
# Do something repeatedly

#Robot EX using while loop Challenge 2:
# number_of_hurdles = 6
# while number_of_hurdles > 0: # while, condition
#     jump() # Do this
#     number_of_hurdles -= 1 #Takes the number of hurdles down until it = 0
#     # print(number_of_hurdles) #For visualization

#Don't know how far to loop through
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while at_goal() != True: #Loop until the end is false. Could also use "while not at_goal()"
#     jump() #

# Challenge 3 Robot while loop:
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def jump():
#     #Got rid of extra move
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
#
#
# while at_goal() != True: # could also use "while not at_goal():"
#     if wall_in_front():
#         jump() #activate jump function
#     else:
#         move() #keep moving forward

#Challenge 4 Random height of walls to hurdle and placement along grid:
# def
# turn_right():
# turn_left()
# turn_left()
# turn_left()
#
#
# def jump():
#     turn_left()
#     while wall_on_right(): #if there is a wall keep climbing until you reach the top
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear(): #Keep climbing down until you reach the bottom.
#         move()
#     turn_left()
#
#
# while at_goal() != True:
#     if wall_in_front():
#         jump()
#     else:
#         move()

#Final Project: Escaping the Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear(): # prevents the robot from getting stuck in a circle (Infinite loop). Moves it to a wall.
    move()
turn_left()

while not at_goal(): # Moves robot right towards the end of the maze
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()