import turtle

back_ground_color = "lightgrey"
side_size = 10
start_pos_x = -200
start_pos_y = 0

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
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()


def draw_shape(start_angle, sides, length, pen_color, direction):
    turtle.pendown()
    if pen_color != "None":
        turtle.pencolor(pen_color)
        # turtle.fillcolor(pen_color)
        # turtle.fill(True)

    angle = 360 / sides

    current_side = 1
    if direction == "left":
        turtle.left(start_angle)
        while (current_side <= sides):
            turtle.forward(length)
            turtle.left(angle)
            current_side += 1
    else:
        while (current_side <= sides):
            turtle.forward(length)
            turtle.right(angle)
            current_side += 1

    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()


set_screen(back_ground_color, "Martin's Turtle Show", 800, 400)
change_pos(start_pos_x, start_pos_y)

starting_angle = 60

draw_shape(starting_angle, 20, side_size, "blue", "right")
turtle.done()