from turtle import Turtle, Screen
from time import sleep
screen = Screen()


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
IS_GAME_ON = True
MOVE_DISTANCE = 10


class Snake:
    def __init__(self):
        self.segments = []
        # self.screen_setup()
        self.head = []

    def screen_setup(self):
        screen.tracer(0)
        screen.setup(600, 600)
        screen.bgcolor("black")
        screen.title('Snake Game')
        Snake.create_snake(self)

#  ********************      Snake Definition        ****************/

    def create_snake(self):
        for index in range(-2, 1):
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.setx(index * 20)
            self.segments.append(new_snake)
        Snake.game(self)
# ***********************  MoveForward The Snake       ***********************/

    def game(self):
        while IS_GAME_ON:
            Screen().update()
            sleep(0.09)
            for seg_pos in range(len(self.segments) - 1, 0, -1):
                new_x = self.segments[seg_pos - 1].xcor()
                new_y = self.segments[seg_pos - 1].ycor()
                self.segments[seg_pos].goto(new_x, new_y)
            self.head = self.segments[0]
            self.segments[0].fd(MOVE_DISTANCE)
            screen.listen()
            screen.onkey(self.up, "Up")
            screen.onkey(self.down, "Down")
            screen.onkey(self.left, "Left")
            screen.onkey(self.right, "Right")

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
