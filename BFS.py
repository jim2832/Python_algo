# -*- coding: utf-8 -*-
"""
Algorithms

Breadth First Search

@author: jychang
"""

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.d = -1 #Distance to start vertex
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

def BFS(start:GraphVertex):
    queue = []
    start.d = 0
    queue.append(start)
    while queue:
        curr = queue.pop(0)
        #process_vertex_early(curr.label)
        for v in curr.edges:
            #process_edge(curr.label, v.label)
            if v.d == -1: #Unvisited vertex
                v.d = curr.d + 1
                v.parent = curr
                queue.append(v)
        #process_vertex_late(curr.label)

def process_vertex_early(label:int):
    print("Processing vertex",label)

def process_edge(i:int, j:int):
    print(f"Processing edge ({i}, {j})")

def process_vertex_late(label:int):
    print(f"Vertex {label} processed")

def find_path(start:GraphVertex, end:GraphVertex):
    if start == end or end is None:
        print(start.label, end=' ')
    else:
        find_path(start, end.parent)
        print(end.label, end=' ')

def connected_components(graph:list):
    c = 0
    for v in graph:
        if v.d == -1: #unvisited
            c += 1
            print(f"Component {c}:")
            BFS(v)

edge_list=[[1,2],[2,1],[1,5],[5,1],[1,6],[6,1],[2,3],[3,2],[2,5],[5,2],[3,4],[4,3],[4,5],[5,4]]
graph = initial_graph(7,edge_list)
BFS(graph[1])
for v in graph:
    print(v)

# for v in graph:
#     if v.d != -1:
#         print('1->',v.label,end=': ')
#         find_path(graph[1], v)
#         print()

# connected_components(graph)