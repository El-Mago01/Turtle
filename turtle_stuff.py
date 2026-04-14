import turtle

back_ground_color = "lightgrey"
side_size = 100
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


def draw_filled_square(start_angle, length, fill_color, direction):
    turtle.pendown()
    if fill_color != "None":
        fill_color = back_ground_color
        turtle.fillcolor(fill_color)
        turtle.fill(True)

    if direction == "left":
        turtle.left(start_angle)
        turtle.forward(length / 2)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length / 2)
    # turtle.left(90)
    else:
        turtle.right(start_angle)
        turtle.forward(length / 2)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length / 2)
    # turtle.forward(length)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()


set_screen(back_ground_color, "Martin's Turtle Show", 800, 400)
change_pos(start_pos_x, start_pos_y)
nr_of_squares = 5
cur_square = 1
starting_angle = -18

angle_increase = -72
while cur_square <= nr_of_squares:
    if cur_square == 1:
        draw_filled_square(starting_angle, side_size, "None", "right")
    else:
        draw_filled_square(angle_increase, side_size, "None", "right")
    change_pos(start_pos_x, start_pos_y)
    # cur_angle+=angle_increase
    cur_square += 1
turtle.done()