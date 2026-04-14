import turtle
import math

back_ground_color = "lightgrey"
side_size = 50
start_pos_x = 0
start_pos_y = -100

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


def draw_filled_triangle(start_angle, length, direction, fill_color:str, pen_color:str):
    turtle.pendown()
    if fill_color != "None":
        fill_color = back_ground_color
        turtle.fillcolor(fill_color)
        turtle.begin_fill()

    turtle.color(pen_color)
    if direction == "left":
        turtle.left(start_angle)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
    else:
        turtle.right(start_angle)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(120)

    # turtle.forward(length)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()

def create_six_triangles(nr_of_triangles,start_pos_x, start_pos_y, side_length,fill_color_list, pen_color_list):
    set_screen(back_ground_color, "Martin's Turtle Show", 800, 400)
    change_pos(start_pos_x, start_pos_y)
    cur_triangle = 1
    starting_angle = 60
    angle_increase = -60
    while cur_triangle <= nr_of_triangles:
        if cur_triangle == 1:
            draw_filled_triangle(starting_angle, side_length, "right",
                                 fill_color_list[cur_triangle], pen_color_list[cur_triangle])
        else:
            draw_filled_triangle(angle_increase, side_length, "None", fill_color_list[cur_triangle],pen_color_list[cur_triangle])
        change_pos(start_pos_x, start_pos_y)
        # cur_angle+=angle_increase
        cur_triangle += 1

def main():
    side_size=100
    turtle.speed(6)
    side_height=math.sin(math.radians(60))*side_size
    pen_color = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
    fill_color = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

    print(side_height)
    nr_of_triangles_in_base_shape = 6
    positions=[(start_pos_x,start_pos_y),
               (start_pos_x - (1.5*side_size), start_pos_y+side_height),
               (start_pos_x - (1.5*side_size), start_pos_y+(3*side_height)),
               (start_pos_x, start_pos_y+(4*side_height)),
               (start_pos_x + (1.5*side_size),start_pos_y+(3*side_height)),
               (start_pos_x + (1.5 * side_size), start_pos_y+side_height)
              ]
    for position in positions:
        create_six_triangles(nr_of_triangles_in_base_shape,position[0],position[1],
                             side_size,fill_color,pen_color)

    turtle.done()

if __name__ == "__main__":
    main()