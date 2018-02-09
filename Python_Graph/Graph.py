from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

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

	def BFScall(self, v):
		visited = [False]*(len(self.graph)+1)
		self.path = []
		q = []; q.append(v); visited[v] = True

		while q:
			v = q.pop(0)
			self.path.append(v)
			for adj in self.graph[v]:
				if visited[adj] == False:
					visited[adj] = True
					q.append(adj)
					



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