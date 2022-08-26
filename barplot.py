import matplotlib.pyplot as plt

x=[1,2,3]  # 确定柱状图数量,可以认为是x方向刻度

y=[181,648,158]  # y方向刻度
yerrer=[31,44,26]
#保存为png
def savefig(filename, fig):
    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = f'{filename}_time_{timestr}.png'
    fig.savefig(filename, bbox_inches='tight')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        #设置图例字体、位置、数值等等
        plt.text(rect.get_x(), 1.01*height, '%s' %
                 int(height), size=30, family="Times new roman")

#color=['#c19277','#9dad7f','#62959c']#,'orchid','deepskyblue'
plt.style.use('default')
plt.rcParams['font.size']=30#30
#plt.rc('font', family='sans-serif')
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams["font.weight"] = "medium"
plt.rcParams['pdf.fonttype'] = 42
#plt.figure(figsize=(11,9))
fig, ax = plt.subplots(figsize=(11, 9))
#设置柱状图颜色
colors = ['red','lightskyblue','yellowgreen']

plt.ylim([0,700])#设置y轴范围
plt.ylabel('Delay')

x_label=['ROI','DEC','Our']
plt.xticks(x, x_label)  # 绘制x刻度标签

# 绘制柱状图
rect=plt.bar(x, y,color=colors,width=0.5)#width是宽度

#标注图中的数据大小
autolabel(rect)
#画误差棒，ecolor是棒的颜色，elinewidth是棒的大小，capsize横杠的长度，capthick是横杠的厚度。fmt是数据点格式，'o'是圆点，'o-'是将数据点连接起来，color='black'数据点颜色，ms设置数据点大小
plt.errorbar(x,y,yerrer,fmt='o',ecolor='b',color='black',ms=15,elinewidth=10,capsize=10,capthick=8)

#设置网格刻度
plt.grid(True,linestyle=':',color='r',alpha=0.6)
plt.show()
#保存图片，要保存图片就打开下面注释
# savefig('errer bar',fig )