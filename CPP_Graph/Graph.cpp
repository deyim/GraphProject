#include <iostream>
#include <list>
using namespace std;

class Graph
{
	int V; // number of  vertices
	list<int> *adj;
	void DFSrecur(int v, bool visited[]);
public:
	Graph(int V); //Constructor
	void addEdge(int v, int w);
	void DFScall(int v);
}

Graph :: Graph(int V)
{
	this->V = V;
	adj = new list<int>[V];
}

void Graph::addEdge(int v, int w)
{
	adj[v].push_back(w);
}

void Graph::DFSrecur(int v, bool visited[])
{
	visited[v] = true;
	cout << v << ' ';
	list<int>::iterator i;
	for(i = adj[v].begin() ; i != adj[v].end() ; ++i){
		if(visited[v] != true)
			DFSrecur(*i, visited);
	}
}

void Graph::DFScall(int V)
{
	bool *visited = new bool[V];
	for(int i = 0 ; i < V ; i++)
		visited[i] = false;
	DFSrecur(V, visited);
}