from turtle import Turtle
score = Turtle()
FONT = ('Arial', 20, 'normal')


class ScorePoint(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.green_point = 0
        self.yellow_point = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.color("green")
        self.goto(250, 250)
        self.write(f"score: {self.green_point}", align="right", font=FONT)
        self.color("yellow")
        self.goto(-250, 250)
        self.write(f"score: {self.yellow_point}", align="right", font=FONT)

    def green_score(self):
        self.green_point += 1
        self.update_score()

    def yellow_score(self):
        self.yellow_point += 1
        self.update_score()
