flag=2;
x=[1,2,3];
if flag==1
    y=[13 12 12];    
elseif flag==2
    y=[15 14 14];
elseif flag==3
    y=[16 15 14];
end
pic1=plot(x,y,'k','marker','^','markersize',10,'markeredgecolor','k','linewidth',2);
grid on;
axis([min(x)-0.2 max(x)+0.2 min(y)-0.2 max(y)+0.2]);
xlabel('Social Depth i','FontName','Times New Roman','FontSize',21);
ylabel('Transmission Round','FontName','Times New Roman','FontSize',21);
if flag==3
    title('Evolution Steps t=5000','FontName','Times New Roman','FontSize',21,'position',[1.7,14.1]);
    rectangle('position',[1.05 14.1 1.3 0.35],'linewidth',2);
    set(gcf,'position',[200,200,750,330]);
elseif flag==2
    title('Evolution Steps t=5000','FontName','Times New Roman','FontSize',21,'position',[2.35,14.5]);
    rectangle('position',[1.7 14.5 1.3 0.2],'linewidth',2);
    set(gcf,'position',[200,200,750,330]);
elseif flag==1
    title('Evolution Steps t=5000','FontName','Times New Roman','FontSize',21,'position',[2.35,12.5]);
    rectangle('position',[1.7 12.5 1.3 0.2],'linewidth',2);
    set(gcf,'position',[200,200,750,330]);
end
set(gca,'xtick',[1 2 3]);
set(gca,'ytick',[10:16]);
set(gca,'FontName','Times New Roman','fontsize',21);
legend({'Transmission Round'},'location','northeast','FontName','Times New Roman','FontSize',21);
if flag==1
    print(1,'-deps','evolution_steps=5000.eps');
    print(1,'-dpng','evolution_steps=5000.png');
elseif flag==2
    print(1,'-deps','gwevolution_steps=5000.eps');
    print(1,'-dpng','gwevolution_steps=5000.png');
elseif flag==3
    print(1,'-deps','bkevolution_steps=5000.eps');
    print(1,'-dpng','bkevolution_steps=5000.png');
end

x=[5000,6000,7000,8000,9000,10000];
if flag==1
    y=[12 13 13 13 13 14];
    z=[5 5 5 5 5 5];
elseif flag==2
    y=[14 14 15 15 15 16];
    z=[16 17 16 15 15 19];
elseif flag==3
    y=[15 15 15 15 15 15];
    z=[18 18 18 17 17 17];
end
[pic2,line1,line2]=plotyy(x,y,x,z);
grid on;
set(pic2(1),'ylim',[min(y)-0.5 max(y)+0.5],'ycolor','k','ytick',[5:19]);
set(pic2(2),'ylim',[min(z)-1 max(z)+1],'ycolor','k','ytick',[5:19]);
set(pic2,'xlim',[4500 10500]);
set(line1,'linestyle','-','color','k','marker','^','markersize',10,'markeredgecolor','k','linewidth',2);
set(line2,'linestyle','-','color','k','marker','o','markersize',10,'markeredgecolor','k','linewidth',2);
set(get(pic2(1),'ylabel'),'string','Transmission Round','FontName','Times New Roman','FontSize',21);
set(get(pic2(2),'ylabel'),'string','Diameter D','rotation',90,'FontName','Times New Roman','FontSize',21);
set(gca,'xcolor','k');
set(gca,'ycolor','k');
set(pic2(1),'FontName','Times New Roman','fontsize',21);
set(pic2(2),'FontName','Times New Roman','fontsize',21);
xlabel('Evolution Steps t','FontName','Times New Roman','FontSize',21);
if flag==3
    set(gcf,'position',[200,200,750,330]);
    title('Social Depth i=2','FontName','Times New Roman','FontSize',21,'position',[9000,15.2]);
    rectangle('position',[8000 15.2 2000 0.15],'linewidth',2);
    legend({'Transmission Round','Diameter D'},'location','southwest','FontName','Times New Roman','FontSize',21);
elseif flag==2
    set(gcf,'position',[200,200,750,330]);
    title('Social Depth i=2','FontName','Times New Roman','FontSize',21,'position',[8800,16]);
    rectangle('position',[7800 16 2000 0.4],'linewidth',2);
    legend({'Transmission Round','Diameter D'},'location','northwest','FontName','Times New Roman','FontSize',21);
elseif flag==1
    set(gcf,'position',[200,200,750,330]);
    title('Social Depth i=2','FontName','Times New Roman','FontSize',21,'position',[5700,13.5]);
    rectangle('position',[4700 13.5 2000 0.3],'linewidth',2);
    legend({'Transmission Round','Diameter D'},'location','southeast','FontName','Times New Roman','FontSize',21);
end
set(gca,'xtick',[5000 6000 7000 8000 9000 10000]);
if flag==1
    print(1,'-deps','social_depth=2.eps');
    print(1,'-dpng','social_depth=2.png');
elseif flag==2
    print(1,'-deps','gwsocial_depth=2.eps');
    print(1,'-dpng','gwsocial_depth=2.png');
elseif flag==3
    print(1,'-deps','bksocial_depth=2.eps');
    print(1,'-dpng','bksocial_depth=2.png');
end