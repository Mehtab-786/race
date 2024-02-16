import random
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race , enter a colour: ")
screen.setup(width=500, height=400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
turtle_players = []  # storing all turtle players

for turtle_in in range(0, 6):
    """Making turtles"""
    new_turtle = Turtle()
    new_turtle.color(colours[turtle_in])
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.goto(x=-230, y=y_positions[turtle_in])
    turtle_players.append(new_turtle)
print(turtle_players)

if user_bet:
    """This argument prevents unnecessarily running while loop"""
    is_race_on = True

while is_race_on:
    for turtle in turtle_players:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won ! The {winner} turtle is the winner")
            else:
                print(f"you've lost ,{winner} turtle won ")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
