import networkx as nx
from random import random
g5000 = nx.generators.barabasi_albert_graph(5000, 2)
temp = g5000.nodes()
pos = []
for node in range(5000):
    pos.append([round(random(), 4), round(random(), 4)])
for num in [2500, 3000, 3500, 4000, 4500, 5000]:
    points = temp[0:num]
    g = nx.subgraph(g5000, points)
    outfile = open('ba'+str(num)+'.txt', 'w')
    outfile.write(str(nx.diameter(g))+'\n')
    for i in g.edges(): outfile.write(str(i[0])+' '+str(i[1])+'\n')
    outfile.close()
    outfile = open('ba'+str(num)+'pos.txt', 'w')
    for i in range(num):
        outfile.write(str(pos[i][0]) + ' ' + str(pos[i][1]) + '\n')
    outfile.close()