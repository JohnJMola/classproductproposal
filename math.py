from math import *
import turtle

print('''Help & intructions:
      1. to place origin in the center of the screen, type in "400, 300"
      2. to multiply to integers, use one "*", and to use an exponent, use "**"
      3. to adjust how many steps on a graph, type in a regular integer. Example: 50
      4. to close out, type in anything, except number.
      ''')

WIDTH,HEIGHT=800,600
WIDTH_HALF,HEIGHT_HALF=WIDTH/2, HEIGHT/2
TICK_LENGTH=10
TICK_LENGTH_HALF=TICK_LENGTH/2
AXISCOLOR="black"
COLORS=["red","green","blue"]

def screen_coords(xo,yo,ratio,x,y):
    return(xo+(ratio*x),yo+(ratio*y))

def get_color(counter):
    color_index=counter%len(COLORS)
    return COLORS[color_index]

def draw_x_axis_label_tick(pointer,screenX,screenY,text):
    pointer.penup()
    pointer.setpos(screenX,screenY-TICK_LENGTH_HALF)
    pointer.pendown()
    pointer.goto(screenX,(screenY-TICK_LENGTH_HALF)+TICK_LENGTH)
    pointer.penup()
    pointer.setpos(screenX,screenY-TICK_LENGTH-8)
    pointer.write(text,False,align="center")
    pointer.penup()
    return

def draw_y_axis_label_tick(pointer,screenX,screenY,text):
    pointer.penup()
    pointer.setpos(screenX-TICK_LENGTH_HALF,screenY)
    pointer.pendown()
    pointer.goto((screenX-TICK_LENGTH_HALF)+TICK_LENGTH,screenY)
    pointer.penup()
    pointer.setpos(screenX-TICK_LENGTH-2,screenY-4)
    pointer.write(text, False, align="center")
    pointer.penup()
    return

def draw_x_axis(pointer, xo, yo, ratio):
    pointer.penup()
    pointer.home()
    positiveX=WIDTH-xo
    negativeX=WIDTH-positiveX
    pointer.sety(yo)
    pointer.pendown()
    pointer.setx(WIDTH)
    pointer.penup()
    totalPositiveXTicks=floor(positiveX/ratio)
    totalNegativeXTicks=floor(negativeX/ratio)
    xmin,xmax=-totalNegativeXTicks,totalPositiveXTicks
    for i in range(totalNegativeXTicks):
        currentTick=i+1
        draw_x_axis_label_tick(pointer, negativeX-(ratio*currentTick),yo,f"-{currentTick}")
    for i in range(totalPositiveXTicks):
        currentTick=i+1
        draw_x_axis_label_tick(pointer,negativeX+(ratio*currentTick),yo,f"{currentTick}")
    pointer.home()
    return xmin, xmax

def draw_y_axis(pointer, xo, yo, ratio):
    pointer.penup()
    pointer.home()
    positiveY=HEIGHT-yo
    negativeY=HEIGHT-positiveY
    pointer.setx(xo)
    pointer.pendown()
    pointer.sety(HEIGHT)
    pointer.penup()
    totalPositiveYTicks=floor(positiveY/ratio)
    totalNegativeYTicks=floor(negativeY/ratio)
    for i in range(0,totalNegativeYTicks):
        currentTick=i+1
        draw_y_axis_label_tick(pointer,xo,negativeY-(ratio*currentTick),f"-{currentTick}")
    for i in range(0, totalPositiveYTicks):
        currentTick=i+1
        draw_y_axis_label_tick(pointer,xo,negativeY+(ratio*currentTick),f"{currentTick}")
    pointer.home()
    return

def draw_expr(pointer,xo,yo,ratio,xmin,xmax,expr):
    pointer.penup()
    pointer.setpos(xo,yo)
    for x in range(xmin*10,xmax*10+1):
        x=x/10
        y=eval(expr)
        coordX,coordY=screen_coords(xo,yo,ratio,x,y)
        if x==xmin:
            pointer.setpos(coordX,coordY)
        else:
            pointer.pendown()
            pointer.goto(coordX,coordY)
            pointer.penup()
    return

def handle_quit():
    turtle.bye()
    print("\nWindow closed, exiting...")
    exit(0)

def setup():
    pointer=turtle.Turtle()
    screen=turtle.getscreen()
    screen.title("Graphing Calculator")
    screen.setup(WIDTH,HEIGHT,0,0)
    screen.setworldcoordinates(0,0,WIDTH,HEIGHT)
    screen.bgcolor("white")
    screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW",handle_quit)
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer

def main():
    pointer=setup()
    try:
        xo,yo=eval(input("Enter pixel coordinates of origin: "))
        ratio=int(input("Enter ratio of pixels per step: "))
    except KeyboardInterrupt:
        print("\nUser interrupted, exiting...")
        exit(0)
    pointer.color(AXISCOLOR)
    xmin,xmax=draw_x_axis(pointer,xo,yo,ratio)
    draw_y_axis(pointer,xo,yo,ratio)
    try:
        expr=input("Enter an arithmetic expression: ")
        counter=0
        while expr!="":
            pointer.color(get_color(counter))
            draw_expr(pointer,xo,yo,ratio,xmin,xmax,expr)
            expr=input("Enterand arithmetic expression: ")
            counter+=1
        print("\nUser entered empty string, exiting...")
    except KeyboardInterrupt:
        print("\nUser interrupted, exiting...")
        exit(0)

main()