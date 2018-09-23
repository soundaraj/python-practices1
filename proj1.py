import turtle
sound=turtle.Turtle()
sound.speed(1)
def square(length,angle):
    for i in range(4):
        sound.forward(length)
        sound.right(angle)
for i in range(100):
    square(50,90)
    sound.right(10)
