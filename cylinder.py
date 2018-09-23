# DRAW THE CYLINDER USING TURTLE

import turtle
myturtle = turtle.Turtle()
def pent(length,angle): 
    for i in range(13):
        myturtle.forward(length) 
        myturtle.left(angle)
pent(20,36)
myturtle.right(16)
myturtle.forward(100)
for i in range(16):
        myturtle.forward(20)
        myturtle.left(36)
myturtle.right(38)
myturtle.forward(100)
myturtle.hideturtle()
