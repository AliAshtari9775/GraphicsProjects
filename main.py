import random
import turtle as t
from turtle import Turtle, Screen


def draw_shape(i):
    tim.shape('circle')
    tim.color("green")
    angle = 360 / i
    for j in range(i):
        tim.forward(100)
        tim.right(angle)


def random_walk(steps):
    tim.shapesize(1)
    tim.pensize(20)
    tim.speed('fastest')
    directions_angle_list = [0, 90, 180, 270]
    for _ in range(steps):
        tim.color(random_color())
        direction_angle = random.choice(directions_angle_list)
        tim.setheading(direction_angle)
        tim.forward(40)


def make_spirograph(number_of_circles):
    angle = 360 / number_of_circles
    for i in range(number_of_circles):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.setheading((i + 1) * angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


tim = Turtle()
tim.speed('fastest')
t.colormode(255)

# screen1 = Screen()
# steps = 200
# random_walk(steps)
# screen1.exitonclick()
#
# screen2 = Screen()
# n = 40
# make_spirograph(n)
# screen2.exitonclick()
