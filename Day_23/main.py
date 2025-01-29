from screen import main_screen, path
from time import sleep
from race_man import RaceMan
from turtle import Screen
from car import CAR

screen = Screen()
screen.tracer(0)
main_screen()
path()
car = CAR()
RaceMan = RaceMan()
game_is_on = True
FONT = ('Arial', 35, 'normal')
# *******************RACE GAME  **************************88
while game_is_on:
    sleep(0.09)
    screen.update()
    car.create_car()
    car.move_cars()

# **************DETECT FINISH LINE AND RESTART  AND INCREASE CAR SPEED ****************
    if RaceMan.is_at_finish_line():
        RaceMan.go_to_start()
        car.increase_speed()

# ******************Detect COLLISION with CAR  **************************
    for collide_car in car.all_cars:
        if collide_car.distance(RaceMan) < 25:
            game_is_on = False
            collide_car.color("white")
            collide_car.goto(0, 0)
            collide_car.write(f"GAME OVER", align="center", font=FONT)

screen.exitonclick()
