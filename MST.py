# -*- coding: utf-8 -*-
"""
Algorithms

Minimum Spanning Tree

@author: jychang
"""

class GraphVertex:
    def __init__(self, label):
        self.label = label
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
            e1 = GraphEdge(graph[e[0]], graph[e[1]], e[2])
            graph[e[0]].edges.append(e1)
            e2 = GraphEdge(graph[e[1]], graph[e[0]], e[2])
            graph[e[1]].edges.append(e2)
    return graph

def prim(graph:list)->list:
    mst = []
    for i in range(len(graph)):
        mst.append(GraphVertex(i))
    v = graph[0] #start
    while not v.intree:
        v.intree = True
        for e in v.edges:
            if not e.destination.intree:
                if e.destination.candidate is None or e.destination.candidate.weight > e.weight:
                    e.destination.candidate = e
                    e.destination.parent = v
        dist = float('inf')
        mst_edge = None
        for i in graph:
            if not i.intree and i.candidate is not None and dist > i.candidate.weight:
                dist = i.candidate.weight
                mst_edge = i.candidate
        if mst_edge is not None: #put edge into mst graph
            s = mst_edge.source.label
            d = mst_edge.destination.label
            w = mst_edge.weight
            mst[s].edges.append(GraphEdge(mst[s],mst[d], w))
            mst[d].edges.append(GraphEdge(mst[d],mst[s], w)) #undirected graph
            v = mst_edge.destination
    return mst

edge_list = [[0,1,5],[0,2,7],[0,3,12],[1,4,7],[1,2,9],\
        [2,3,4],[2,4,4],[2,5,3],[3,5,7],[4,5,2],[4,6,5],[5,6,2]]
mst = prim(initial_graph(7, edge_list))
for v in mst:
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

graph_mst = nx.Graph()
graph_mst.add_nodes_from(range(6))
for v in mst:
    for e in v.edges:
        graph_mst.add_edge(e.source.label,e.destination.label,weight=e.weight)
pos=nx.planar_layout(graph_mst)
labels = nx.get_edge_attributes(graph_mst,'weight')
print('Minimum Spanning Tree')
nx.draw_networkx(graph_mst, pos, with_labels=True, font_weight='bold')
nx.draw_networkx_edge_labels(graph_mst,pos,edge_labels=labels)
