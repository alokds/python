from turtle import Screen, Turtle
from screen import main_screen, divider
from paddle import Paddle
from time import sleep
from ball import Ball
from pntscr import ScorePoint
turtle = Turtle
main_screen()
divider()
screen = Screen()
ball = Ball()
point = ScorePoint()
is_game_on = True


# ************************* GREEN (RIGHT) PADDLE *************************
screen.listen()
green_paddle = Paddle((470, 0), color="green")
screen.onkey(green_paddle.up, "Up")
screen.onkey(green_paddle.down, "Down")
# ************************* YELLOW (LEFT) PADDLE *************************

yellow_paddle = Paddle((-480, 0), color="yellow")
screen.onkey(yellow_paddle.up, "q")
screen.onkey(yellow_paddle.down, "w")


while is_game_on:
    sleep(ball.set_sleep)
    screen.update()
    ball.ball_point()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bouncey()
    if ((ball.distance(green_paddle) < 50 and ball.xcor() >= 450) or
            (ball.distance(yellow_paddle) < 50 and ball.xcor() <= -450)):
        ball.bouncex()
    if ball.xcor() > 490:
        ball.bounce_back()
        point.yellow_score()

    if ball.xcor() < -490:
        ball.bounce_back()
        point.green_score()


screen.exitonclick()
