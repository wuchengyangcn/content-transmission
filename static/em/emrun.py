import networkx as nx
import random
from queue import Queue as q
import math
from time import time

def hop(n, depth, data):
    if n not in data:
        data.append(n)
    if depth == 0:
        return
    for i in g.neighbors(n):
        hop(i, depth - 1, data)
    return

# distance
d = 6
bound = [15000, 16000, 17000, 18000, 19000, 20000]
files = ['em2500', 'em3000', 'em3500', 'em4000', 'em4500', 'em5000']
for flag in [0, 1, 2, 3, 4, 5]:
    g = nx.Graph()
    order = {}
    current = 0
    infile = open(files[flag]+'small.txt')
    for line in infile.readlines():
        [u, v] = line.strip().split(' ')
        if u not in order:
            order[u] = current
            current += 1
        if v not in order:
            order[v] = current
            current += 1
        g.add_edge(order[u], order[v])
    infile.close()
    n = g.number_of_nodes()
    print(n)
    pos = []
    for line in open(files[flag]+'pos.txt').readlines():
        [u, v] = line.strip().split()
        pos.append([float(u)*n**0.5, float(v)*n**0.5])
    for maxhop in [2,1]:
        for co in [50, 40, 30, 20, 10]:
            start = time()
            distance = co/100*(n**(1-2/d*math.floor(maxhop/2)))\
                * math.log10(n)/math.pi
            source = random.randint(0, n-1)
            trees = [q()]*n
            flags = [0]*n
            total = []
            new = [source]
            checktime = 0
            special = []
            specialtarget = []
            specialcount = []
            while len(total) < nx.number_of_nodes(g):
                checktime += 1
                # new nodes lead to new eager nodes
                eager = []
                for i in new:
                    flags[i] = 2
                    total.append(i)
                    for j in g.neighbors(i):
                        if flags[j] == 0:
                            eager.append(j)
                            flags[j] = 1
                    # check special nodes
                    for j in range(0, len(special)):
                        if i in specialtarget[j]:
                            specialcount[j] += 1
                for i in eager:
                    temp = [i]
                    hop(i, maxhop, temp)
                    valid = []
                # nodes within i hops and within distance and have file are valid
                    for j in temp[1:]:
                        if flags[j] > 1 and (pos[i][0]-pos[j][0])**2 + \
                         (pos[i][1]-pos[j][1])**2 < distance:
                            valid.append(j)
                # randomly add to one of the trees
                    if len(valid) > 0:
                        target = random.sample(valid, 1)[0]
                        trees[target].put(i)
                # consider special nodes
                    else:
                        special.append(i)
                        count = 0
                        target = []
                        for j in temp[1:]:
                            if nx.shortest_path_length(g, source=source, target=i) >\
                                    nx.shortest_path_length(g, source=source, target=j):
                                target.append(j)
                                if flags[j] > 1:
                                    count += 1
                        specialtarget.append(target)
                        specialcount.append(count)
                new = []
                # send file to new nodes on the trees
                for i in range(0, n):
                    if flags[i] > 1:
                        for j in range(0, int(flags[i])):
                            if not trees[i].empty():
                                new.append(trees[i].get())
                            else:break
                        flags[i] *= 2
                # send file to special nodes
                for i in range(0, len(special)):
                    if specialcount[i] == len(specialtarget[i]):
                        target = random.sample(specialtarget[i], 1)[0]
                        trees[target].put(special[i])
                        specialcount[i] += 1
                print(len(total))
            end = time()
            outfile = open('em.txt', 'a')
            outfile.write(files[flag]+' co='+str(co)+' '+str(distance)+' i='+str(maxhop)+' slot=' +
                          str(checktime)+'\tt='+str(round(end-start, 4))+'\n')
            outfile.close()
