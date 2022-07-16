# event listener
# onkeys(key,function)
# key we define from keyboard
# function
# Higher order function that is a function that can work with another function
from turtle import Turtle,Screen

tim = Turtle()
screen  = Screen()

def move_forward():
    return tim.forward(100)
def move_backward():
    return tim.backward(100)
def turn_left():
    return tim.left(45)
def turn_right():
    return tim.right(45)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"l")
screen.onkey(turn_right,"r")
screen.onkey(clear,"c")
screen.exitonclick()

# instance and states
# state is when , one two objects have same attributes and methods but perform different functions
# instance is the part of objects when different objects are created and they are independent of each other 