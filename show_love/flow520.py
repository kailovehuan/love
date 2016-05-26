# coding:utf-8
'''
Created on 2016/5/26

@author: sunyihuan
'''
import matplotlib.pyplot as plt      #加载matplotlib包
from matplotlib import animation
import numpy as np                   #加载numpy包
import math

figure = plt.figure()    #新建一张空白图片
axes = plt.axes(xlim=(-2, 2), ylim=(-2, 2))    #坐标的区间为x，[-2,2],y，[-2,2]
line1, = axes.plot([], [], color='red', linewidth=2, label='1')   #定义之后动画的内容
line2, = axes.plot([], [], color='red', linewidth=2, label='2')

# init()是我们的动画在在创建动画基础框架(base frame)时调用的函数
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


# 定义动画函数
def animate(i):
    print i
    t = np.linspace(0, i / math.pi, 100)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 3)
    line1.set_data(x, y)
    line2.set_data(-x, y)
    return line1, line2


# 显示动画
ani = animation.FuncAnimation(figure, animate, init_func=init, frames=14, interval=100)
plt.show()