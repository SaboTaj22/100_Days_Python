# import mod_1
# print(mod_1.variable)

# from turtle import Turtle, Screen
# juan = Turtle() # Creates a turtle object/class
# print(juan) # Prints the turtle
# juan.shape("turtle") # Attributes of the turtle
# juan.color("DeepPink")
# juan.forward(100)
#
# my_screen = Screen() # Creates a screen to see the turtle and exits once clicked.
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"
print(table)

