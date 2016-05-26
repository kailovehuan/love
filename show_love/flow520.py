# coding:utf-8
'''
Created on 2016/5/26

@author: sunyihuan
'''
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

figure = plt.figure()
axes = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line1, = axes.plot([], [], color='red', linewidth=2, label='1')
line2, = axes.plot([], [], color='red', linewidth=2, label='2')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def animate(i):
    print i
    t = np.linspace(0, i / math.pi, 100)
    x = np.sin(t)
    y = np.cos(t) + np.power(x, 2.0 / 3)
    line1.set_data(x, y)
    line2.set_data(-x, y)
    return line1, line2


ani = animation.FuncAnimation(figure, animate, init_func=init, frames=14, interval=200)
plt.show()