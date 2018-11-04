import networkx as nx
import random
g = nx.Graph()
order = {}
current = 0
for line in open('Brightkite_edges.txt').readlines():
    [u, v]=line.strip().split()
    if u not in order:
        order[u] = current
        current += 1
    if v not in order:
        order[v] = current
        current += 1
    g.add_edge(order[u], order[v])

source = random.sample(list(g.nodes()), 1)[0]
order = {source: 0}
current = 1

pos = []
for node in range(5000):
    pos.append([round(random.random(), 4), round(random.random(), 4)])

for num in [2500, 3000, 3500, 4000, 4500, 5000]:
    while current < num:
        target = random.sample(list(g.neighbors(source)), 1)[0]
        tolerate = 100
        while g.degree(target) >= 0.012 * num:
            target = random.sample(list(g.neighbors(source)), 1)[0]
            tolerate -= 1
            if tolerate == 0: break
        if target not in order:
            order[target] = current
            current += 1
        source = target
    subgraph = g.subgraph(list(order.keys()))
    outfile = open('bkst'+str(num)+'.txt', 'w')
    outfile.write(str(nx.diameter(subgraph))+'\n')
    for edge in subgraph.edges():
        outfile.write(str(edge[0])+' '+str(edge[1])+'\n')
    outfile.close()
    outfile = open('bkst'+str(num)+'pos.txt', 'w')
    for node in range(num):
        outfile.write(str(pos[node][0])+' '+str(pos[node][1])+'\n')
    outfile.close()
