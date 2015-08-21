import turtle
ourScreen = turtle.Screen()
t = turtle.Turtle()
import math
def circle (r, cl, lt, p, t):
	t.goto(0, 0)
	t.color(cl)
	t.pensize(1)
	for i in range (0, 360):
		t.fd(2.0*math.sin(math.pi/360)*r)
		turtle.lt(1)
circle(5,"red",1,(100,100), t)


ourScreen.exitonclick()
