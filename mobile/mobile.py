import networkx as nx
import numpy as np
import random
class data:
    graph = nx.Graph()
    status = []
    pos = []
    def __init__(self,file):
        self.name = file
        infile = open(self.name+'.txt')
        self.d = int(infile.readline())
        nodeorder = {}
        currentorder = 0
        for temp in infile:
            [u, v] = temp.split()
            if u not in nodeorder:
                nodeorder[u] = currentorder
                currentorder += 1
            if v not in nodeorder:
                nodeorder[v] = currentorder
                currentorder += 1
            self.graph.add_edge(nodeorder[u], nodeorder[v])
        infile.close()
        self.n = self.graph.number_of_nodes()
        print(self.n, 'nodes')
        self.move()
        self.trans = []
        self.recv = []

    def propagate(self, i, co):
        self.status = [0]*self.n
        target = 500
        targets = self.map(target, np.ceil(i/2))
        for temp in targets:
            self.status[temp] = 2
        self.have = len(targets)
        gamma = min(3/14, 1/self.d)
        self.l = (self.n**(1-gamma*(np.floor(i/2)-2/3))/np.log10(self.n))**0.25*co
        time = 0
        while self.have < self.n:
            self.connect(i)
            self.transmit()
            self.move()
            time += 1
            print(self.have)
        outfile = open('result.txt', 'a')
        outfile.write(self.name+'\tco='+str(co)+'\ti='+str(i)+'\ttime='+str(time)+'\n')
        outfile.close()

    def move(self):
        self.pos = []
        for temp in range(0, self.n):
            self.pos.append([random.random()*self.n**0.5, random.random()*self.n**0.5])

    def transmit(self):
        for temp in self.recv:
            self.status[temp] = 2
            self.have += 1
        for temp in self.trans:
            self.status[temp] = 2
        self.trans = []
        self.recv = []

    def connect(self, i):
        for temp in range(self.n):
            if self.status[temp] == 0:
                if not self.notransmitter(temp):
                    continue
                result = self.source(temp, i)
                if len(result) == 0:
                    continue
                target = random.randint(0, len(result)-1)
                self.status[temp] = 1
                self.status[result[target]] = 3
                self.recv.append(temp)
                self.trans.append(result[target])

    def source(self, node, i):
        result = []
        neighbor = self.map(node, i)
        for temp in neighbor:
            if self.status[temp] == 2 and self.near(node, temp):
                result.append(temp)
        return result

    def map(self, node, i):
        if i == 0:
            return [node]
        result = [node]
        for temp1 in self.graph.neighbors(node):
            for temp2 in self.map(temp1, i-1):
                if temp2 not in result:
                    result.append(temp2)
        return result

    def notransmitter(self, node):
        for temp in self.trans:
            if self.near(node, temp):
                return False
        return True

    def near(self, node1, node2):
        [x1, y1] = self.pos[node1]
        [x2, y2] = self.pos[node2]
        return (x1-y1)*(x1-y1)+(x2-y2)*(x2-y2)<self.l*self.l


for file in ['em5000small']:
    dataset = data(file)
    for co in [9.6,9.4,9.2,9.8,9.5,9.3]:
        for i in [3]:
            dataset.propagate(i, co)
    open('result.txt', 'a').write('\n')
