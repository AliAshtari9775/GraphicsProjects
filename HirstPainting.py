import random
import turtle as t
from ExtractedColors import color_list

def random_color():
    color_tuple = random.choice(color_list)
    return color_tuple


from main import random_color

tim = t.Turtle()
screen3 = t.Screen()
t.colormode(255)

x_num = 10
y_num = 10
tim.pu()

tim.setx(-(x_num/2)*50)
tim.sety(-(y_num/2)*50)

for j in range(y_num):
    for i in range(x_num):
        x_shift = -((x_num/2)-i)*50
        y_shift = -((y_num/2)-j)*50
        tim.teleport(x_shift,y_shift)
        tim.dot(20,random_color())


screen3.exitonclick()
