import turtle 
Screen = turtle.Screen()
t = turtle.Turtle()

t.shapesize(0)

def tree(w, t):
	t.color("brown")
	t.fill(True)
	t.fd(w) # width
	t.rt(90)
	t.fd(w*5) # height
	t.rt(90)
	t.fd(w) #width
	t.rt(90)
	t.fd(w*5) #height
	t.rt(90)
	t.fill(False)
	t.fd(w/2)
	t.rt(90)
	t.fd(w/10)
	t.color("orange")
	t.lt(90)
	t.fill(True)
	for i in range (0, 360):
		t.fd(w*2/100)
		t.lt(1)
	t.fill(False)

tree(50, t)

Screen.exitonclick()
