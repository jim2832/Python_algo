# -*- coding: utf-8 -*-
"""
Algorithms

Dynamic Programming II
Customizing Edit Distance
Substring Matching

@author: jychang
"""

class Cell:
    def __init__(self):
        self.cost = 0 #Cost of reaching this cell
        self.parent = -1 #Parent opt
    def __str__(self):
        return f"{self.cost}[{str(self.parent)[0]}]"

def init_matrix(m:list):
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j] = Cell()
            # if i == 0: #Row init
            #     m[0][j].cost = j
            #     if j > 0:
            #         m[0][j].parent = 'INSERT'
        m[i][0].cost = i #Column init
        if i > 0:
            m[i][0].parent = 'DELETE'
            
def reconstruct_path(m:list, s:str, t:str, i:int, j:int):
    if m[i][j].parent == -1:
        return
    elif m[i][j].parent == 'MATCH':
        yield from reconstruct_path(m, s, t, i-1, j-1)
        yield match_out(s[i-1],t[j-1])
    elif m[i][j].parent == 'INSERT':
        yield from reconstruct_path(m, s, t, i, j-1)
        yield insert_out(s[i],t[j-1])
    elif m[i][j].parent == 'DELETE':
        yield from reconstruct_path(m, s, t, i-1, j)
        yield delete_out(s[i-1],t[j])

def match_out(c:str, d:str)->str:
    return ('M' if c == d else 'S')

def insert_out(c:str, d:str)->str:
    return 'I'

def delete_out(c:str, d:str)->str:
    return 'D'

def string_compare(s:str, t:str)->int:
    opt = {}
    init_matrix(m)
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            opt['MATCH'] = m[i-1][j-1].cost + (0 if s[i-1] == t[j-1] else 1)
            opt['INSERT'] = m[i][j-1].cost + 1
            opt['DELETE'] = m[i-1][j].cost + 1
            m[i][j].cost = min(opt.values())
            m[i][j].parent = min(opt, key=opt.get)
    #return m[len(s)][len(t)].cost
    goal = goal_cell(m,s,t)
    print(goal)
    return m[goal[0]][goal[1]].cost


def goal_cell(m:list, s:str ,t:str)->list:
    goal = [len(s), 0]
    for k in range(1, len(t)+1):
        if m[goal[0]][k].cost < m[goal[0]][goal[1]].cost:
            goal[1] = k
    return goal

s = 'shot'
# s = 'sport'
t = 'The movie opens with a dreamy shot of a sunset'
# t = 'He is just starting shooting his new movie'
# t = 'This short is perfect for all sorts of sport'

m = [x[:] for x in [[None]*(len(t)+1)]*(len(s)+1)]

import time
start=time.time()
print(string_compare(s,t))
print("running time =",time.time() - start)
# for row in m:
#     print(" ".join(map(str, row)))
# print(",".join(reconstruct_path(m, s, t, len(s), len(t))))
