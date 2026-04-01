import turtle

t = turtle.Turtle()
turtle.hideturtle()


def set_screen(bgcolor, title, x, y):
    screen = turtle.Screen()
    screen.setup(width=x, height=y)
    screen.bgcolor(bgcolor)
    # turtle.title(title)


# WHY THE SETTING OF STARTING POSITION IS NOT WORKING?
# I ALSO TRIED USING GOTO, SAME RESULT

def set_start_pos(x, y):
    turtle.penup()
    turtle.setx(-x)
    turtle.sety(-y)
    turtle.pendown()


def draw_filled_square(length, fill_color):
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()
    turtle.end_fill()


set_screen("lightgrey", "Martin's Turtle Show", 800, 400)
set_start_pos(200, 5)
draw_filled_square(30, "red")
draw_filled_square(60, "blue")
draw_filled_square(90, "green")
turtle.done()