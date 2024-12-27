import turtle

class Disk(object):
    def __init__(self, name = "", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
    
    def show_disk(self, pencolor="black"):
        # Setup turtle to draw the disk (rectangular object)
        turtle.penup()
        turtle.color(pencolor)
        turtle.goto(self.dxpos - self.dwidth/2, self.dypos)  # Start position (centered)
        turtle.setheading(0)  # Make sure the turtle is facing right
        turtle.pendown()
        
        # Draw the rectangle representing the disk
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
    
    def newpos(self, xpos, ypos):
        # Move disk to a new position
        # self.cleardisk()  # Clear the previous disk
        self.dxpos = xpos
        self.dypos = ypos
        self.show_disk()  # Redraw the disk at the new position

    def cleardisk(self):
        self.show_disk("white")  # This assumes the background is white
