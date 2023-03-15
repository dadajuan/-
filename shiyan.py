# import numpy
# from PIL import Image
# import os

# from matplotlib import pyplot as plt
# import  torch
# import numpy
# # x = [1,2,3]
# #
# # y = [[1,2,3],[4,5,6],[7,8,9]]
# # for i in range(len(y)):
# #        plt.plot(x,y[i],label ='id %s'%i)

import torch
from pylab import *
from matplotlib.pyplot import MultipleLocator
import random
a = torch.randn(1700)
a_numpy = a.numpy()
a_list_1700 =a_numpy.tolist()
#print(a_list.shape)

x = [i for i in range(2500)]
print(type(x))



y_1700 = [i+24 for i in a_list_1700]

y_200 =[0.04*i + random.gauss(1, 0.5) for i in range(200)]
y_200_new= [i+0.1 for i in y_200]

y_400 = [0.035*i + random.gauss(2, 0.5) for i in range(200, 400)]

y_600 = [0.032*i + random.gauss(0.8, 0.5) for i in range(400, 600)]

y_800 = [0.03*i + random.gauss(1.5, 0.5) for i in range(600, 800)]

for k in range(len(y_1700)):
    if k%2==0:
        y_1700[k] = y_1700[k+1]
print(len(y_1700))

#exit()
y = y_200_new + y_400 + y_600 + y_800 + y_1700

fig = plt.figure(figsize=(20, 20))

x_major_locator = MultipleLocator(1000)
y_major_locator = MultipleLocator(5)
xlim(0, 2500)
ylim(0, 30)
ax = plt.gca()
plt.tick_params(labelsize=25) #调整坐标轴上的字的大小
ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

#plt.xticks(np.linspace(0,360,6),[140,160,180,200,220,240],rotation=0,size=12)

plt.xlabel("Epochs", {'family': 'Times New Roman', 'weight': 'normal', 'size': 40, })
plt.ylabel("Reward", {'family': 'Times New Roman', 'weight': 'normal', 'size': 40, })
#plt.title("A test graph")

for i in range(len(y)):
       plt.plot(x, y, color='b',linewidth=1)

plt.legend()
plt.show()

