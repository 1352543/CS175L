#CS175L
#Andrew Fisher
#STOP
import turtle
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45

turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
#DIAMETER
#MOVE TO STARTING POINT
turtle.pensize(20)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.color("red")
for x in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)
turtle.end_fill()

turtle.penup()
turtle.goto(0,-5)
turtle.pendown()

turtle.pensize(10)
turtle.fillcolor("white")
turtle.color("white")
for x in range(NUM_SIDES):
    turtle.forward(LENGTH / 1.05)
    turtle.right(ANGLE)

turtle.penup()
turtle.goto(-10,-145)
turtle.pendown()
turtle.fillcolor("white")
turtle.color("white")
turtle.write("STOP", font=("Arial", 45, "normal", "bold"))

turtle.hideturtle()
