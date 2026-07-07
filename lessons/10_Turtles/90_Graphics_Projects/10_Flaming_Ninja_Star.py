"""
# 10_Flaming_Ninja_Star.py

This program already works; run it to see what it does.
Then change it to make it draw a different pattern.

uid: ejUIkGvk
name: Flaming Ninja Star
"""

import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = (import turtle

def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path                        # Import Path from pathlib module
    image_dir = Path(__file__).parent / "images"    # Define the directory containing images
    image_path = str(image_dir / image_name)        # Create the full path to the image file

    screen = turtle.getscreen()                     # Get the turtle's screen
    screen.addshape(image_path)                     # Register the image as a shape
    turtle.shape(image_path)                        # Set the turtle's shape to the image

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "pikachu.gif")

t.penup()   # Prevent drawing when moving
t.speed(3)  # Set a moderate speed

# Move the turtle to each corner of the screen in a square pattern
for x, y in [(200, 200), (200, -200), (-200, -200), (-200, 200)]:
    t.goto(x, y)

turtle.exitonclick() "red", black", "yellow", "orange")


def get_next_color(i):
    return colors[i % len(colors)]

turtle.setup(600, 600, 0, 0)            # Set the size of the window
window = turtle.Screen()

base_size = 200  # the size of the black part of the star
flame_size = 1300  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2)
t.speed(0)

for i in range(25):
    t.pencolor(get_random_color())
    t.fillcolor(get_random_color())
    t.begin_fill()
    t.forward(64)
    t.left(40)
    t.forward(flame_size)
    t.right(170)
    t.forward(flame_size)
    t.right(62)
    t.forward(base_size)
    t.end_fill()

t.hideturtle()

turtle.done()
