import turtle
import random
'''
needs mod for Pythonista

'''
# circle class that inherits from the Turtle class
class Circle(turtle.Turtle):
  def __init__(self, x, y, radius):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.penup()
    self.goto(x, y)
    self.pendown()
    self.r = radius

# set the background colour
screen = turtle.Screen()
screen.bgcolor("lightblue")

# create a list to store the circles and set variables
Circles = []
screen_width = 200
screen_height = 200
no_of_circles = 200
colour_range = 255.0

for i in range(no_of_circles):
  
  # ensure circles are on canvas 
  radius = random.randint(2, 100)
  width = screen_width - 2*radius
  height = screen_height - 2*radius
  
  # random r g b values
  r = random.uniform(0.0, colour_range)
  g = random.uniform(0.0, colour_range)
  b = random.uniform(0.0, colour_range)
  colour = (r,g,b)
  
  # random x y coordinates
  x = random.randint(-width,width)
  y = random.randint(-height,height)
  
  # create new circle, set pen colour and add to list of circles
  new_circle = Circle(x, y, radius)
  new_circle.pencolor(colour)
  Circles.append(new_circle)

# loop through the list of circles and draw them
screen = turtle.Screen()
for item in Circles:
  item.circle(item.r)