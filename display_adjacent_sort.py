import turtle



def swap (array, firstIndex, secondIndex):
	x = array[firstIndex] 
	array[firstIndex] = array[secondIndex]
	array[secondIndex] = x
	
def turtleDrawSwap (idx):
	wp = turtle.pos()
	turtle.setpos((idx)*40+15, turtle.ycor()+100)
	turtle.pendown()
	turtle.pensize(2)
	turtle.pencolor("red")
	turtle.circle(16)
	turtle.left(130)
	circleWP = turtle.pos()
	turtleDrawArrow ()
	turtle.penup()
	turtle.setpos(circleWP)
	turtle.forward(40)
	turtle.color("red")
	turtle.pendown()
	turtle.circle(16)
	turtleDrawArrow ()
	turtle.pensize(1)
	turtle.penup()
	turtle.setpos(wp)
	
def turtleDrawArrow ():
	turtle.pencolor("black")
	
	turtle.right(155)
	turtle.forward(50)
	tipWP = turtle.pos()
	turtle.left(30)
	turtle.back(10)
	turtle.setpos(tipWP)
	turtle.right(60)
	turtle.back(10)
	turtle.seth(0)


def checkSort (array):
	for idx, val in enumerate(array):
		if idx == len(array)-1:
			return True
		elif val > array[idx+1]:
			return False
		
def adjacentSort (array):
	turtleWriteLine(array)
	while checkSort(array) != True:
		for idx, val in enumerate(array):
			if idx == len(array)-1:
				break
			elif val > array[idx + 1]:
				swap(array, idx, idx+1)
				turtleWriteLine(array)
				turtleDrawSwap(idx)
						
def turtuleNextLine ():
	turtle.penup()
	turtle.setpos(0,turtle.ycor()-50)
	
def turtleWriteLine (array):
	for i in array:
		turtle.write(i, move=False, align="left", font=("Arial", 20, "normal"))
		turtle.penup()
		turtle.forward(40)
	turtuleNextLine ()
	
def turtleSeperator ():
	turtle.setpos(0,turtle.ycor()+50)
	turtle.pendown()
	turtle.forward(300) 
	turtle.penup()
	turtle.back(300)
	turtle.setpos(0,turtle.ycor()-50)

				

def drawFirst ():
	turtle.clear()
	turtle.reset()
	turtle.speed(100)
	array = [22, 11, 99, 88, 10]
	adjacentSort(array)

def drawSecond ():
	turtle.clear()
	turtle.reset()
	turtle.speed(100)
	array = [22, 24, 55, 84, 30]
	adjacentSort(array)

def drawThird ():
	turtle.clear()
	turtle.reset()
	turtle.speed(100)
	array = [12, 34, 99, 55, 20]
	adjacentSort(array)
	


turtle.ontimer(drawFirst, 0)

turtle.ontimer(drawSecond, 5500)

turtle.ontimer(drawThird, 8000)

turtle.mainloop()
