import random

import colorgram
import turtle

colors = colorgram.extract("/home/murat/PycharmProjects/hirst-painting/image.jpeg", 25)
johnny = turtle.Turtle()
johnny.pencolor("white")
turtle.colormode(255)
johnny.hideturtle()
colors_list = []
johnny.speed("fastest")
for color in colors:
    colors_list.append(color.rgb)
turtle_position_y = -200
johnny.penup()
for i in range(0, 10):
    johnny.setpos(-200, turtle_position_y)

    for k in range(0, 10):
        johnny.dot(20,colors_list[random.randint(0, len(colors_list)-1)])
        johnny.forward(50)
        turtle_position_y += 5
screen = turtle.Screen()
screen.exitonclick()
