import turtle
import math



back_ground_color = "lightgrey"
side_size = 50
start_pos_x = 0
start_pos_y = 0




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



def draw_filled_shape(start_angle, nr_of_sides,center_pos_x, center_pos_y, mid_side_to_center, fill_color:str, pen_color:str):
    turtle.penup()
    turtle.home()
    # head_angle=turtle.heading()
    # change_pos(center_pos_x, center_pos_y)
    turtle.penup()
    if fill_color is not None:
        fill_color = back_ground_color
        turtle.fillcolor(fill_color)
        turtle.begin_fill()

    turning_angle=360//nr_of_sides
    side_length=mid_side_to_center/(math.sin(math.radians(turning_angle)))
    print("side_length=",side_length)
    print("turning_angle=",turning_angle)
    print("mid_side_to_center=",mid_side_to_center)


    # Go to starting point in the shape.
    # length of the shape will be 2x the padding
    turtle.color(pen_color)
    turtle.left(start_angle)
    turtle.forward(side_length)
    if turning_angle < 90:
        turtle.left(turning_angle*2)
    else:
        turtle.left(turning_angle)
    # turtlehead is now in the right direction
    turtle.pendown()

    for side in range(nr_of_sides):
        turtle.forward(side_length)
        turtle.left(turning_angle)

    turtle.end_fill()
    turtle.hideturtle()
    turtle.penup()

def create_shapes(start_angle, nr_of_shapes, nr_of_sides, start_pos_x, start_pos_y,
                   padding, fill_color_list, pen_color_list,small_to_large):
    set_screen(back_ground_color, "Martin's Turtle Show", 1200, 800)
    change_pos(start_pos_x, start_pos_y)
    cur_shape =0
    if small_to_large:
        base_to_center=padding
    else:
        base_to_center=padding*nr_of_shapes
    center_pos_x = start_pos_x
    center_pos_y = start_pos_y

    while cur_shape < nr_of_shapes:
        if len(pen_color_list) <= cur_shape+1:
            pen_color_list.append("black")
        if len(fill_color_list) < cur_shape+1:
            fill_color_list.append(None)
        draw_filled_shape(start_angle, nr_of_sides, center_pos_x, center_pos_y, base_to_center,
                           fill_color_list[cur_shape], pen_color_list[cur_shape])
        if small_to_large:
            base_to_center += padding
        else:
            base_to_center -= padding
        cur_shape += 1


def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(2)
    screen = turtle.Screen()
    screen.setup(width=1000, height=600, startx=-2000, starty=-700)

    padding=15
    start_angle = 0
    nr_of_sides=6
    nr_of_shapes = 10

    pen_color = ["red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple"]
    #fill_color = ["red", "orange", "black", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue","orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple"]
    fill_color = [None, None, None, None, None, None, None]
    create_shapes(start_angle,nr_of_shapes,nr_of_sides, start_pos_x,start_pos_y,
                   padding, fill_color,pen_color,True)

    turtle.done()

if __name__ == "__main__":
    main()