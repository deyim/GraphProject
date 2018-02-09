from Graph import *


g = Graph()
f = open("graph_data.txt", 'r')

for line in f:
	u,v = line.split(',')
	g.addEdge(int(u), int(v))
f.close()

#g.printGraph()
#g.DFScall(2)
g.BFScall(1)
print(g.path)