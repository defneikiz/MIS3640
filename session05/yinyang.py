import turtle
import math


def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)


jack= turtle.Turtle()
jack.speed(0)
r=100
r2=r/2
r6=r/6
jack.pen(pencolor="black", pensize= "3")
arc(jack,r2,angle=180)
arc(jack,r,angle=180)
jack.penup()
arc(jack,r2,angle=180)
jack.pendown()
arc(jack,r2,angle=180)

arc(jack,r,angle=180)
jack.penup()
jack.fd(r6)
jack.lt(90)
jack.forward(r2)
jack.pendown()

circle(jack,r6)

jack.penup()
jack.fd(r)
jack.pendown()

circle(jack,r6)


turtle.mainloop()