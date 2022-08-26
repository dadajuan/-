import matplotlib.pyplot as plt
import yaml

from matplotlib.ticker import FuncFormatter
# colors = [
#     '#c19277', #mpeg
#     '#62959c', #ours
#     '#9dad7f', #dds
#     '#d9dab0', #eaar
#     '#a98b98', #cloudseg
#     '#c1c0b9' # reducto
# ]
#颜色
colors = ['red',
          'lightskyblue',
          'yellowgreen'

]

# set default parameters
plt.style.use('default')
plt.rcParams['font.size']=20#30#字体大小
#plt.rc('font', family='sans-serif')
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams["font.weight"] = "medium"
plt.rcParams['pdf.fonttype'] = 42


import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Ellipse

#保存为png
def savefig(filename, fig):
    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = f'{filename}_time_{timestr}.png'
    fig.savefig(filename, bbox_inches='tight')

#画椭圆
def add_data(ax, data, color):

    # print(data[1])
    cov = np.cov(data[0], data[1])
    lambda_, v = np.linalg.eig(cov)
    lambda_ = np.sqrt(lambda_) / math.sqrt(len(data[0]))

    #print(np.mean(data[0]), np.mean(data[1]))#打印中心点

    ell = Ellipse(xy=(np.mean(data[0]), np.mean(data[1])),
                  width=lambda_[0]*2,
                  height=lambda_[1]*2,
                  angle=np.rad2deg(np.arccos(v[0,0])),
                  alpha=0.8)
    ell.set_edgecolor(color)
    ell.set_facecolor(color)
    ax.add_artist(ell)
    #plt.scatter(data[0], data[1], c = color)
    ax.scatter([np.mean(data[0])], [np.mean(data[1])], marker = 'o', color = 'black', s=10,zorder=3)
    return np.mean(data[0]).item(), np.mean(data[1]).item()


fig, ax = plt.subplots(figsize=(11, 9))
ax.grid()

#将注释打开就是打印那个图
#图1,原图1270KB
accs=([0.9415, 0.944, 0.9228, 0.958, 0.9170, 0.8949, 0.9055, 0.8873],[368.16, 300.67, 279, 270, 199.42, 187.15, 165.67, 156.47] )#our
accs1=([0.89459, 0.8509, 0.8433, 0.8294, 0.7934], [721.35, 366.51, 322, 402.79, 318.35])#ROI
accs2=([0.944, 0.9209, 0.8433, 0.8994, 0.8834], [748.68, 671, 677, 501.89, 504.99])#CLOUD

#图2，原图927KB
# accs=([0.928, 0.935, 0.926, 0.928, 0.927, 0.925, 0.9112, 0.910], [408, 276.87, 255.43, 245.21, 235.56, 214.78, 204.34, 197.53])#our
# accs1=([0.9124, 0.8836, 0.8745, 0.8524, 0.8082], [514.05, 375.8, 249.53,194.91, 131.19])#ROI
# accs2=([0.9241, 0.9347, 0.8753, 0.8354, 0.8645], [456.77, 497.47, 498.63, 438.45, 472.76])#CLOUD

#图3，原图943KB
# accs=([0.948, 0.947, 0.944, 0.928, 0.945, 0.946, 0.945, 0.943], [229.34, 210.23,189.20, 183.47, 179.65, 172.11,168.18, 162.45])#our
# accs1=([0.9293, 0.8425, 0.8644, 0.8353, 0.8123], [429.93, 353.69, 356.98, 314.88, 282.35])#ROI
# accs2=([0.9438, 0.9312, 0.9234, 0.8875, 0.9054], [577.39, 576.36, 549.98, 532.18, 510.12])#CLOUD

#图4，原图1147KB
# accs=([0.91, 0.915, 0.91, 0.904, 0.906, 0.907, 0.909, 0.9], [408.34, 360.32, 336.28, 336.28, 312.26, 288.24,287.57, 259.41])#our
# accs1=([0.8932, 0.8731, 0.8468, 0.8402, 0.8356], [491.45, 363.51, 349.62, 218.26,194.39])#ROI
# accs2=([0.9151, 0.9130, 0.9013, 0.8876, 0.8967], [691.56, 664.23, 647.28, 631.88, 589.14])#CLOUD


x, y = add_data(ax, accs1, colors[0])
ax.text(x + 0.005, y-50 , 'ROI')#图中的标注
x, y = add_data(ax, accs, colors[1])
ax.text(x, y-35 , 'Our')
x, y = add_data(ax, accs2, colors[2])
ax.text(x+0.004, y-65 , 'DEC')

#设置坐标轴范围
l, r = 0.82, 0.94
b, u = 0, 700
ax.set_xlim(l,r)#设置x轴范围
ax.set_ylim(b,u)#设置y轴范围
ax.set_xticks([0.82, 0.84, 0.86, 0.88,0.90,0.92,0.94])#设置x轴刻度
ax.set_xlabel('Confidence Score')
ax.set_ylabel('Data Amount')

#设置Better箭头的，ec是框的颜色，rotation是箭头角度
bbox_props = dict(boxstyle="rarrow", fc=(1,1,1), ec="grey", lw=2)
t = ax.text(l,u, "Better", ha="left", va="top", rotation=-45,#right  bottom
            bbox=bbox_props)
bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.05)


plt.show()
#保存图片
savefig('detection_drone_FPN', fig)


