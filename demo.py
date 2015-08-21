import turtle
wd = turtle.Screen()
oT = turtle.Turtle()
oT.hideturtle()
def fireworks(pos, color, size, turtle):
	turtle.shapesize(0)
	turtle.goto(pos)
	turtle.color(color)
	for i in range(0, 36):
		turtle.speed(0)
		turtle.fd(size)
		turtle.lt(250)
def pyramid (level,size, turtle):
	while (level > 0):
		upperleftx = (-size/2*level)
		upperlefty = (size/2*level)
		bottomrightx =(size/2*level)
		bottomrighty =(-size/2*level)
		levelcolor = level%6
		if (levelcolor == 5):
			color = (1,0,1)
		elif (levelcolor == 4):
			color = (0,0,1)
		elif (levelcolor == 3):
			color = (0,1,0)
		elif (levelcolor == 1):
			color = (1,0.5,0)
		elif (levelcolor == 2):
			color = (1,1,0)
		else:
			color = (1,0,0)
		x = upperleftx
		y = upperlefty
		while(x < bottomrightx):
			fireworks((x,y), color, size, turtle)
			x = x+size
		while(y > bottomrighty):
			fireworks((x,y), color, size, turtle)
			y = y-size
		while(x > upperleftx):
			fireworks((x,y), color, size, turtle)
			x = x-size
		while(y < upperlefty):
			fireworks((x,y), color, size, turtle)
			y = y+size
		level = level -1
	fireworks((0,0), "red",size,turtle)
wd.tracer(0,0)
pyramid(20,50,oT)
wd.tracer(1,10)
wd.exitonclick()
