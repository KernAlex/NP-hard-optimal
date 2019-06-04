#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:47:36 2018

@author: alexkern
"""
import networkx as nx
import busGen as bg
import numpy as np
def is_neg_def(x):
    return np.all(np.linalg.eigvals(x) <= 0)
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) >= 0)


#Tiny Tester
############################################
#G = nx.Graph()
#for i in range(10,18):
#    G.add_node(i)
#G.add_edge(10, 12)
#G.add_edge(11, 13)
#G.add_edge(16, 14)
#G.add_edge(15, 17)
### v2
#G.add_edge(13, 12)
#G.add_edge(12, 15)
#G.add_edge(12, 14)
### v3
#G.add_edge(13, 14)
#G.add_edge(13, 15)
### v4
#G.add_edge(14, 15)
############################################
#SmallG
############################################
#G = nx.Graph()
#for i in range(1, 33):
#    G.add_node(i)
#for i in range(5, 11):
#    G.add_edge(1, i)
#    G.add_edge(2, i)
#    G.add_edge(i, i + 1)
#for j in range(11, 17):
#    G.add_edge(3, j)
#    G.add_edge(4, j)
#    G.add_edge(j, j + 1)
#for k in range(17, 23):
#    G.add_edge(29, k)
#    G.add_edge(30, k)
#    G.add_edge(k, k + 1)
#for l in range(23, 29):
#    G.add_edge(31, l)
#    G.add_edge(32, l)
#    G.add_edge(l, l + 1)
#G.add_edge(6, 24)
#G.add_edge(6, 26)
#G.add_edge(9, 25)
#G.add_edge(9, 27)
#G.add_edge(18, 12)
#G.add_edge(18, 14)
#G.add_edge(21, 15)
#G.add_edge(21, 13)
###########################################
#Middle G
###########################################
#G = nx.Graph()
#for i in range(1, 301):
#    G.add_node(i)
#for j in range(1, 101):
#    for k in range(1, 101):
#        if (j < k):
#            G.add_edge(j, k)
#for l in range(100, 201):
#    for m in range(100, 201):
#        if (l < m):
#            G.add_edge(l, m)
#for n in range(200, 281):
#    for q in range(200, 281):
#        if(n < q):
#            G.add_edge(n, q)
#for p in range(281, 292):
#    G.add_edge(280, p)
#    G.add_edge(300, p)
#    G.add_edge(p, p + 1)
#for v in range(292, 300):
#    G.add_edge(280, v)
############################################
#Large G
############################################
G = nx.Graph()
for i in range(1, 800):
    G.add_node(i)
for j in range(1,500):
    for k in range(1, 500):
        if j < k:
            G.add_edge(j, k)
for l in range(500, 800):
    G.add_edge(l, l + 1)
for m in range(500, 600):
    G.add_edge(m, m + 100)
    G.add_edge(m, m + 50)
    G.add_edge(m, m + 150)
    G.add_edge(m, m + 200)
G.add_edge(499, 500)
############################################
xx = bg.busOpt(G, 300, 10)
