from turtle import Turtle, Screen
from score import Score

screen = Screen()
score = Score()
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 250


# ********************************  ROAD CROSSING TURTLE  **************************

class RaceMan(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        screen.listen()
        screen.onkey(self.go_up, "Up")

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            score.new_score += 1
            score.score()
            return True
        else:
            return False
