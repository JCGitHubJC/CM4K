import turtle
ourScreen = turtle.Screen()
t = turtle.Turtle()
ourScreen.bgcolor("yellow")

def firework(pos, color, size, turtle):
	t.speed(0)
	t.goto(pos)
	t.color(color)
	for i in range(0, 36):
		t.fd(size)
		t.lt(250)
firework((0, 0), "blue", 250, t)
firework((100, 50), "black", 200, t)


ourScreen.exitonclick()

