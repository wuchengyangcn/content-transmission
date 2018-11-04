tic;
temp=textread('10000.txt');
data=temp(2:end,1:2)+1;
data2=data(:);
degree=zeros(1,max(data2));
for i =1:length(data2)
    degree(1,data2(i))=degree(1,data2(i))+1;
end
degree=sort(degree,'descend');
dict=zeros(1000,2);
index=1;
flag=degree(1,index);
dict(index,1)=flag;
for i =1:length(degree)
    if (degree(i)~=flag)
        flag=degree(i);
        index=index+1;
        dict(index,1)=flag;
    end
    dict(index,2)=dict(index,2)+1;
end
x=dict(:,1)';
x(x==0)=[];
y=dict(:,2)';
y(y==0)=[];
y=y/length(degree);
loglog(x,y,'k.','marker','d','markersize',4,'markeredgecolor','b','markerfacecolor','b');
hold on;
grid on;
xlabel('User Degree','FontName','Times New Roman','FontSize',21);
ylabel('Distribution of User Degree','FontName','Times New Roman','FontSize',21);
set(gca,'xtick',[1 10 100 1000 10000]);
set(gca,'ytick',[0.0001 0.001 0.01 0.1]);
axis([min(x)-0.3 max(x)+300 0.00015 max(y)+0.008]);
x=1:2000;
y=0.9./(x.^1.3);
plot(x,y,'--r');
legend({'Data Point','Fitted Line'},'location','northeast','FontName','Times New Roman','FontSize',21);
print(1,'-deps','degreepicture.eps');
print(1,'-dpng','degreepicture.png');
fig=gcf;
saveas(fig,'degreepicture.fig');
toc;