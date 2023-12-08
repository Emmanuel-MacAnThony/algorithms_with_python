from typing import Dict
from collections import deque

class Vertex(object):
    
    def __init__(self, key) -> None:
        self.connectedTo = {}
        self.id = key
        
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
        
    def getConnections(self):
        return self.connectedTo.keys()
    
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def __str__(self) -> str:
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])
    
    
class Graph:
    
    def __init__(self) -> None:
        self.vertList: Dict[str, Vertex] = {}
        self.numVertices = 0
        
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
        
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
            
        if t not in self.vertList:
            nv = self.addVertex(t)
            
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        
    
    def getVertices(self):
        return self.vertList.keys()
    
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    
    def __contains__(self, n):
        return n in self.vertList
    
    
# depth first traversal
def dfs_traverse(vertex: Vertex, visited_vertices={}):
    
    visited_vertices[vertex.getId()] = True
    
    print(vertex.getId())
    
    #iterate through the current vertex adjacent vertices
    for adjacent_vertex in vertex.connectedTo:
        
        if adjacent_vertex.getId() in visited_vertices:
            continue
        
        # recursively call this method on the adjacent vertice
        dfs_traverse(adjacent_vertex, visited_vertices)
        

# breadth first search
def bfs_traverse(starting_vertex: Vertex):
    
    visited_vertices = {}
    visited_vertices[starting_vertex.getId()] = True
    queue = deque([starting_vertex])
    
    while queue:
        
        current_vertex = queue.popleft()
        
        for adjacent_vertex in current_vertex.connectedTo:
            if adjacent_vertex.getId() not in visited_vertices:
                visited_vertices[adjacent_vertex.getId()] = True
                queue.extend([adjacent_vertex])
    
    
    
    
    
        
            
        
            
            