from turtle import Turtle,Screen
import turtle
import random
Timmy = Turtle()  # now the timmy is converted into an object
turtle.colormode(255)
Timmy.speed('fastest')
def pen_color():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    random_color = (r,g,b)
    return random_color
# syntax is 
# from module name import module thing 
# to import everything from the module
# from module name import *
# aliasing the module
# import module name as nickname
# def draw_shape(num_of_sides):
#     angle = 360/num_of_sides
#     for _ in range(num_of_sides):
#         Timmy.forward(100)
#         Timmy.right(angle)
# for sides in range(3,11):
#     Timmy.color(pen_color())
#     draw_shape(sides)
# # for _ in range(50):
# #     Timmy.forward(10)
# #     Timmy.penup()
# #     Timmy.forward(10)
# #     Timmy.pendown()
# # for _ in range(200):
# #     Timmy.forward(2)
#     # Timmy.setheading(choice(directions))
#     # Timmy.setheading(30)
#     # Timmy.setheading(90)

# my_screen = Screen()
# my_screen.exitonclick()
# # Tuples
# # A tuple is a data type in python it has round brackets around it separated by ,
# # we cannot change the value in tuple like list

Timmy.color(pen_color())  
def spirograph(gaps):
    for _ in range(360//gaps):
      Timmy.color(pen_color())
      Timmy.circle(100)
      Timmy.setheading(Timmy.heading()+gaps)
spirograph(5)      
      