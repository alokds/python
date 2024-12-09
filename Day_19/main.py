import random
from turtle import Turtle, Screen
screen = Screen()

#  Setting the Screen Size  *****************************/
screen.setup(width=600, height=400)

#  Setting the Finish Line    *************************/
y_turtle = Turtle()
y_turtle.penup()
y_turtle.setpos(230,180)
y_turtle.rt(90)
y_turtle.pendown()
y_turtle.fd(360)
y_turtle.hideturtle()

#  Setting the Turtle Colour , I is used to decide Y axis,         ********************************************/
colors = ["purple", "blue",  "indigo", "green", "yellow", "orange", "red"]
i = -150
turtle_list = []
is_race_on = False

#  Defining 7 Turtle objects   ******************************/
for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-280, y=i)
    new_turtle.color(color)
    turtle_list.append(new_turtle)
    i = i + 50

#  Taking User Input   **************************************/
user_input = screen.textinput(title="bet for the winning turtle",prompt="enter the Colour of winning Turtle")

#  Setting Up the Race status   *****************************/
if user_input:
    is_race_on = True

#  Starting the Race after User Input is provided  ***********************/
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_input == winner:
                print(f"you are correct ! the {winner} has won the race.")
            else:
                print(f"you are wrong ! the {winner} has won the race.")
        turtle.fd(random.randint(0, 20))

screen.exitonclick()