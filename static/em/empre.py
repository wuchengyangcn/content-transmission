import networkx as nx
import random

p1 = 0.5
g = nx.Graph()
g.add_nodes_from([1, 2, 3, 4, 5], bipartite=0)
g.add_nodes_from([-1, -2, -3], bipartite=1)
leftnode = 5
leftbound = 2
rightnode = -3
rightbound = 3
g.add_edges_from([(1, -1), (1, -2), (2, -1), (2, -3), (3, -1),
                  (3, -3), (4, -1), (4, -2), (4, -3), (5, -2), (5, -3)])
pos = []
for node in range(5000):
    pos.append([round(random.random(), 4), round(random.random(), 4)])
for nums in [2500, 3000, 3500, 4000, 4500, 5000]:
    while abs(rightnode) < nums:
        targetedge = random.sample(g.edges(), 1)[0]
        if random.random() < p1:
            leftnode += 1
            g.add_node(leftnode, bipartite=0)
            model = max(targetedge)
            temp = random.sample(list(g.neighbors(model)), leftbound)
            for j in temp:
                g.add_edge(leftnode, j)
        else:
            rightnode -= 1
            g.add_node(rightnode, bipartite=1)
            model = min(targetedge)
            temp = random.sample(list(g.neighbors(model)), rightbound)
            for j in temp:
                g.add_edge(j, rightnode)
    top = [i for i in range(1, leftnode+1)]
    bottom = [i for i in range(-1, rightnode-1, -1)]
    em = nx.Graph()
    for node in top:
        temp = g.neighbors(node)
        for i in temp:
            for j in temp:
                if i != j:
                    em.add_edge(-i-1, -j-1)
    outfile = open('em'+str(nums)+'.txt', 'w')
    outfile.write(str(nx.diameter(em))+'\n')
    for i in em.edges():
        outfile.write(str(i[0])+' '+str(i[1])+'\n')
    outfile.close()
    outfile = open('em'+str(nums)+'pos.txt', 'w')
    for i in range(nums):
        outfile.write(str(pos[i][0]) + ' ' + str(pos[i][1]) + '\n')
    outfile.close()
