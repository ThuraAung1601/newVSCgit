import turtle

# Disk class (from lab5_3_1)
class Disk(object):
    def __init__(self, name="", xpos=0, ypos=0, height=20, width=40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def show_disk(self, pencolor="black"):
        # Setup turtle to draw the disk (rectangular object)
        turtle.penup()
        turtle.color(pencolor)
        turtle.goto(self.dxpos - self.dwidth / 2, self.dypos)  # Start position (centered)
        turtle.setheading(0)  # Make sure the turtle is facing right
        turtle.pendown()
        
        # Draw the rectangle representing the disk
        for _ in range(2):
            turtle.forward(self.dwidth)
            turtle.left(90)
            turtle.forward(self.dheight)
            turtle.left(90)
        turtle.penup()

    def newpos(self, xpos, ypos):
        # Move disk to a new position
        self.dxpos = xpos
        self.dypos = ypos
        self.show_disk()

    def cleardisk(self):
        # Clear the disk (draw it in the background color)
        self.show_disk("white")


# Pole class (from lab5_3_2)
class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []  # This will store the disks
        self.toppos = ypos  # Initial position of the top of the pole
        self.pxpos = xpos  # Horizontal position of the pole
        self.pypos = ypos  # Vertical position of the pole
        self.pthick = thick  # Thickness of the pole
        self.plength = length  # Height of the pole

    def showpole(self):
        # Draw the pole using Turtle
        turtle.penup()
        turtle.left(90)
        turtle.goto(self.pxpos - self.pthick / 2, self.pypos)  # Start at the base
        turtle.pendown()
        turtle.forward(self.plength)  # Draw the pole
        turtle.penup() 
        turtle.goto(self.pxpos, self.pypos)  # Return to the base position
        turtle.setheading(0)  # Reset the turtle's heading

    def pushdisk(self, disk):
        # Position the disk above the pole
        if self.stack:
            # If there's already a disk, stack the new one above the last
            disk_y = self.pypos + (len(self.stack) * disk.dheight)
        else:
            # If no disk, place the first disk at the base of the pole
            disk_y = self.pypos
        
        # Update the disk position
        disk.newpos(self.pxpos, disk_y)
        
        # Draw the disk using its own method (show_disk)
        disk.show_disk()
        
        # Add the disk to the stack
        self.stack.append(disk)

    def popdisk(self):
        if not self.stack:
            return None
        disk = self.stack.pop()
        disk.cleardisk()  # Clear the disk from the screen
        # Move the remaining disks down
        if self.stack:
            for i in range(len(self.stack)):
                self.stack[i].newpos(self.pxpos, self.pypos + i * self.stack[i].dheight)
        return disk

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startp = Pole(start, 0, -100)
        self.workspacep = Pole(workspace, 150, -100)
        self.destinationp = Pole(destination, 300, -100)
        
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        
        for i in range(n):
            self.startp.pushdisk(Disk("d" + str(i), 0, -100 + (i * 30), 20, (n - i) * 30))
        
        self.n = n 

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self, n, s, d, w):
        if n == 1:
            self.move_disk(s, d)
        else:
            self.move_tower(n - 1, s, w, d)
            self.move_disk(s, d)
            self.move_tower(n - 1, w, d, s)

    def solve(self):
        self.move_tower(self.n, self.startp, self.destinationp, self.workspacep)

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Towers of Hanoi")

h = Hanoi(n=3)
h.solve()

screen.exitonclick()