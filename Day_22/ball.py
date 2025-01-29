from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.new_x = 0
        self.new_y = 0
        self.movex = 10
        self.movey = 10
        self.set_sleep = 0.07

    def ball_point(self):
        self.new_x = self.xcor() + self.movex
        self.new_y = self.ycor() + self.movey
        self.goto(self.new_x, self.new_y)

    def bouncey(self):
        self.movey *= -1

    def bouncex(self):
        self.movex *= -1

    def bounce_back(self):
        self.goto(0, 0)
        self.bouncex()
