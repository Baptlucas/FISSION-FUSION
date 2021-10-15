# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:39:17 2021

@author: Baptiste
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

ax.set_xlim([5,20])
ax.set_ylim([-10,10])

L = 400
theta = np.linspace(0,25,L)
theta2 = np.linspace(0,25,L)

x = theta
y = 0
Y = theta2
X = theta2
neutron, = ax.plot(0,0, 'ko', markersize = 1)
neutron2, = ax.plot(-10,0, 'ko', markersize = 1)
neutron3, = ax.plot(-10,0, 'ko', markersize = 1)
uranium, = ax.plot(10,0, 'go', markersize = 10)
uranium2, = ax.plot(-10.2,-10, 'ro', markersize = 10)

profission, = ax.plot(-10,0, 'ro', markersize = 5)
profission1, = ax.plot(-10,0, 'ro', markersize = 5)
annotation = ax.annotate(
    'Neutron', xy=(0,0), xytext=(0,0))
annotation3 = ax.annotate(
    'Neutron ', xy=(-20,-20), xytext=(-20,-20))
annotation2 = ax.annotate(
    '$U_{235}$', xy=(10.2,0.5), xytext=(10.2,0.5))

annotation4 = ax.annotate(
    '$U_{236}$', xy=(- 20,20), xytext=(-20,20))
#retirer les graduations des axes
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)    
annotation5 = ax.annotate("", xy=(-9.5, 0), xytext=(-14.5, 0),
            arrowprops=dict(arrowstyle="->"))

def update(i):
    
    uranium.set_data(10.2,0)
    uranium2.set_data(-10.2,0)
    annotation2.set_position((9.5,0.5))   
    annotation2.xy = (9.5,0.5)
    
    annotation4.set_position((-20,20))
    annotation4.xy = (-20,20)
    
    profission.set_data(-15,1)
    profission1.set_data(-15,-1)
    
    new_x = x[i%L]
    new_y = y
    
    if  10< new_x < 15:
        
        neutron.set_data(-10,-10)
        neutron2.set_data(-10,-10)
        neutron3.set_data(-10,-10)
        annotation.set_position((-10,-10))
        annotation.xy = (-10,-10)        
        
        uranium.set_data(-10,-10)
        uranium2.set_data(10.2,0)
        
        
        #U_235
        annotation4.set_position((9.5,0.5))
        annotation4.xy = (9.5,0.5)
        
        annotation2.set_position((-20,20))
        annotation2.xy = (-20,20)
        if 10.5< new_x < 15:
            annotation5.set_position((10.5,0))
            annotation5.xy = (new_x,0)
        
       
    elif  new_x >= 15 : 
        #arrow1 = ax.arrow(10.2,0, 4.8 , 1, ls='--')
        #arrow2 = ax.arrow(10.2,0, 4.8 , -1, ls='--' )
        
        uranium2.set_data(10.2,0)
        annotation4.set_position((10.2,0.2))
        annotation4.xy = (10.2,0.2)
        annotation2.set_position((-20,20))
        annotation2.xy = (-20,20)
        
        new_y = Y[i%L]-14
        new_x = X[i%L]
        #Neutron 2
        annotation3.set_position((new_x,new_y))
        annotation3.xy = (new_x,new_y)
        neutron3.set_data(new_x,new_y)
        neutron2.set_data(new_x,-new_y)
        neutron.set_data(new_x,0)
        profission.set_data(15,1)
        profission1.set_data(15,-1)
    else:  
        annotation5.set_position((-10,0))
        annotation5.xy = (-10,0)
        neutron.set_data(new_x,0)
        annotation.set_position((new_x+0.1,0.1))
        annotation.xy = (new_x,0)
        
    print(new_x)
    return neutron, annotation

ani = animation.FuncAnimation(
    fig, update, interval = 15, blit = False)



#ani.save('ani.mp4', fps=60, writer='imagemagick')   

plt.show()
