import turtle

back_ground_color = "lightgrey"
side_size = 50
start_pos_x = 0
start_pos_y = 0
t = turtle.Turtle()


def set_screen(bgcolor, title, x, y):
    screen = turtle.Screen()
    screen.setup(width=x, height=y, startx=-2000, starty=-700)
    screen.bgcolor(bgcolor)

def create_circle(radius:float, fill_color:str="black",pen_color:str="black",extend:float=None,steps:int=None):
    t.penup()
    t.pencolor(pen_color)
    t.pendown()
    t.color(fill_color)
    t.begin_fill()
    t.circle(radius,extend,steps)
    t.end_fill()

def create_triangle(side_length:float, fill_color:str="black",pen_color:str="black"):
    t.penup()
    t.pencolor(pen_color)
    t.pendown()
    if fill_color!="None":
        t.color(fill_color)
        t.begin_fill()

    for i in range(3):
        t.forward(side_length)
        t.left(120)
    if fill_color != "None":
        t.end_fill()


def main():
    t.hideturtle()
    t.penup()
    t.speed(0)
    screen = turtle.Screen()
    radius=30.5
    base=30
    padding=10
    start_angle = 0
    nr_of_sides=6
    nr_of_shapes = 10

    pen_color = ["red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple"]
    fill_color = ["red", "orange", "black", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue","orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple", "red", "orange", "yellow", "green", "blue", "purple"]
    #fill_color = [None, None, None, None, None, None, None]

    for flower_bush in range(8):
        for bunch_of_flowers in range(4):
            for flower in range(12):
                for diamont in range(2):
                    create_triangle(base, "None", "darkgrey")
                    # create_circle(radius, fill_color[0],pen_color[2],270,3)
                    t.penup()
                    t.forward(base)
                    t.pendown()
                    t.left(180)
                t.penup()
                t.forward(base+padding)
                t.pendown()
                t.left(30)
                print(".", end='')
            t.left(90)
            t.penup()
            t.forward(base*5)
            t.pendown()
        t.left(45)
        t.penup()
        t.backward((flower_bush + base) * 6)
        t.pendown()
    print("Done")

    turtle.done()

if __name__ == "__main__":
    main()