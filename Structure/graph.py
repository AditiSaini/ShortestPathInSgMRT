#This file defines the graph data structure used in the program
from collections import defaultdict

#Graph data structure
class Graph:
    def __init__(self):
        self.graph_dict = defaultdict(list)
        self.weights = {}
    def addEdge(self, u, v, weight):
        if v not in self.graph_dict[u]:
            self.graph_dict[u].append(v)
        if u not in self.graph_dict[v]:
            self.graph_dict[v].append(u)
        self.weights[(u, v)] = weight
        self.weights[(v, u)] = weight