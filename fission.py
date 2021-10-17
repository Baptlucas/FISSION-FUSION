# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:39:17 2021

@author: Baptiste
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
xlim_sup = 20
ax.set_xlim([5,xlim_sup])
ax.set_ylim([-10,10])

L = 600

theta = np.linspace(0,25,L)
theta2 = np.linspace(0,25,L)

x = theta
y = 0
Y = theta2
X = theta2
neutronsize = 4
urasize = 14
neutron, = ax.plot(0,0, 'ko', markersize = neutronsize)
neutron2, = ax.plot(-10,0, 'ko', markersize = neutronsize)
neutron3, = ax.plot(-10,0, 'ko', markersize = neutronsize)
uranium, = ax.plot(10,0, 'go', markersize = urasize)
uranium2, = ax.plot(-10.2,-10, 'ro', markersize = urasize)

profission, = ax.plot(-10,0, 'ro', markersize = urasize/2)
profission1, = ax.plot(-10,0, 'ro', markersize = urasize/2)
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
annotation6 = ax.annotate("Produits de fission", xy=(-9, 0), xytext=(-14.5, 0),
            arrowprops=dict(arrowstyle="->"))

annotation7 = ax.annotate("", xy=(-9.9, 0), xytext=(-14.5, 0),
            arrowprops=dict(arrowstyle="fancy"))
annotation8 = ax.annotate("", xy=(-9.9, 0), xytext=(-14.5, 0),
                          arrowprops=dict(arrowstyle="fancy"))
        
annotation9 = ax.annotate("", xy=(-9.9, 0), xytext=(-14.5, 0),
                          arrowprops=dict(arrowstyle="fancy"))
            
annotation10 = ax.annotate("", xy=(-9.9, 0), xytext=(-14.5, 0),
                           arrowprops=dict(arrowstyle="fancy"))

annotation11 = ax.annotate("Energie", xy=(-9.9, 0), xytext=(-14.5, 0))
                                  
def update(i):
    
    uranium.set_data(10.2,0)
    uranium2.set_data(-10.2,0)
    
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
        annotation4.set_position((10,0.5))
        annotation4.xy = (10,0.5)
        
        annotation2.set_position((-20,20))
        annotation2.xy = (-20,20)
        
        if 10.5< new_x < 15:
            annotation5.set_position((10.5,0))
            annotation5.xy = (new_x,0)
        
       
    elif  new_x >= 15 : 
        #arrow1 = ax.arrow(10.2,0, 4.8 , 1, ls='--')
        #arrow2 = ax.arrow(10.2,0, 4.8 , -1, ls='--' )
        
        uranium2.set_data(10.2,0)        
        new_y = Y[i%L]-14
        new_x = x[i%L]
        #Neutron 2
        annotation3.set_position((new_x,new_y))
        annotation3.xy = (new_x,new_y)
        neutron3.set_data(new_x,new_y)
        neutron2.set_data(new_x,-new_y)
        neutron.set_data(new_x,0)
        profission.set_data(15,1)
        profission1.set_data(15,-1)
        
        annotation6.set_position((13,5))
        annotation6.xy = (15,1)
        
        annotation7.set_position((14,1))
        annotation7.xy = (12.5,2.5)
        
        annotation8.set_position((14,-1))
        annotation8.xy = (12.5,-2.5)
        
        annotation9.set_position((16,1))
        annotation9.xy = (17.5,2.5)
        
        annotation10.set_position((16,-1))
        annotation10.xy = (17.5,-2.5)
        
        annotation11.set_position((12.5,-3.2))
        annotation11.xy = (12.5,-2.5)
    else:  
        ax.set_xlim(5, xlim_sup)
        ax.set_ylim(-10, 10)
        annotation5.set_position((-10,0))
        annotation5.xy = (-10,0)
        neutron.set_data(new_x,0)
        
        annotation.set_position((new_x,-0.9))
        annotation.xy = (new_x,0)
        
        annotation4.set_position((-20,20))
        annotation4.xy = (-20,20)
        
        annotation2.set_position((10,0.5))   
        annotation2.xy = (10,0.5)
        
        annotation6.set_position((-12,5))
        annotation6.xy = (-15,1)
        
        annotation7.set_position((-10.5,3))
        annotation7.xy = (-14,1)
        
        annotation8.set_position((-12,-3))
        annotation8.xy = (-14,-1)
        
        annotation9.set_position((-18,3))
        annotation9.xy = (-16,1)
        
        annotation10.set_position((-18,-3))
        annotation10.xy = (-16,-1)
        
        annotation11.set_position((-11.5,-2.5))
        annotation11.xy = (-12.5,-2.5)
    return neutron, annotation

ani = animation.FuncAnimation(
    fig, update, interval = 15, blit = False)



#ani.save('ani.mp4', fps=60, writer='imagemagick')   

plt.show()



"""   
    elif new_x > xlim_sup  :
        uranium2.set_data(10.2,0)
        ax.set_xlim(5, 50)
        ax.set_ylim(-20, 20)
        new_y = Y[i%L]-14
        new_x = X[i%L]
        annotation3.set_position((new_x,new_y))
        annotation3.xy = (new_x,new_y)
        neutron3.set_data(new_x,new_y)
        neutron2.set_data(new_x,-new_y)
        neutron.set_data(new_x,0)
        profission.set_data(15,1)
        profission1.set_data(15,-1)"""
