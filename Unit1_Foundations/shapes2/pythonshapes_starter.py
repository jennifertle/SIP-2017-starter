from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(2000,1800)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
n= input('how many sides of a shape?:')
print(n)
move = 500
for move in range (n):
    move = forward (180)
    move = right(360/n)
