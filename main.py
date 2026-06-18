import turtle

screen = turtle.Screen()
screen.bgcolor("#A3F00A")
screen.setup(600, 600)
screen.title("Хрестики Нулики")

pen = turtle.Turtle()
pen.color("blue")
pen.pensize(4)
pen.speed(0)

cells = [
    None, None, None, 
    None, None, None, 
    None, None, None
]

def draw_square():
    for i in range(4):
        pen.forward(100)
        pen.right(90)

def draw_line():
    for i in range(3):
        draw_square()
        pen.forward(100)
        
def draw_field():
    y = 150
    for i in range(3):
        pen.penup()
        pen.goto(-150, y)
        pen.pendown()
        draw_line()
        y -= 100
        
draw_field()

def draw_cross(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("#FF0000")
    pen.goto(x +100, y -100)
    pen.penup()
    pen.goto(x +100, y)
    pen.pendown()
    pen.goto(x , y -100)
    
def draw_zero(x, y):
    pen.penup()
    pen.goto(x + 50,y - 100)
    pen.pendown()
    pen.color("#06167D")
    pen.circle(50)



win = None


def check_win(object):
    global win
    
    if cells[0] == object and cells[1] == object and cells[2] == object:
        win = True
    if cells[3] == object and cells[4] == object and cells[5] == object:
        win = True
    if cells[6] == object and cells[7] == object and cells[8] == object:
        win = True
    if cells[0] == object and cells[3] == object and cells[6] == object:
        win = True
    if cells[1] == object and cells[4] == object and cells[7] == object:
        win = True
    if cells[2] == object and cells[5] == object and cells[8] == object:
        win = True
    if cells[0] == object and cells[4] == object and cells[8] == object:
        win = True
    if cells[2] == object and cells[4] == object and cells[6] == object:
        win = True



    if win == True:
        pen.penup()
        pen.goto(0,200)
        pen.pendown()
        pen.write(f"{object} victory",font = (None,40),align="center" )




turn = ["cross"]    

def click(x, y):
    global win
    x_corner = None 
    y_corner = None 
    index = None
    if x >= -150 and x <= -50:
        x_corner = -150
        index = 0 
    if x >= -50 and x <= 50:
        index = 1
        x_corner = -50 
    if x >= 50 and x <= 150:
        index = 2 
        x_corner = 50

    if y <= 150 and y >= 50:
        y_corner = 150
    if y <= 50 and y >= -50:
        y_corner = 50
        index += 3
    if y <= -50 and y >= -150:
        y_corner = -50 
        index += 6
    
    if win != True:
        if x_corner != None and y_corner != None:
            if cells[index] == None:
                if turn[0] == "cross":
                    cells[index] = "cross"
                    draw_cross(x_corner, y_corner)
                    check_win("cross")
                    turn[0] = "zero"
                else:
                    cells[index] = "zero"
                    check_win("zero")
                    draw_zero(x_corner, y_corner)
                    turn[0] = "cross"
        
screen.onclick(click)
screen.mainloop()