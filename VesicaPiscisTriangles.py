import turtle
import random
import math

# Vesica Piscis and equilateral triangles from 2 circles
# partition into lessons skeleton code
# extras?..golden mean, circles at intersects, emphasise hexagons

def get_intersection_points(Circle1, Circle2):
  # taken from 
  # https://www.xarg.org/2016/07/calculate-the-intersection-points-of-two-circles/
  # credit Robert Eisele
  # adapted to Python
  
  d = math.hypot(Circle2.x - Circle1.x, Circle2.y - Circle2.y)
  
  if d <= (Circle1.r + Circle2.r):
    
    ex = (Circle2.x - Circle1.x) / d
    ey = (Circle2.y - Circle2.y) / d

    x = (Circle1.r * Circle1.r - Circle2.r * Circle2.r + d * d) / (2 * d)
    y = math.sqrt(Circle1.r * Circle1.r - x * x)
    
    p1 = (Circle1.x + x * ex - y * ey, Circle1.y + x * ey + y * ex)
    p2 = (Circle1.x + x * ex + y * ey, Circle1.y - x * ey - y * ex)
    return p1,p2

  else:
    return False
      
    

# circle class that inherits from the Turtle class
class Circle(turtle.Turtle):
  def __init__(self, x, y, radius):
    turtle.Turtle.__init__(self)
    self.hideturtle()
    self.penup()
    self.goto(x, y)
    self.pendown()
    self.r = radius
    self.x = x
    self.y = y + radius # turtle draws from base
    
screen = turtle.Screen().bgcolor("lightgreen")

# set size of circles
RADIUS = 100
x = -RADIUS/2
y = -RADIUS


# create the left circle
left_circle = Circle(x, y, RADIUS)
left_circle.pencolor("blue")
left_circle.circle(RADIUS)


# create the right circle
right_circle = Circle(x + RADIUS, y, RADIUS)
right_circle.pencolor("blue")
right_circle.circle(RADIUS)


# create equal triangles
points = get_intersection_points(left_circle, right_circle)
if points:
  intersect1 = points[0]
  intersect2 = points[1]
  
  
  # create a new turtle to draw the triangles
  triangles = turtle.Turtle()
  triangles.hideturtle()
  triangles.penup()
  triangles.goto(left_circle.x, left_circle.y)
  triangles.pendown()
  triangles.pencolor("red")
  
  
  # draw the 2 vesica piscis triangles
  triangles.goto(intersect1[0], intersect1[1])
  triangles.goto(right_circle.x, right_circle.y)
  triangles.goto(intersect2[0], intersect2[1])
  triangles.goto(left_circle.x, left_circle.y)
  triangles.goto(right_circle.x, right_circle.y)
  
  
  # get triangle side length
  dist = abs(right_circle.x - left_circle.x)
  
  #bottom right 1
  triangles.goto(intersect2[0], intersect2[1])
  triangles.fd(dist)
  triangles.left(120)
  triangles.fd(dist)
  
  # bottom left 1
  triangles.penup()
  triangles.goto(intersect2[0], intersect2[1])
  triangles.left(60)
  triangles.pendown()
  triangles.fd(dist)
  triangles.right(120)
  triangles.fd(dist)
  
  # bottom left 2
  triangles.left(120)
  triangles.fd(dist)
  triangles.left(120)
  triangles.fd(dist)
  
  # top left 
  triangles.goto(left_circle.x, left_circle.y)
  triangles.left(180)
  triangles.fd(dist)
  triangles.left(120)
  triangles.fd(dist)
  
  triangles.penup()
  triangles.goto(intersect1[0], intersect1[1])
  triangles.right(60)
  triangles.pendown()
  triangles.fd(dist)
  
  # top right
  triangles.goto(intersect1[0], intersect1[1])
  triangles.right(180)
  triangles.fd(dist)
  triangles.right(120)
  triangles.fd(dist)
  
  triangles.left(120)
  triangles.fd(dist)
  triangles.left(120)
  triangles.fd(dist)
  
  # bottom right 2
  triangles.left(120)
  triangles.fd(dist)
  triangles.left(60)
  triangles.fd(dist)
  triangles.left(120)
  triangles.fd(dist)