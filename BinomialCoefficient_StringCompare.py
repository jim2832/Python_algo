# -*- coding: utf-8 -*-
"""
Algorithms

Dynamic Programming I
Binomial Coefficient & String Compare

@author: jychang
"""

def binomial_coefficient_r(n:int, k:int)->int:
    #Compute n choose k
    if n == k or k == 0:
        return 1
    return binomial_coefficient_r(n-1, k-1) + \
        binomial_coefficient_r(n-1, k)

def binomial_coefficient(n:int, k:int)->int:
    bc = [x[:] for x in [[1]*(n+1)]*(n+1)]  #Table of binomial coefficients
    # bc = [[1]*(n+1)]*(n+1)
    for i in range(2, n+1):
        for j in range(1, i):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j]
    return bc[n][k]
            
print(binomial_coefficient(6,3))

def string_compare_r(s:str, t:str, i:int, j:int)->int:
    opt = {}
    if i < 0:
        return j+1
    if j < 0:
        return i+1
    opt['MATCH'] = string_compare_r(s,t,i-1,j-1) + (0 if s[i] == t[j] else 1)
    opt['INSERT'] = string_compare_r(s,t,i,j-1) + 1
    opt['DELETE'] = string_compare_r(s,t,i-1,j) + 1
    return min(opt.values())

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
            if i == 0: #Row init
                m[0][j].cost = j
                if j > 0:
                    m[0][j].parent = 'INSERT'
        m[i][0].cost = i #Column init
        if i > 0:
            m[i][0].parent = 'DELETE'
            
def reconstruct_path(m:list, s:str, t:str, i:int, j:int):
    if m[i][j].parent == -1:
        return
    elif m[i][j].parent == 'MATCH':
        yield from reconstruct_path(m, s, t, i-1, j-1)
        yield ('M' if s[i-1] == t[j-1] else 'S')
    elif m[i][j].parent == 'INSERT':
        yield from reconstruct_path(m, s, t, i, j-1)
        yield 'I'
    elif m[i][j].parent == 'DELETE':
        yield from reconstruct_path(m, s, t, i-1, j)
        yield 'D'

s = 'shot'
t = 'sport'
# s = 'thou-shalt-not'
# t = 'you-should-not'
s = 'shall'
t = 'should'


m = [x[:] for x in [[None]*(len(t)+1)]*(len(s)+1)]
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
    return m[len(s)][len(t)].cost

import time
start=time.time()
print(string_compare_r(s,t,len(s)-1,len(t)-1))
print("running time =",time.time() - start)
# init_matrix(m)
# for row in m:
#     print(" ".join(map(str, row)))
start=time.time()
print(string_compare(s,t))
print("running time =",time.time() - start)
for row in m:
    print(" ".join(map(str, row)))
print(",".join(reconstruct_path(m, s, t, len(s), len(t))))