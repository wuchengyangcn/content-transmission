import networkx
import random
import time
import queue
import math
start=time.time();
files=['5000.txt','6000.txt','7000.txt','8000.txt','9000.txt','10000.txt'];
fileflag=0;
totaltimes=2;
infile=open(files[fileflag]);
d=int(infile.readline());
g=networkx.Graph();
for i in infile:
    [u,v]=i.split();
    g.add_edge(int(u),int(v));
infile.close();
delta=2/3;
n=networkx.number_of_nodes(g);
squarelength=(n)**0.5;
positions=[];
for i in range(0,n):
    positions.append([random.random()*squarelength,\
                      random.random()*squarelength]);
gamma=min(3/14,1/d);
end=time.time();
print(end-start,'\ts');

#sub function to find neighbors in depth hops
def hop(n,depth,data):
    if n not in data:data.append(n);
    if depth==0:return;
    for i in g.neighbors(n):
        hop(i,depth-1,data);
    return;

for maxhop in range(5,6):
    for coefficient in range(90,19,-10):
        distance=coefficient/100*(n)**(1-gamma*(math.floor(maxhop/2)-delta))\
            *math.log10(n)/math.pi;
        for times in range(0,totaltimes):   
            source=random.randint(1,n);
            trees=[queue.Queue()]*n;
            flags=[0]*n;
            total=[];
            new=[source];
            checktime=0;
            special=[];
            specialtarget=[];
            specialcount=[];    
            while len(total)<networkx.number_of_nodes(g):
                checktime+=1;
                #new nodes lead to new eager nodes
                eager=[];
                for i in new:
                    flags[i]=2;
                    total.append(i);
                    for j in g.neighbors(i):
                        if flags[j]==0:
                            eager.append(j);
                            flags[j]=1;
                #check special nodes
                    for j in range(0,len(special)):
                        if i in specialtarget[j]:specialcount[j]+=1;
                for i in eager:
                    temp=g.nodes();
                    temp.remove(i);
                    valid=[];
                #nodes within maxhop hops and within distance and have file are valid
                    for j in temp:
                        if flags[j]>1 and (positions[i][0]-positions[j][0])**2+\
                        (positions[i][1]-positions[j][1])**2<distance:
                            valid.append(j);
                #randomly add to one of the trees
                    if len(valid)>0:
                        target=random.sample(valid,1)[0];
                        trees[target].put(i);
                #consider special nodes
                    else:
                        special.append(i);
                        count=0;
                        target=[];
                        for j in temp:
                            if networkx.shortest_path_length(g,source=source,\
                            target=i)>networkx.shortest_path_length(g,\
                            source=source,target=j):
                                target.append(j);
                                if flags[j]>1:count+=1;
                        specialtarget.append(target);
                        specialcount.append(count);
                new=[];
                #send file to new nodes on the trees
                for i in range(0,n):
                    if flags[i]>1:
                        for j in range(0,int(flags[i])):
                            if not trees[i].empty():new.append(trees[i].get());
                        flags[i]*=2;
                #send file to special nodes
                for i in range(0,len(special)):
                    if specialcount[i]==len(specialtarget[i]):
                        target=random.sample(specialtarget[i],1)[0];
                        trees[target].put(special[i]);
                        specialcount[i]+=1;
                print(source);
            outfile=open('result.txt','a');
            outfile.write(files[fileflag]+'\t');
            outfile.write('coefficient='+str(coefficient)+'\t');
            outfile.write('maxhop='+str(maxhop)+'\t');
            outfile.write('time='+str(checktime)+'\n');
            outfile.close();
            print (checktime);