from math import *
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print (bob)

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, 360/n)

def circle(t, r):
    lenght = (2*pi*r)/360
    polygon(t, lenght, 360)

def arc(t, r, angle):
    length = 2 * pi * r * angle / 360
    n = int(length/10)+1
    step_length = length / n
    step_angle = angle / n
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

#square(bob, 150)
#polygon(bob, 10, 30)
#circle(bob, 100)
arc(bob, 100, 180)

wait_for_user()
