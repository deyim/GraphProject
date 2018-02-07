from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def printGraph(self):
		for u in self.graph:
			print(self.graph[u])

	def DFSrecur(self, v, visited):
		visited[v] = True
		print(v, ' ', end="")
		for u in self.graph[v]:
			if visited[u] != True:
				self.DFSrecur(u, visited)
	def DFScall(self,v):
		visited = [False]*(len(self.graph)+1)
		self.DFSrecur(v, visited)
		print()

'''
	def DFSutil(self, v, visited):
		visited[v] = True
		print(v,)
		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSutil(i, visited)

	def DFS(self,v):
		visited = [False]*(len(self.graph)+1)
		self.DFSutil(v,visited)	

	def BFS:
	'''