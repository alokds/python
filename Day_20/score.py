from turtle import Turtle


score = Turtle()

ALIGN = "center"
FONT = ('Arial', 10, 'normal')


class ScoreBoard:
    def __init__(self):
        self.new_score = 0
        self.highest_score = 0

    def pnt_scr(self):
        score.hideturtle()
        score.penup()
        score.goto(10, 270)
        score.color("orange")
        # self.update_score()

    def update_score(self):
        score.clear()
        score.write(f"SCORE: {self.new_score}  HIGHEST-SCORE = {self.highest_score}",
                    move=False, align=ALIGN, font=FONT)

    def reset(self):
        if self.new_score > self.highest_score:
            self.highest_score = self.new_score
        self.new_score = 0
        self.update_score()

    def increase_score(self):
        self.new_score += 1
        self.update_score()

    # def game_over(self):
    #     text = "GAME  OVER"
    #     score.color("white")
    #     score.clear()
    #     score.goto(0, 0)
    #     self.reset()
    #     score.write(f" {text} SCORE: {self.new_score}  HIGHEST-SCORE = {self.highest_score}",
    #                 move=False, align=ALIGN, font=FONT)


ScoreBoard()
