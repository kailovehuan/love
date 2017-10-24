# coding:utf-8
'''
Created on 2017/10/24

@author: sunyihuan
'''

import pylab as plt
from matplotlib import colors

a = [[] for i in range(1000)]

i = 0
while i < 1000:
    j = 0
    while j < 1000:
        x = -1.8 + 0.003 * i
        y = -1.4 + 0.0028 * j
        z = y ** 2 + (-x - (y ** 2) ** 0.33333) ** 2
        if z <= 1:
            a[i].append(0.9)
        else:
            a[i].append(0.0)
        j = j + 1
    i = i + 1

cmap = colors.ListedColormap(['white', 'pink'])
im = plt.imshow(a, cmap=cmap, interpolation='bicubic')
plt.show()
