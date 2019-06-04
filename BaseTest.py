#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 14:14:58 2018

@author: alexkern
"""

import pydot

a = 13
b = 2

def f(n, b):
    v = [n]
    while v[-1] not in v[:-1]:
        v += [(v[-1] ** b) % a]
    return zip(v, v[1:])
def h(n, b):
    v1 = []
    v2 = []
    for i in range(a):
        v2 += [n**i % a]
        v1 += [n]
    return zip(v1,v2)
gdot = pydot.Dot(directed=True)
edges = {(x, y) for n in range(a) for x, y in f(n, b)}
for x, y in edges:
    gdot.add_edge(pydot.Edge(x, y))
gdot.write_png("tmp.png")