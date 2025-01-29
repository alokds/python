from turtle import Screen, Turtle
from score import Score
screen = Screen()
t = Turtle()
score = Score()


#   ******************** ROAD CROSS SCREEN  ***************************
def main_screen():
    screen.tracer(2)
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.title("Turtle_Crossing")
    score.score()


#  *****************************  VEHICLE ROAD ****************************
def path():
    t.hideturtle()
    t.color("green")
    t.shape("classic")
    t.penup()
    t.goto(-280, -250)
    for width in range(0, 12):
        for step in range(-1, 27):
            t.pendown()
            t.fd(10)
            t.penup()
            t.fd(10)
            step += 1
        new_y = t.ycor() + 50
        t.goto(-280, new_y)
        width += 1
