#oops in python
#Procedural Programming in which one procedure leads to another and code run from top to bottom and then jumps to a function 
#Object-oriented programming (OOP) is a fundamental programming paradigm used by nearly every developer at some point in their career. OOP is the most popular programming paradigm and is taught as the standard way to code for most of a programmers educational career.
# A programming paradigm is the classification, style or way of programming. It is an approach to solve problems by using programming languages. Depending on the language, the difficulty of using a paradigm differs.
# Why oops called oops is because it tries to model a real world object
# in oops is it basically based on what it has and what it does
# object is made up of two things attributes and methods 
# attributes tells what an object has it is basically variables associated with the object and 
# methods tells what this object does it is basically a function

# class is the blueprint of the object that has been created and using those blueprints we can create no. of objects
# an object is the actual we gonna use in our codes
# class is written in pascal case i.e . first word should be capital
# object = class() so here object is created with the help of this blueprint named as class
# HOW TO USE OOP 
# Turtle library
# turtle module have screen
# object(timmy) = Turtle()(class)
from turtle import Turtle,Screen

timmy= Turtle()# creating the object
print(timmy)
my_screen = Screen()
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
# Accessing the attributes syntax
# object.attributes
print(my_screen.canvheight)
#accessing the methods syntax
# object.method()
my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Anime Name",["5cm apart","Dororo"])
table.add_column("Character_name",["Akari","Dora"])
print(table)