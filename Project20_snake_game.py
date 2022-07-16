from random import gammavariate
from turtle import Turtle,Screen

screen  = Screen()
screen.setup(width = 600,height =600)
screen.bgcolor('black')
screen.title('Snake Game')
snake = [(0,0 ),(-20,0),(-40,0)]
snake_body = []
for i in snake:
    snake = Turtle(shape='square')
    snake.color('white')
    snake.penup()
    snake.goto(i)
    snake_body.append(snake)

game_is_on = True
while game_is_on:
    for body in snake_body:
        body.forward(20)
screen.exitonclick()