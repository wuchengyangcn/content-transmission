import networkx as nx
from random import random
g = nx.Graph()
order = {}
current = 0
for line in open('Gowalla_edges.txt').readlines():
    [u, v]=line.strip().split()
    if u not in order:
        order[u] = current
        current += 1
    if v not in order:
        order[v] = current
        current += 1
    g.add_edge(order[u], order[v])
pos = []
for node in range(5000):
    pos.append([round(random(), 4), round(random(), 4)])
degrees ={}
for node in g.nodes():
    degrees[node] = g.degree(node)
nodes = sorted(degrees, reverse=True, key = degrees.__getitem__)
start = 1200
for num in [2502, 3004, 3507, 4014, 4524, 5016]:
    choose = max(nx.connected_component_subgraphs(nx.subgraph(g, nodes[start:start+num])), key=len)
    total = choose.number_of_nodes()
    outfile = open('gwem'+str(total)+'.txt', 'w')
    outfile.write(str(nx.diameter(choose)) + '\n')
    for edge in choose.edges():
        outfile.write(str(edge[0])+' '+str(edge[1])+'\n')
    outfile.close()
    outfile = open('gwem'+str(total)+'pos.txt', 'w')
    for node in range(total):
        outfile.write(str(pos[node][0])+' '+str(pos[node][1])+'\n')
    outfile.close()
