'''
class Background:
	def drawBackground:
		self.win = GraphWin('Window', 1000, 700)

		self.rect = Rectangle(P)
'''
from graphics import *
'''
class DrawGraphic:
	def drawBackGround():
		self.win = GraphWin('Window', 1000, 700)
		startX = 200; startY = 50
		finishX = 800; finishY = 650
		rect = Rectangle(Point(startX, startY), Point(finishX, finishY))
		rect.draw(self.win)
		for Y in range(startY, finishY, 12):
			line = Line(Point(startX, Y), Point(finishX, Y))
			line.draw(self.win)
		for X in range(startX, finishX, 12):
			line = Line(Point(X, startY), Point(X, finishY))
			line.draw(self.win)

	def drawNode(x, y):
		p = self.win.getMouse()
		cir = Circle(Point(x,y), 3)
'''


win = GraphWin('Window', 1000, 700)
startX = 200; startY = 50
finishX = 800; finishY = 650
rect = Rectangle(Point(startX, startY), Point(finishX, finishY))
rect.draw(win)
for Y in range(startY, finishY, 18):
	line = Line(Point(startX, Y), Point(finishX, Y))
	line.draw(win)
for X in range(startX, finishX, 18):
	line = Line(Point(X, startY), Point(X, finishY))
	line.draw(win)

entry1 = Entry(Point(win.getWidth()/2, 30), 10)
entry1.draw(win)
Text(Point(win.getWidth()/2, 10), 'Node: ').draw(win)
Text(Point(win.getWidth()/2+60, 40), 'Submit').draw(win)
win.getMouse()
node = int(entry1.getText())
win.getMouse()

nodes = list()

while node:
	node -= 1
	p = win.getMouse();
	adjX = p.x - startX; adjY = p.y - startY
	if adjX%18 >= 9: adjX = adjX - adjX%18 + 18
	else: adjX -= adjX%18
	if adjY%18 >= 9: adjY = adjY - adjY%18 + 18
	else: adjY -= adjY%18
	p.x = adjX+startX; p.y = adjY+startY
	nodes.append((adjX/18,adjY/18))
	cir = Circle(p,6)
	cir.draw(win)
	cir.setFill('blue')

print(nodes)
win.getMouse()











