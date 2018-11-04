import networkx as nx
import random

bound = [15000, 16000, 17000, 18000, 19000, 20000]
files = ['em2500', 'em3000', 'em3500', 'em4000', 'em4500', 'em5000']
for flag in [0, 1, 2, 3, 4, 5]:
    g0 = nx.Graph()
    order = {}
    current = 0
    infile = open(files[flag]+'.txt')
    d = int(infile.readline())
    for line in infile.readlines():
        [u, v] = line.strip().split()
        if u not in order:
            order[u] = current
            current += 1
        if v not in order:
            order[v] = current
            current += 1
        g0.add_edge(order[u], order[v])
    infile.close()
    print(g0.number_of_edges())
    g1 = nx.Graph()
    while g1.number_of_edges() < bound[flag]:
        choose = random.sample(list(g0.nodes()), 1)[0]
        g1.add_edges_from(list(nx.bfs_edges(g0, choose)))
    g = nx.Graph()
    order = {}
    current = 0
    for edge in g1.edges():
        if edge[0] not in order:
            order[edge[0]] = current
            current += 1
        if edge[1] not in order:
            order[edge[1]] = current
            current += 1
        g.add_edge(order[edge[0]], order[edge[1]])
    n = g.number_of_nodes()
    print(str(n)+' '+str(g.number_of_edges()))
    outfile = open(files[flag]+'small.txt', 'w')
    for edge in g.edges():
        outfile.write(str(edge[0])+' '+str(edge[1])+'\n')
    outfile.close()