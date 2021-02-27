import turtle
import random
import math

# STEP 1 - Global vars and constants etc
# allows some vars as global and not others in f of life function ... ????
RADIUS = 20.0
x = 0.0
y = -5*RADIUS
golden_ratio = 1.61803398875
metranons_circles = []
name = "Circle"
circle_number = 1
screen = turtle.Screen()



# Metranons Cube

"""
add an image of circles with numbers (paint or other)
plus ping pong balls for class
"""

# circle class that inherits from the Turtle class
class Circle(turtle.Turtle):
  def __init__(self, x, y, radius, name):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.penup()
    self.goto(x, y)
    self.pendown()
    self.pensize(3)
    self.r = radius
    self.x = x
    self.y = y # turtle draws from base so plus radius for centre
    self.name = name
    
  def __repr__(self):
    return self.name + " x = " + str(self.x) + " y = " + str(self.y)
 
# STEP 3 - draw all lines to show metranons cube    
def metranons_cube(circlesList):
  lines = turtle.Turtle()
  lines.pencolor("lightblue")
  for i in range(len(circlesList)):
    
    for j in range(i+1, len(circlesList)):
      
      lines.goto(circlesList[i].x, circlesList[i].y+RADIUS)
      lines.goto(circlesList[j].x, circlesList[j].y+RADIUS)
      
  lines.hideturtle()  
  
def cube_hexahedron(circlesList):
  # circles 1,3,5,7,8,10,12 (-1 for list entries)
  lines = turtle.Turtle()
  
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[6].x, circlesList[6].y + RADIUS)
  lines.goto(circlesList[2].x, circlesList[2].y + RADIUS)
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.penup()
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.pendown()
  lines.goto(circlesList[6].x, circlesList[6].y + RADIUS)
  lines.hideturtle()
  
def tetrahedron(circlesList):
  lines = turtle.Turtle()
  
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.home()
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.home()
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.hideturtle()
  
def octahedron(circlesList):
  
  lines = turtle.Turtle()
  lines.penup()
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.pendown()
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[6].x, circlesList[6].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.hideturtle()
  
def icosahedron(circlesList):
  lines = turtle.Turtle()
  lines.penup()
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.pendown()
  
  lines.goto(circlesList[6].x, circlesList[6].y + RADIUS)
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[3].x, circlesList[3].y + RADIUS)
  lines.goto(circlesList[9].x, circlesList[9].y + RADIUS)
  lines.goto(circlesList[8].x, circlesList[8].y + RADIUS)
  lines.goto(circlesList[3].x, circlesList[3].y + RADIUS)
  lines.goto(circlesList[8].x, circlesList[8].y + RADIUS)
  lines.goto(circlesList[6].x, circlesList[6].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[8].x, circlesList[8].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[9].x, circlesList[9].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.goto(circlesList[9].x, circlesList[9].y + RADIUS)
  lines.hideturtle()
  
def star_tetrahedron(circlesList):
  lines = turtle.Turtle()
  lines.goto(circlesList[3].x, circlesList[3].y + RADIUS)
  lines.goto(circlesList[9].x, circlesList[9].y + RADIUS)
  lines.goto(circlesList[8].x, circlesList[8].y + RADIUS)
  lines.goto(circlesList[2].x, circlesList[2].y + RADIUS)
  lines.goto(circlesList[3].x, circlesList[3].y + RADIUS)
  lines.goto(circlesList[8].x, circlesList[8].y + RADIUS)
  lines.home()
  lines.goto(circlesList[9].x, circlesList[9].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[3].x, circlesList[3].y + RADIUS)
  lines.goto(circlesList[11].x, circlesList[11].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.goto(circlesList[9].x, circlesList[9].y + RADIUS)
  lines.goto(circlesList[10].x, circlesList[10].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[8].x, circlesList[8].y + RADIUS)
  lines.goto(circlesList[7].x, circlesList[7].y + RADIUS)
  lines.goto(circlesList[4].x, circlesList[4].y + RADIUS)
  lines.goto(circlesList[3].x, circlesList[3].y + RADIUS)
  lines.goto(circlesList[6].x, circlesList[6].y + RADIUS)
  lines.goto(circlesList[0].x, circlesList[0].y + RADIUS)
  lines.hideturtle()
  
  
  
  
# STEP2 - Create the 13 circles aka Flower of Life and put them in a list

def flower_of_life(visible, x, y, circle_number):
  
  # create the 5 vertical circles
  for i in range(5):
    new_circle = Circle(x, y, RADIUS, name + str(circle_number))
    if visible:
      new_circle.circle(RADIUS)
    metranons_circles.append(new_circle)
    circle_number += 1
    y = y + 2*RADIUS
  
  
  # right arm circles
  y = y - 5*RADIUS
  x = x + RADIUS + RADIUS/golden_ratio
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  y = y + RADIUS
  x = x + RADIUS + RADIUS/golden_ratio
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  # right leg circles
  y = y - 4*RADIUS
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  y = y + RADIUS
  x = x = x - RADIUS - RADIUS/golden_ratio
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  # left leg circles
  x = x - 2*RADIUS - 2*(RADIUS/golden_ratio)
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  y = y - RADIUS
  x  = x - RADIUS - RADIUS/golden_ratio
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  # right arm circles
  y = y + 4*RADIUS
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
  y = y - RADIUS
  x  = x + RADIUS + RADIUS/golden_ratio
  new_circle = Circle(x, y, RADIUS, name + str(circle_number))
  if visible:
    new_circle.circle(RADIUS)
  metranons_circles.append(new_circle)
  circle_number += 1
  
def platonic_solids(metranons_circles):
  # only displays first then clears and wont redisplay
  
  #metranons_cube(metranons_circles)
  #screen.clear()
  cube_hexahedron(metranons_circles)
  #screen.clear()
  tetrahedron(metranons_circles)
  #screen.clear()
  octahedron(metranons_circles)
  #screen.clear()
  icosahedron(metranons_circles)
  #screen.clear()
  star_tetrahedron(metranons_circles)
  
flower_of_life(False, x, y, circle_number)
star_tetrahedron(metranons_circles)
#platonic_solids(metranons_circles)
#cube_hexahedron(metranons_circles)
#tetrahedron(metranons_circles)
#metranons_cube(metranons_circles)
#octahedron(metranons_circles)
#icosahedron(metranons_circles)

print(metranons_circles)