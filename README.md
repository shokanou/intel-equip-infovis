### intel-equip-infovis  
#### visual analysis of data collected from intelligent household robot "Rokid"  
Rokid's website: https://www.rokid.com/  
using *d3.js* for visualization  
web framework  *Python-flask*  

首先， 从若琪获取的数据如图所示  
![alt](/data.png)  
可以看出这些数据是结构化的，显示了机器接收到的指令和机器对该指令进行的操作  
我们首先需要对数据进行处理，为每个数据贴上标签，然后对数据使用k-means聚类分析  
聚类人群在一段时间内的变化呈现可以使用桑基图  
![alt](/sankey.png)  
一天内某一人群的聚类结果可以用热力图的方式展现其规律  
![alt](/heatmap.png)  
一段时间内的操作数量则可以用柱状图的方式来直观的呈现  
![alt](/bar.png)  
一天内不同主题的操作数量变化则可以用customized饼图来展示  
![alt](/pie.png)  
而在这些不同的之间，我也加入了交互的操作，使用户更有操作感  
最后的系统页面  
![alt](/main.png)  
![alt](/iv.jpeg)  
