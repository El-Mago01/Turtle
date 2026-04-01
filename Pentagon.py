import turtle

t = turtle.Turtle()
side_size = 12
number_of_sides = 5
side = 1
angle = 72
turtle.begin_fill()
turtle.pencolor("purple")
turtle.fillcolor("yellow")

while side <= number_of_sides:
    turtle.forward(side_size)
    turtle.right(angle)
    side += 1

turtle.end_fill()