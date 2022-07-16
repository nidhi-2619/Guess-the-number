# Hirst Painting
import colorgram
from turtle import Screen
import turtle,random
# this code is used to extract the color from the image
# colors = colorgram.extract('download.jpg',30)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newcolor = (r,g,b)
#     rgb_color.append(newcolor)
# print(rgb_color)
my_screen = Screen()
turtle.colormode(255)
color_list =[ (153, 77, 50), (203, 149, 109), (22, 27, 55), (236, 225, 91), (133, 161, 205), (63, 88, 136), (139, 66, 88), (49, 30, 24), (26, 38, 30), (127, 33, 47), (63, 29, 37), (43, 50, 110), (143, 175, 159), (190, 89, 122), (189, 141, 158), (137, 32, 25), (76, 108, 83), (207, 86, 66), (101, 111, 186), (69, 75, 41), (165, 183, 228), (102, 149, 96), (231, 176, 166), (221, 171, 186), (49, 83, 33), (155, 205, 217)]    
T = turtle.Turtle()
T.speed('fastest')
T.penup()
T.setheading(225)
T.forward(300)
T.setheading(0)
number_of_dots  = 225
for dot_count in range(1,number_of_dots):
    T.dot(10,random.choice(color_list))
    T.forward(30)
    if dot_count%15 ==0:
        T.setheading(90)
        T.forward(30)
        T.setheading(180)
        T.forward(450)
        T.setheading(0)
        
my_screen.exitonclick()
