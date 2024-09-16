import random
import turtle as t
from turtle import Turtle, Screen

t.colormode(255)
tim = Turtle()
tim.shape("classic")
tim.hideturtle()
tim.penup()
tim.speed("fastest")
number_of_dots = 10

# color_list = [(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35),
#               (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64),
#               (56, 39, 19), (41, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (224, 93, 79),
#               (243, 163, 161), (38, 32, 34), (3, 25, 25), (80, 147, 169), (161, 26, 22), (21, 78, 90),
#               (234, 167, 171), (171, 206, 190), (103, 127, 156), (165, 202, 210), (61, 60, 72), (183, 190, 204),
#               (78, 66, 42), (23, 99, 96)]

#                                   --------------------------------------------------------------
#                                             colorgram module to extract colors from image.jpg
#                                   --------------------------------------------------------------

#import colorgram
#rgb_colors = []
#colore =  colorgram.extraxt('image.jpg', 30)
#for color in colors:
#       r = color.rgb.r
#       g = color.rgb.g
#       b = color.rgb.b
#       new_color = (r, g, b)
#       rgb_colors.append(new_color)
#                                   --------------------------------------------------------------
#                                   --------------------------------------------------------------




def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


#                               -------------------------
#                                   write Dashed Line
#                               -------------------------
# tim.penup()
# tim.setx((-300))
# tim.sety(-200)
# for _ in range(25):
#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
#                               ----------------------------
#                                  draw different shapes
#                               ----------------------------

# def draw_shape(sides):
#     tim.color(random_color())
#     angle = 360 / sides
#     for _ in range(sides):
#         tim.fd(100)
#         tim.rt(angle)
#
#
# for num_sides in range(3, 11):
#     draw_shape(num_sides)

#                                ----------------------------
#                                       draw random Walk
#                                ----------------------------

# direction = [0, 90, 180, 270]
#
# tim.penup()
# tim.setx((-300))
# tim.sety(-200)
# tim.pendown()
#
# for _ in range(200):
#     tim.color(random_color())
#     tim.speed("fastest")
#     tim.pensize(10)
#     tim.setheading(random.choice(direction))
#     tim.fd(30)


#                                ----------------------------
#                                       draw a spirograph
#                                ----------------------------
# i = 5
# for _ in range(int(360 / i)):
#     tim.color(random_color())
#     tim.speed("fastest")
#     tim.circle(100)
#     tim.lt(i)

#                                  ------------------------------
#                                       draw Hirst Painting
#                                   -----------------------------

def set_pos():
    tim.setpos((-20 * number_of_dots), -(20 * number_of_dots) + (50 * dot_count))


def dot_painting():
    # tim.dot(20, random.choice(color_list))
    tim.dot(20, random_color())
    tim.fd(50)


for dot_count in range(number_of_dots):
    set_pos()
    for _ in range(number_of_dots):
        dot_painting()

screen = Screen()
screen.exitonclick()
