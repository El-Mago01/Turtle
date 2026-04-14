import turtle
import math

back_ground_color = "lightgrey"
side_size = 50
start_pos_x = 0
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
    turtle.setx(-x)
    turtle.sety(-y)
    turtle.pendown()


def draw_filled_square(angle, center_pos_x, center_pos_y, padding, direction, fill_color:str, pen_color:str):
    turtle.penup()
    change_pos(center_pos_x, center_pos_y)
    turtle.penup()
    if fill_color is not None:
        fill_color = back_ground_color
        turtle.fillcolor(fill_color)
        turtle.begin_fill()


    # Go to start position in the square.
    # length of the square will be 2x the padding
    turtle.color(pen_color)
    if direction == "left":
        turtle.left(angle)
        turtle.forward(padding)
        turtle.left(90)
        # turtlehead is now in the right direction
        turtle.pendown()
        turtle.forward(padding)
        turtle.left(90)
        turtle.forward(2*padding)
        turtle.left(90)
        turtle.forward(2*padding)
        turtle.left(90)
        turtle.forward(2*padding)
        turtle.left(90)
        turtle.forward(padding)
    else:
        turtle.right(angle)
        turtle.forward(padding)
        turtle.right(90)
        # turtlehead is now in the right direction
        turtle.pendown()
        turtle.forward(padding)
        turtle.right(90)
        turtle.forward(2*padding)
        turtle.right(90)
        turtle.forward(2*padding)
        turtle.right(90)
        turtle.forward(2*padding)
        turtle.right(90)
        turtle.forward(padding)

    # turtle.forward(length)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()

def create_squares(angle, nr_of_squares,start_pos_x, start_pos_y,
                   padding, fill_color_list, pen_color_list,small_to_large):
    set_screen(back_ground_color, "Martin's Turtle Show", 800, 400)
    change_pos(start_pos_x, start_pos_y)
    cur_square =0
    if small_to_large:
        base_to_center=padding
    else:
        base_to_center=padding*nr_of_squares
    center_pos_x = start_pos_x
    center_pos_y = start_pos_y

    while cur_square <= nr_of_squares:
        if len(pen_color_list) <= cur_square+1:
            pen_color_list.append("black")
        if len(fill_color_list) < cur_square+1:
            fill_color_list.append(None)
        draw_filled_square(angle, center_pos_x, center_pos_y, base_to_center, "left",
                           fill_color_list[cur_square], pen_color_list[cur_square])
        if small_to_large:
            base_to_center += padding
        else:
            base_to_center -= padding

        cur_square += 1
        angle = 0


def main():
    turtle.speed(6)
    padding=20
    angle = 45
    pen_color = ["red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple"]
    #fill_color = ["red", "orange", "black", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue","orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple"]
    fill_color = [None, None, None, None, None, None, None]
    nr_of_squares = 20
    create_squares(angle,nr_of_squares,start_pos_x,start_pos_y,
                   padding, fill_color,pen_color,False)

    turtle.done()

if __name__ == "__main__":
    main()