# -*- coding: utf-8 -*-
"""
Algorithms

Depth First Search

@author: jychang
"""

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.d = 0 #Distance to start vertex
        self.discovered = False
        self.processed = False
        self.parent = None #The vertex discovers me
        self.edges = []  #Edges in Adjacency List
    def __str__(self):
        output = f"{self.label}(d={self.d}): "
        for e in self.edges:
            output += f"{self.label}->{e.label} "
        return output

def initial_graph(n:int, edge_list:list)->list:
    graph = []
    for i in range(n):
        graph.append(GraphVertex(i))
    for e in edge_list:
        if  0 <= e[0] < n and 0 <= e[1] < n:
            graph[e[0]].edges.append(graph[e[1]])
    return graph


def DFS(v:GraphVertex):
    v.discovered = True
    #process_vertex_early(v)
    for t in v.edges:
        if not t.discovered:
            t.parent = v
            t.d = v.d + 1
            #process_edge(v, t)
            DFS(t)
        elif v.parent != t:
            process_edge(v, t)
    #process_vertex_late(v)
    v.processed = True

def process_vertex_early(v:GraphVertex):
    print("Processing vertex",v.label)

def process_edge(i:GraphVertex, j:GraphVertex):
    print(f"Processing edge ({i.label}, {j.label}) {edge_classification(i,j)}")

def process_vertex_late(v:GraphVertex):
    print(f"Vertex {v.label} processed")

from enum import Enum
class EdgeType(Enum):
    TREE = 0
    BACK = 1
    FORWARD = 2
    CROSS = 3

def edge_classification(x:GraphVertex, y:GraphVertex)->EdgeType:
    if y.parent is x:
        return EdgeType.TREE
    elif y.discovered and not y.processed:
        return EdgeType.BACK if x.d > y.d else EdgeType.CROSS
    elif y.processed:
        return EdgeType.FORWARD if x.d < y.d else EdgeType.CROSS
    print(f"Warning: unclassified edge ({x.label},{y.label})")
    return None

def find_path(start:GraphVertex, end:GraphVertex):
    if start == end or end is None:
        print(start.label, end=' ')
    else:
        find_path(start, end.parent)
        print(end.label, end=' ')

# def process_edge(i:GraphVertex, j:GraphVertex):
#     if j.parent != i: #find back edge in DFS on undirected graph
#         find_path(j, i)
#         raise Exception(f" Cycle from {i.label} to {j.label}")

# order = []
# def process_vertex_late(v:GraphVertex):
#     order.insert(0, v.label)

# def process_edge(i:GraphVertex, j:GraphVertex):
#     if edge_classification(i, j) == EdgeType.BACK:
#         print(f"Cycle found from {i.label} to {j.label}")


edge_list=[[1,2],[2,1],[1,5],[5,1],[1,6],[6,1],[2,3],[3,2],[2,5],[5,2],[3,4],[4,3],[4,5],[5,4]]
graph = initial_graph(7,edge_list)
DFS(graph[1])
# for v in graph:
#     print(v)

for v in graph:
    if v.d != -1:
        print('1->',v.label,end=': ')
        find_path(graph[1], v)
        print()

import networkx as nx
graph = nx.Graph()
# graph = nx.DiGraph(directed=True)
graph.add_nodes_from(range(1,7))
graph.add_edges_from(edge_list)
nx.draw_networkx(graph, arrows=True, arrowstyle='-|>', arrowsize=12, with_labels=True, font_weight='bold')

def topsort(graph:list)->list:
    zeroin = [] # queue for vertices with in-degree 0
    sorted = []
    indeg = [0 for v in graph] # in-degrees of all vertices
    for v in graph: # compute in-degrees
        for e in v.edges:
            indeg[e.label] += 1
    for idx,i in enumerate(indeg):
        if i == 0:
            zeroin.append(graph[i])
    j = 0
    while zeroin:
        j += 1
        x = zeroin.pop(0)
        sorted.append(x.label)
        for e in x.edges:
            indeg[e.label] -= 1
            if indeg[e.label] == 0:
                zeroin.append(e)
    if j != len(graph):
        print(f"Not a DAG -- only {j} vertices found.")
    return sorted

edge_list=[[0,1],[0,6],[1,2],[1,3],[2,3],[2,4],[3,5],[3,6],[5,4],[6,5]]
graph = initial_graph(7,edge_list)
print(topsort(graph))