# -*- coding: utf-8 -*-
"""
Algorithms

Floyd-Warshall's All Pairs Shortest Path Algorithm

@author: jychang
"""

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf') #The distance from start vertex
        self.intree = False #Is the vertex in the tree yet?
        self.candidate = None #Candidate mst edge
        self.parent = None #The vertex discovers me
        self.edges = []  #Edges in Adjacency List
    def __str__(self):
        output = f"{self.label}: "
        for e in self.edges:
            output += f"{self.label}-({e.weight})->{e.destination.label} "
        return output

class GraphEdge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def initial_graph(n:int, edge_list:list)->list:
    graph = []
    for i in range(n):
        graph.append(GraphVertex(i))
    for e in edge_list:
        if 0 <= e[0] < n and 0 <= e[1] < n:
            graph[e[0]].edges.append(GraphEdge(graph[e[0]], graph[e[1]], e[2]))
            graph[e[1]].edges.append(GraphEdge(graph[e[1]], graph[e[0]], e[2]))
    return graph

def to_adj_matrix(graph:list)->list:
    n = len(graph)
    M = [x[:] for x in [[float('inf')]*n]*n]
    for i in range(n):
        M[i][i] = 0
    for v in graph:
        i = v.label
        for e in v.edges:
            j = e.destination.label
            M[i][j] = e.weight
    return M

def floyd(M:list):
    n = len(M)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if M[i][k] != float('inf') and M[k][j] != float('inf'):
                    M[i][j] = min(M[i][j], M[i][k]+M[k][j])

import networkx as nx
def draw_graph(M:list):
    graph = nx.Graph()
    n = len(M)
    graph.add_nodes_from(range(n))
    for i in range(n):
        for j in range(n):
            if 0 < M[i][j] < float('inf'):
                graph.add_edge(i,j,weight=M[i][j])
    pos=nx.planar_layout(graph)
    labels = nx.get_edge_attributes(graph,'weight')
    nx.draw_networkx(graph, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
    
edge_list = [[0,1,5],[0,2,7],[0,3,12],[1,4,7],[1,2,9],\
        [2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
graph = initial_graph(7, edge_list)
adj_M = to_adj_matrix(graph)
draw_graph(adj_M)
floyd(adj_M)
print("\n".join([",".join("%02d "%x for x in row) for row in adj_M]))
