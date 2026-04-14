import turtle
john = turtle.Turtle()

john.width(5)
john.penup()
john.back(140)
john.pendown()

for color in ["red", "blue", "green"]:
  john.color(color)
  john.forward(10)
  john.penup()
  john.forward(10)
  john.pendown()

turtle.done()