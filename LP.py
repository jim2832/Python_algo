# -*- coding: utf-8 -*-
"""
Algorithms

Dynamic Programming II
Linear Partition

@author: jychang
"""

def partition(s:list, n:int, k:int):
    m = [x[:] for x in [[0]*(k+1)]*(n+1)]
    d = [x[:] for x in [[0]*(k+1)]*(n+1)]
    p = [0]*(n+1)
    for i in range(1,n+1):
        p[i] = p[i-1]+s[i]
        m[i][1] = p[i]
    for j in range(1,k+1):
        m[1][j] = s[1]
    
    for i in range(2,n+1):
        for j in range(2,k+1):
            m[i][j] = float('inf')
            for x in range(1, i):
                cost = max(m[x][j-1], p[i]-p[x])
                if m[i][j] > cost:
                    m[i][j] = cost
                    d[i][j] = x
    construct_partition(s,d,n,k)

def construct_partition(s:list, d:list, n:int, k:int):
    if k > 0:
        construct_partition(s,d,d[n][k],k-1)
        print(" ".join(map(str,s[d[n][k]+1:n+1])))

# s=[0,1,1,1,1,1,1,1,1,1]
s=[0,1,2,3,4,5,6,7,8,9]
import time
start=time.time()
partition(s,9,3)
print("running time =",time.time() - start)
