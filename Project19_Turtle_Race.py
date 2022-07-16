from turtle import Turtle,Screen
import random
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make the bet",prompt="Which turtle will win the race")
if user_choice :
    is_race_on = True
colors = ['red','blue','green','yellow','violet','orange']
y_positions = [-100,-60,-20,20,60,100]
all_turtles = []
for i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtles.append(new_turtle)
while is_race_on :
    
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice :
                print(f"You've Won !The {winning_color} turtle is the winner")
            else:
                print("You've Lost")    
        rand_speed=random.randint(0,10)
        turtle.forward(rand_speed)
screen.exitonclick()