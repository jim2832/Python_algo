# -*- coding: utf-8 -*-
"""
Algorithms

Dijkstra's Shortest Path Algorithm

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

def dijkstra(graph:list, start:GraphVertex)->list:
    spst = [] #spst -> shortest path 
    for i in range(len(graph)):
        spst.append(GraphVertex(i))
    v = start #start vertex
    v.distance = 0
    while not v.intree:
        v.intree = True
        for e in v.edges:
            if not e.destination.intree:
                if e.destination.distance > (e.weight + v.distance):
                    e.destination.distance = e.weight + v.distance
                    e.destination.candidate = e
                    e.destination.parent = v
        dist = float('inf')
        spst_edge = None
        for i in graph:
            if not i.intree and dist > i.distance:
                dist = i.distance
                spst_edge = i.candidate
        if spst_edge is not None: #put edge into mst graph
            s = spst_edge.source.label
            d = spst_edge.destination.label
            w = spst_edge.weight
            spst[s].edges.append(GraphEdge(spst[s],spst[d], w))
            spst[d].edges.append(GraphEdge(spst[d],spst[s], w)) #undirected graph
            v = spst_edge.destination
    return spst

edge_list = [[0,1,5],[0,2,7],[0,3,12],[1,4,7],[1,2,9],\
        [2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
graph = initial_graph(7, edge_list)
spst = dijkstra(graph, graph[0])
for v in spst:
    print(v)
    
import networkx as nx
# graph = nx.Graph()
# graph.add_nodes_from(range(6))
# for e in edge_list:
#     graph.add_edge(e[0],e[1],weight=e[2])
# pos=nx.planar_layout(graph)
# labels = nx.get_edge_attributes(graph,'weight')
# print('Original Graph')
# nx.draw_networkx(graph, pos, with_labels=True, font_weight='bold')
# nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)

graph_spst = nx.Graph()
graph_spst.add_nodes_from(range(6))
for v in spst:
    for e in v.edges:
        graph_spst.add_edge(e.source.label,e.destination.label,weight=e.weight)
pos=nx.planar_layout(graph_spst)
labels = nx.get_edge_attributes(graph_spst,'weight')
print('Shortest Path Spanning Tree')
nx.draw_networkx(graph_spst, pos, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(graph_spst,pos,edge_labels=labels)
