from turtle import Turtle, Screen
import random
screen = Screen()
COLORS = ['red', 'green', 'yellow', 'purple', 'blue', 'pink']
SPEED_INCREMENT = 5


class CAR:
    def __init__(self):
        self.all_cars = []
        self.CAR_SPEED = 5

    def create_car(self):
        random_chance = random.randint(1, 3)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.CAR_SPEED)

    def increase_speed(self):
        self.CAR_SPEED += SPEED_INCREMENT
