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
a = torch.randn(152)
a_numpy = a.numpy()
a_list_152 =a_numpy.tolist()
#print(a_list.shape)

x = [i for i in range(200)]
print(type(x))


y_152 = [i+22 for i in a_list_152]
y_30 = [0.66*i + random.gauss(1, 0.5) for i in range(30)]
y_30_new = [i+0.1 for i in y_30]

y_40 = [0.25*i + 12 + random.gauss(2, 0.5) for i in range(30, 40)]
y_48 = [0.35*i + 7.5 + random.gauss(0.8, 0.5) for i in range(40, 48)]
y1 = y_30_new + y_40 + y_48 + y_152


a = torch.randn(120)
a_numpy = a.numpy()
a_list_120 =a_numpy.tolist()
y2_120 = [i+18 for i in a_list_120]

y2_25 = [0.48*i + random.gauss(0.1, 0.1) for i in range(25)]
y2_25_new = [i+0.1 for i in y2_25]

y2_32 = [0.41*i + 1.7 + random.gauss(2, 0.5)-2 for i in range(25, 32)]

y2_50 = [0.13*i + 12 + random.gauss(0.8, 0.5)-2 for i in range(32, 50)]

y2_80 = [0.1*i +13+ random.gauss(0.8, 0.5)-2 for i in range(50, 80)]

for k in range(len(y2_120)):
    if k%2 == 0:
        y2_120[k] = y2_120[k+1]
#exit()

y2 = y2_25_new + y2_32 + y2_50 + y2_80 + y2_120

y =[]
y.append(y1)
y.append(y2)
print(len(y1), len(y2), len(y))

fig = plt.figure(figsize=(10, 8))

x_major_locator = MultipleLocator(50)
y_major_locator = MultipleLocator(5)
xlim(0, 200)
ylim(0, 25)
ax = plt.gca()

ax.xaxis.set_major_locator(x_major_locator)
ax.yaxis.set_major_locator(y_major_locator)

plt.xlabel("Epochs", {'family': 'Times New Roman', 'weight': 'normal', 'size': 30, })
plt.ylabel("Reward", {'family': 'Times New Roman', 'weight': 'normal', 'size': 30, })
#plt.title("A test graph")
coloritem = ['b','r']
labelitem = ['DQN','AC']
for i in range(len(y)):
       plt.plot(x, y[i], color=coloritem[i],linewidth=2,label = labelitem[i] )

plt.legend()
plt.show()

