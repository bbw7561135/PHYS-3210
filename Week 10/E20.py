#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:56:21 2019

@author: amandaash
"""

import numpy as np
import matplotlib.pyplot as plt

def harmonic_oscillator(p,k,v0,x0,m,time_step,t0,tf):
    v = v0
    x = x0
    x_val = []
    v_val = []
    time_array = np.arange(t0,tf, time_step)

    for n in time_array:
        #first Euler's method to find half step:
        x_half = x + (time_step/2)*v
        v_half = v + ((time_step/2)*(-k/m)*x**(p-1))
        
        vf = v + ((time_step)/m)*(-k*x_half**(p-1))
        xf = x + (time_step)*v_half
        
        x_val.append(x)
        v_val.append(v)
        
        x = xf
        v = vf
    
    return x_val, v_val, time_array

#P_val = np.arange(2, 8,2)
P_val = np.array([2,6,10])
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)

for P in P_val:
    
    x,v,t = harmonic_oscillator(P,10,0,1,1,0.0001,0,10)
    ax1.plot(x,t, label = 'P = {0}'.format(P))
    ax2.plot(v,t, label = 'P = {0}'.format(P))

ax1.legend()
ax1.set_xlabel('distance')
ax1.set_ylabel('time')
fig1.show()

ax2.legend()
ax2.set_xlabel('velocity')
ax2.set_ylabel('time')
fig2.show()



    