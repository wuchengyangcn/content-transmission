import networkx
import random
import time
import queue
import math
start=time.time();
times=2000;
p1=0.5;
p2=1-p1;
g=networkx.Graph();
g.add_nodes_from([1,2,3,4,5],bipartite=0);
g.add_nodes_from([-1,-2,-3],bipartite=1);
leftnode=5;
leftbound=2;
rightnode=-3;
rightbound=3;
#number of maximum hop
maxhop=2;
g.add_edges_from([(1,-1),(1,-2),(2,-1),(2,-3),(3,-1),\
                  (3,-3),(4,-1),(4,-2),(4,-3),(5,-2),(5,-3)]);
for i in range(0,times):
    targetedge=random.sample(g.edges(),1)[0];
    if random.random()<p1:
        leftnode+=1;
        g.add_node(leftnode,bipartite=0);
        model=max(targetedge);
        temp=random.sample(g.neighbors(model),leftbound);
        for j in temp:
            g.add_edge(leftnode,j);
    else:
        rightnode-=1;
        g.add_node(rightnode,bipartite=1);
        model=min(targetedge);
        temp=random.sample(g.neighbors(model),rightbound);
        for j in temp:
            g.add_edge(j,rightnode);
top=[];
bottom=[];
#generate social graph
for i in range(1,leftnode+1):top.append(i);
for i in range(-1,rightnode-1,-1):bottom.append(i);
socialbottom=networkx.Graph();
end=time.time();
print(end-start,'\ts');
for topnode in top:
    temp=g.neighbors(topnode);
    for i in temp:
        for j in temp:
            if i!=j:socialbottom.add_edge(-i,-j);
"""
socialtop=networkx.Graph();
for bottomnode in bottom:
    temp=g.neighbors(bottomnode);
    for i in temp:
        for j in temp:
            if i !=j:socialtop.add_edge(i,j);
"""
end=time.time();
print(end-start,'\ts');
#random positions
squarelength=(-rightnode)**0.5;
positions=[];
for i in range(0,-rightnode):
    positions.append([random.random()*squarelength,\
                      random.random()*squarelength]);
#calculate gamma and square of L
delta=leftbound/rightbound;
d=networkx.diameter(socialbottom);
gamma=min(3/14,1/d);
distance=0.4*(-rightnode)**(1-gamma*(math.floor(maxhop/2)-delta))\
        *math.log10(-rightnode)/math.pi;
source=random.randint(1,-rightnode);
trees=[queue.Queue()]*-rightnode;
flags=[0]*-rightnode;
end=time.time();
print(end-start,'\ts');

#sub function to find neighbors in depth hops
def hop(n,depth,data):
    if depth==0:
        if n not in data:
            data.append(n);
        return;
    for i in socialbottom.neighbors(n):
        hop(i,depth-1,data);
    return;
total=[];
new=[source];
checktime=0;
special=[];
specialtarget=[];
specialcount=[];
print();

while len(new)>0:
    checktime+=1;
    #new nodes lead to new eager nodes
    eager=[];
    for i in new:
        flags[i-1]=2;
        total.append(i);
        for j in socialbottom.neighbors(i):
            if flags[j-1]==0:
                eager.append(j);
                flags[j-1]=1;
    #check special nodes
        for j in range(0,len(special)):
            if i in specialtarget[j]:specialcount[j]+=1;
    for i in eager:
        temp=[i];
        hop(i,maxhop,temp);
        valid=[];
    #nodes within maxhop hops and within distance and have file are valid
        for j in temp[1:]:
            if flags[j-1]>1 and (positions[i-1][0]-positions[j-1][0])**2+\
            (positions[i-1][1]-positions[j-1][1])**2<distance:
                valid.append(j);
    #randomly add to one of the trees
        if len(valid)>0:
            target=random.sample(valid,1)[0];
            trees[target-1].put(i);
    #consider special nodes
        else:
            special.append(i);
            count=0;
            target=[];
            for j in temp[1:]:
                if networkx.shortest_path_length(socialbottom,source=source,\
                target=i)>networkx.shortest_path_length(socialbottom,\
                source=source,target=j):
                    target.append(j);
                    if flags[j-1]>1:count+=1;
            specialtarget.append(target);
            specialcount.append(count);
    new=[];
    #send file to new nodes on the trees
    for i in range(0,-rightnode):
        if flags[i]>1:
            for j in range(0,int(flags[i])):
                if not trees[i].empty():new.append(trees[i].get());
            flags[i]*=2;
    #send file to special nodes
    for i in range(0,len(special)):
        if specialcount[i]==len(specialtarget[i]) and flags[special[i]-1]<2:
            new.append(special[i]);
    end=time.time();
    print(end-start,'\ts');
print (checktime);
print (-rightnode-len(total),'\tnodes left');
end=time.time();
print(end-start,'\ts');