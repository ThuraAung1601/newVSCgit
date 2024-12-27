import turtle
from lab5_3_1 import Disk  # Assuming this is where the Disk class is located.

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
        turtle.goto(self.pxpos, self.pypos)  # Return tothe base position
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

    def popdish(self):
        if not self.stack:
            return None
        disk = self.stack.pop()
        disk.cleardisk()
        return disk

screen = turtle.Screen()

pole1 = Pole(name="Pole 1", xpos=0, ypos=-100, thick=10, length=200)
pole1.showpole()

disk1 = Disk(name="Disk 1", xpos=0, ypos=-100, height=20, width=40)
disk2 = Disk(name="Disk 2", xpos=0, ypos=-100, height=20, width=60)
disk3 = Disk(name="Disk 3", xpos=0, ypos=-100, height=20, width=80)

pole1.pushdisk(disk1)
pole1.pushdisk(disk2)
pole1.pushdisk(disk3)

pole1.popdish()

screen.exitonclick()
