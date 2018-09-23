import turtle
myturtle = turtle.Turtle()
def pent(length,angle):
    for i in range(5):
        myturtle.forward(length)
       #myturtle.backward(10)
        myturtle.left(angle)
pent(120,72)
