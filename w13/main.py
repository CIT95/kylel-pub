# Note: this program works about 99% of the time
# there is one small issue where the turtle in last place
# decides to make a 180 turn, instead of turning right.
# But in reality, it doesn't matter for the race, since it's
# so far behind.
# Guess it just gives up haha.

# Turns out having the turtles follow a
# maze is actually kind of difficult.
# There's a lot of room for improvement with
# my code, if you have suggestions to make it better
# or more concise,
# feel free to adjust it.
from turtle import Turtle, Screen, bgpic
import random

bgpic('kylel-pub\\w13\\maze.png')
is_race_on = False
screen = Screen()
user_bet = screen.textinput(title="Make Your Bet",
                            prompt="Which Turtle will win the race?"
                                   "Enter a color:")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-80.00, y=210.00)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        x = turtle.xcor()
        y = turtle.ycor()
        if x > 30 and y == 210:
            turtle.setposition(30, 210)
            turtle.right(90)
        elif x == 30.0 and y <= -110:
            turtle.setposition(30, -110)
            turtle.right(90)
        elif x <= -40.0 and y == -110.0:
            turtle.setposition(-40, -110)
            turtle.left(90)
        elif x == -40.0 and y < -250.0:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
screen.exitonclick()
