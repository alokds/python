from turtle import Turtle, Screen
screen = Screen()
UP = 20
DOWN = 20


# ************** PADDLE CLASS with its ATTRIBUTES  ********************************
class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color(color)
        self.goto(position)
# *************************** UP and DOWN METHODS ********************

    def up(self):
        if self.ycor() <= 240:
            new_y = self.ycor() + UP
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -230:
            new_y = self.ycor() - DOWN
            self.goto(self.xcor(), new_y)
            