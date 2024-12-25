from turtle import Turtle

score = Turtle()
ALIGN = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard:
    def __init__(self):
        self.new_score = 0

    def pnt_scr(self):
        score.hideturtle()
        score.penup()
        score.goto(10, 270)
        score.color("orange")
        score.clear()
        score.write(f"score: {self.new_score}", move=False, align=ALIGN, font=FONT)
        self.new_score = self.new_score + 1

    def game_over(self):
        text = "GAME  OVER"
        score.color("white")
        score.clear()
        score.goto(0, 0)
        score.write(f"{text} \n your score is {self.new_score - 1}", move=False, align="center",
                    font=('Arial', 35, 'normal'))


ScoreBoard()
