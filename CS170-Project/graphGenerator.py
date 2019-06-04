import os
import sys
import networkx as nx
import matplotlib.pyplot as plt
smallG = nx.Graph()
for i in range(1, 33):
    smallG.add_node(i)
for i in range(5, 11):
    smallG.add_edge(1, i)
    smallG.add_edge(2, i)
    smallG.add_edge(i, i + 1)
for j in range(11, 17):
    smallG.add_edge(3, j)
    smallG.add_edge(4, j)
    smallG.add_edge(j, j + 1)
for k in range(17, 23):
    smallG.add_edge(29, k)
    smallG.add_edge(30, k)
    smallG.add_edge(k, k + 1)
for l in range(23, 29):
    smallG.add_edge(31, l)
    smallG.add_edge(32, l)
    smallG.add_edge(l, l + 1)
smallG.add_edge(6, 24)
smallG.add_edge(6, 26)
smallG.add_edge(9, 25)
smallG.add_edge(9, 27)
smallG.add_edge(18, 12)
smallG.add_edge(18, 14)
smallG.add_edge(21, 15)
smallG.add_edge(21, 13)
#plt.subplot(121)
#nx.draw(smallG, with_labels=True, font_weight ='bold')
#plt.subplot(122)
#nx.draw_shell(smallG)
#print(smallG.nodes)
#print(smallG.edges)
nx.write_gml(smallG, "inputs/small/graph.gml")
middleG = nx.Graph()
for i in range(1, 301):
    middleG.add_node(i)
for j in range(1, 101):
    for k in range(1, 101):
        if (j < k):
            middleG.add_edge(j, k)
for l in range(100, 201):
    for m in range(100, 201):
        if (l < m):
            middleG.add_edge(l, m)
for n in range(200, 281):
    for q in range(200, 281):
        if(n < q):
            middleG.add_edge(n, q)
for p in range(281, 292):
    middleG.add_edge(280, p)
    middleG.add_edge(300, p)
    middleG.add_edge(p, p + 1)
for v in range(292, 300):
    middleG.add_edge(280, v)
nx.write_gml(middleG, "inputs/medium/graph.gml")
largeG = nx.Graph()
for i in range(1, 800):
    largeG.add_node(i)
for j in range(1,500):
    for k in range(1, 500):
        if j < k:
            largeG.add_edge(j, k)
for l in range(500, 800):
    largeG.add_edge(l, l + 1)
for m in range(500, 600):
    largeG.add_edge(m, m + 100)
    largeG.add_edge(m, m + 50)
    largeG.add_edge(m, m + 150)
    largeG.add_edge(m, m + 200)
nx.write_gml(largeG, "inputs/large/graph.gml")
text_file = open("inputs/large/parameters.txt", "w")
text_file.write("780\n")
text_file.write("500\n")
for n in range(1, 100):
    text_file.write("["+str(n*7 + 200)+","+str(n*5)+","+str(n*7 + 2)+","+str(n*8 + 4)+","+str(900 - n*5)+","+str(n + 127)+","+str(n + 232)+","+str(1000 - n*7) + "]\n")
for q in range(3, 80):
    for p in range(1, 20):
        text_file.write("[" + str(q * 5  + p * 26) + "," + str(q * 7 + p * 10) + "," + str(p * 37 + q) + "]\n")
text_file.close()
text_file = open("outputs/medium.out", "w")
for i in range(0, 14):
    text_file.write("[")
    for j in range(1, 20):
        text_file.write(str(20*i + j) + ",")
    text_file.write(str(20*(i+1)) + "]\n")
text_file.write("[281,282,283,284,285,286,287,288,289,290,291]\n")
text_file.write("[280,292,293,294,295]\n")
text_file.write("[296]\n")
text_file.write("[297]\n")
text_file.write("[298]\n")
text_file.write("[299]")
text_file.close()
text_file = open("outputs/large.out", "w")
for i in range(1, 21):
    text_file.write("[" + str(i) + "," + str(i + 20) + "]\n")
for j in range(21, 781):
    text_file.write("[" + str(j) + "]\n")
text_file.close()
