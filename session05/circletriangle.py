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

def circletriangle():
    jack.speed(10)
    r=120
    r2=r/2
    r3=r/2/math.sqrt(3)
    circle(jack,r)
    jack.penup()
    arc(jack,r,30)
    jack.pendown()
    jack.lt(90)
    jack.fd(r*2)
    jack.rt(120)
    jack.fd(r)
    jack.rt(120)
    jack.fd(r*2)
    jack.lt(120)
    jack.fd(r)

    #another 8 shape triangle
    jack.penup()
    jack.lt(30)
    arc(jack,r,90)
    jack.lt(90)
    jack.pendown()

    jack.fd(r*2)
    jack.rt(120)
    jack.fd(r)
    jack.rt(120)
    jack.fd(r*2)
    jack.lt(120)
    jack.fd(r)

    jack.bk(r2)
    #first circle
    circle(jack,r3)
    jack.penup()
    jack.goto(0,r+r/2*math.sqrt(3))
    jack.pendown()
    #second circle
    jack.rt(270)
    circle(jack,r3)
    jack.penup()
    #third circle
    jack.goto(-r/2*math.sqrt(3),r)
    jack.lt(90)
    jack.pendown()
    circle(jack,r3)
    #fourth circle
    jack.penup()
    jack.goto(0,(r-r/2*math.sqrt(3)))
    jack.lt(90)
    jack.pendown()
    circle(jack,r3)

circletriangle()

turtle.mainloop()