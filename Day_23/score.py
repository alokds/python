from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 15, 'normal')
turtle = Turtle()


class Score:
    def __init__(self):
        self.new_score = 0

    def score(self):
        turtle.clear()
        turtle.hideturtle()
        turtle.color("yellow")
        turtle.penup()
        turtle.goto(-250, 260)
        turtle.write(f"LEVEL : {self.new_score}", align=ALIGN, font=FONT)
