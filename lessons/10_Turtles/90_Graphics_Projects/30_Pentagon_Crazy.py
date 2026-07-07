"""
# 30_Pentagon_Crazy.py

This program already works. Run it, then change it to make it draw a different pattern.

uid: QG1OFNKY
name: Pentagon Crazy
"""

import random
import turtle

colors = ("red", "black")

def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

def get_next_color(i):
    return colors[i % len(colors)]

window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600, startx=0, starty=0)

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.speed(5000)
my_turtle.width(5)

sides = 11
angle = 2000 / sides

for i in range(10000):
    if i == 50:
        my_turtle.width(6)
    if i == 100:
        my_turtle.width(7)
    if i == 150:
        my_turtle.width(8)
    if i == 200:
        my_turtle.width(9)
    if i == 250:
        my_turtle.width(10)
    if i == 300:
        my_turtle.width(11)
    if i == 350:
        my_turtle.width(12)
    my_turtle.pencolor(get_next_color(i))
    my_turtle.forward(i)
    my_turtle.right(angle + 1)

my_turtle.hideturtle()

turtle.done()
