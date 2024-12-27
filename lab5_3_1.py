import turtle
class Disk(object):
    def __init__(self, name = "", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    
    def show_disk(self, pencolor="black"):
        # Your code
        turtle.penup()
        turtle.color(pencolor)
        turtle.goto(self.dxpos - self.dwidth/2, self.dypos)
        turtle.pendown()
    
        for _ in range(2):
            turtle.forward(self.dwidth/2)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
            turtle.forward(self.dwidth/2)
    
    def newpos(self, xpos, ypos):
        # Your code
        self.cleardisk()
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        # Your code 
        self.show_disk("white")

screen = turtle.Screen()
disk1 = Disk()
disk1.show_disk()
disk1.newpos(100, 100)
disk1.show_disk()
disk1.cleardisk()

screen.exitonclick()