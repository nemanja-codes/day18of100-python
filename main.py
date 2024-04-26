# import colorgram
import random
import turtle
from turtle import Turtle, Screen

# colors = colorgram.extract('image.jpg', 22)
#
# rgb = []
# for n in range(len(colors)):
#     r = colors[n].rgb.r
#     g = colors[n].rgb.g
#     b = colors[n].rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
#
# print(rgb)

color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176),
              (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169),
              (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82)]

timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")
timmy.hideturtle()
x = -250
y = -200
timmy.teleport(x, y)
for _ in range(10):
    for _ in range(10):
        timmy.pencolor(random.choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    y += 50
    timmy.teleport(x, y)


s = Screen()
s.exitonclick()