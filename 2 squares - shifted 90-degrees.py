import turtle

back_ground_color = "lightgrey"
side_size = 50
start_pos_x = 200
start_pos_y = 50

t = turtle.Turtle()
turtle.hideturtle()
turtle.penup()


def set_screen(bgcolor, title, x, y):
    screen = turtle.Screen()
    screen.setup(width=x, height=y)
    screen.bgcolor(bgcolor)
    # turtle.title(title)


# WHY THE SETTING OF STARTING POSITION IS NOT WORKING?
# I ALSO TRIED USING GOTO, SAME RESULT

def change_pos(x, y):
    turtle.penup()
    turtle.setx(-x)
    turtle.sety(-y)
    turtle.pendown()


def draw_filled_square(start_angle, length, fill_color):
    turtle.pendown()
    if fill_color != "None":
        fill_color = back_ground_color
        turtle.fillcolor(fill_color)
        turtle.fill(True)

    turtle.left(start_angle)
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


set_screen(back_ground_color, "Martin's Turtle Show", 800, 400)
change_pos(start_pos_x, start_pos_y)
draw_filled_square(0, side_size, "None")
change_pos(start_pos_x - 0.5 * side_size, start_pos_y + 0.25 * side_size)
draw_filled_square(45, side_size, "None")
turtle.done()
