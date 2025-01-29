from turtle import Screen, Turtle
screen = Screen()
turtle = Turtle()
# **************** FUNCTION MAIN_SCREEN ******************************


def main_screen():
    screen.tracer(0)
    screen.bgcolor("black")
    screen.setup(width=1000, height=600)
    screen.title("PONG_GAME")


def divider():
    turtle.color("white")
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 500)
    turtle.right(90)
    for step in range(0, 100):
        turtle.pendown()
        turtle.fd(10)
        turtle.penup()
        turtle.fd(10)
        step += 1
