#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:13:07 2018

@author: alexkern
"""

import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()

G = nx.grid_2d_graph(3, 3)

nx.draw(G, with_labels=True, font_weight='bold')
plt.subplot(122)

nx.draw_shell(G)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(6, 4)
G.add_edge(5, 7)
