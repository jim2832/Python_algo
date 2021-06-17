# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:47:40 2021

Maximum Flow 

This code is contributed by Neelam Yadav and fixed by Jiing-Yao Chang
"""

# Python program for implementation
# of Ford Fulkerson algorithm
 
# This class represents a graph
# using adjacency matrix representation
class Graph:
 
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.Vertices = len(graph)
 
    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''
 
    def BFS(self, s, t, parent):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.Vertices)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        # Standard BFS Loop
        while queue:
 
            # Dequeue a vertex from queue and print it
            u = queue.pop(0)
 
            # Get all adjacent vertices of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    # If we find a connection to the sink node,
                    # then there is no point in BFS anymore
                    # We just have to set its parent and can return true
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True
                    queue.append(ind)
 
        # We didn't reach sink in BFS starting
        # from source, so return false
        return False
             
     
    # Returns tne maximum flow from s to t in the given graph
    def FordFulkerson(self, source, sink):
 
        # This array is filled by BFS and to store path
        parent = [None]*(self.Vertices)
 
        max_flow = 0 # There is no flow initially
 
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :
 
            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            path=[]
            while(s !=  source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                path.insert(0,s)
                s = parent[s]
            path.insert(0,s)
            print("->".join(str(i) for i in path),", path flow =",path_flow)
            # Add path flow to overall flow
            max_flow +=  path_flow
 
            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
 
        return max_flow
 
  
# Create a graph given in the above diagram
 
graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
 
# graph = [[ 0, 20, 10,  0],
#          [20,  0, 30, 10],
#          [10, 30,  0, 20],
#          [ 0, 10, 20,  0]]

g = Graph(graph)
 
source = 0
sink = 5

# source = 0
# sink = 3

print("The maximum possible flow is ", g.FordFulkerson(source, sink))