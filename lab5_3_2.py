import turtle
class Pole(object):
    def __init__(self, name="", xpos = 0, ypos = 0, thick = 10, length = 100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        turtle.penup()
        turtle.goto(self.pxpos - self.pthick / 2, self.pypos)
        turtle.pendown()
        turtle.forward(self.plength)
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.setheading(0)

    def pushdisk(self,disk):
        disk_x = self.pxpos
        disk_y = self.pypos
        turtle.penup()
        turtle.goto(disk_x - disk / 2, disk_y)
        turtle.setheading(0)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(disk)
            turtle.left(90)
            turtle.forward(20)
            turtle.left(90)
        turtle.end_fill()
        self.stack.append(disk)
    
    def popdish(self):
        if not self.stack:
            return None
        disk = self.stack.pop()
        return disk
