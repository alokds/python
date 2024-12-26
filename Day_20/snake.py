from turtle import Turtle, Screen
from time import sleep
from food import Food
from score import ScoreBoard

screen = Screen()
food = Food()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 10
STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]

# ****************Initialise SNAKE class with ScoreBoard Class as Super**************


class Snake(ScoreBoard):
    def __init__(self):
        super().__init__()
        self.segments = []

# ********************Snake Definition ***********************************

    def snake_def(self, position):
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.shapesize(0.5, 0.5)
        new_snake.color("white")
        new_snake.goto(position)
        self.segments.append(new_snake)

# ******************Define Snake Tail *******************************

    def snake_tail(self):
        self.snake_def(self.segments[-1].position())

# **************Screen Set UP definition *********************************

    def screen_setup(self):
        screen.tracer(0)
        screen.bgcolor("black")
        screen.setup(600, 600)
        screen.title(f"Snake Game")
        Snake.create_snake(self)

#  ********************      Snake Definition        ****************/

    def create_snake(self):
        for position in STARTING_POSITION:
            self.snake_def(position)
        Snake.game(self)

# ** ** ** ** ** ** ** ** ** ** ** *MoveForward    The Snake ** ** ** ** ** ** ** ** ** ** ** * /
    def move(self):
        for seg_pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_pos - 1].xcor()
            new_y = self.segments[seg_pos - 1].ycor()
            self.segments[seg_pos].goto(new_x, new_y)
        self.segments[0].fd(MOVE_DISTANCE)

# ***********************   Snake Game       ***********************/

    def game(self):
        Snake.pnt_scr(self)
        is_game_on = True
        while is_game_on:
            Screen().update()
            sleep(0.09)
            Snake.move(self)
            screen.listen()
            screen.onkey(self.up, "Up")
            screen.onkey(self.down, "Down")
            screen.onkey(self.left, "Left")
            screen.onkey(self.right, "Right")
            if self.segments[0].distance(food) <= 10:
                food.new_loc()
                Snake.pnt_scr(self)
                Snake.snake_tail(self)
            if (self.segments[0].xcor() > 290 or self.segments[0].xcor() < -290 or self.segments[0].ycor() > 270
                    or self.segments[0].ycor() < -290):
                is_game_on = False
                self.game_over()
# **********************   Detect Collision with Tail ************************************
            for segment in self.segments[1:]:
                if self.segments[0].distance(segment) < 5:
                    self.game_over()
                    is_game_on = False


# ***********************Snake Direction Control ************************************
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
