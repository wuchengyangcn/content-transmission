import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()
status = []
infile = open('em2500small.txt')
d = int(infile.readline())
order = {}
current = 0
for temp in infile:
    [u, v] = temp.split()
    if u not in order:
        order[u] = current
        current += 1
    if v not in order:
        order[v] = current
        current += 1
    graph.add_edge(order[u], order[v])
infile.close()
dic = {}
for i in graph.nodes():
    num = graph.degree(i)
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
x = dic.keys()
y = dic.values()
plt.loglog(x, y, 'd')
plt.axis([0.5, 3000, 0.5, 2000])
plt.grid()
plt.savefig('degree.png')
plt.show()
