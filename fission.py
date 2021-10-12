# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:39:17 2021

@author: Baptiste
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim([-1,20])
ax.set_ylim([-10,10])

L = 40
theta = np.linspace(0,25,L)
theta2 = np.linspace(0,25,L)

x = theta
y = 0
Y = theta2

neutron, = ax.plot(0,0, 'ko')
neutron2, = ax.plot(-10,0, 'ko')
neutron3, = ax.plot(-10,0, 'ko')
uranium, = ax.plot(10,0, 'go')
uranium2, = ax.plot(-10.2,-10, 'ro')

annotation = ax.annotate(
    'Neutron', xy=(0,0), xytext=(0,0))
annotation3 = ax.annotate(
    'Neutron 2', xy=(-20,-20), xytext=(-20,-20))
annotation2 = ax.annotate(
    'U_235', xy=(10.04,0.2), xytext=(10.04,0.2))

annotation4 = ax.annotate(
    'U_236', xy=(- 20,20), xytext=(-20,20))
#retirer les graduations des axes
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
def update(i):
    uranium.set_data(10.2,0)
    uranium2.set_data(-10.2,0)
    annotation2.set_position((10.2,0.2))   
    annotation2.xy = (10.4,0.2)
    
    annotation4.set_position((-20,20))
    annotation4.xy = (-20,20)
    
    new_x = x[i%L]
    new_y = y
    
    if  new_x > 10 :
        neutron.set_data(-10,-10)
        annotation.set_position((-10,-10))
        annotation.xy = (-10,-10)
        
    #if  new_x > 10 and new_x < 15 : 
        
        uranium.set_data(-10,-10)
        uranium2.set_data(10.2,0)
        neutron.set_data(-10,0)
        
        #U_235
        annotation4.set_position((10.2,0.2))
        annotation4.xy = (10.2,0.2)
        
        annotation2.set_position((-20,20))
        annotation2.xy = (-20,20)
        
    if  new_x > 15 : 
        new_y = Y[i%L]-10
        #Neutron 2
        annotation3.set_position((new_x,new_y))
        annotation3.xy = (new_x,new_y)
        neutron3.set_data(new_x,new_y)
        neutron2.set_data(new_x,-new_y)
    
        
    else:  
        
        neutron.set_data(new_x,0)
        annotation.set_position((new_x+0.1,0.1))
        annotation.xy = (new_x,0)
        
    print(new_x)
    return neutron, annotation

ani = animation.FuncAnimation(
    fig, update, interval = 250, blit = False)

plt.show()