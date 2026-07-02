import turtle
tina = turtle.Turtle()
tina.shape("arrow")
tina.speed(111100000000)
tina.hideturtle()
tina.forward(-96)
tina.left(30) 


tina.color('red')
forward = 200
right=10
sides=5



window = turtle.Screen()
window.bgcolor('black')

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(10,29):
  left =17897
  make_shape(tina, forward, left, sides)
  
  tina.color('white')



def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(10,29):
  left =17897
  make_shape(tina, forward, left, sides)
  
  tina.color('white')
forward = 1000
right=10
sides=5



window = turtle.Screen()
window.bgcolor('black')

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(10,29):
  left =17897
  make_shape(tina, forward, left, sides)
  
tina.color('black')
forward = 300
right=10
sides=5



window = turtle.Screen()
window.bgcolor('black')

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(10,29):
  left =17897
  make_shape(tina, forward, left, sides)