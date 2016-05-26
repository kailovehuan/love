# coding:utf-8
'''
Created on 2016/5/26

@author: sunyihuan
'''
import matplotlib.pyplot as plt
figure = plt.figure()
axes = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line1, = axes.plot([], [], color='red', linewidth=2, label='1')

plt.show()