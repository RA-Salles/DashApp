# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:23:40 2022

@author: Locust (R. Salles), without other known aliases
"""
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class particula:
    global rng
    rng     = np.random.default_rng(seed=85420)
    dt      = 0.001
    xposit  = float()
    yposit  = float()
    xfposit = float()
    yfposit = float()
    xvel    = float()
    yvel    = float()
    xacc    = float()
    yacc    = float()
    ptype   = int()
    mass    = float()
    radius  = float()
    
    def __init__(self):
        self.xposit   = (21 - (-20)) * rng.random() + (-20)
        self.yposit   = (21 - (-20)) * rng.random() + (-20)
        self.xvel     = (2 - (-2)) * rng.random() + (-2)
        self.yvel     = (2 - (-2)) * rng.random() + (-2)
        self.xacc     = (1 - (-1)) * rng.random() + (-1)
        self.yacc     = (1 - (-1)) * rng.random() + (-1)
        self.xfposit  = self.xposit + self.xvel * self.dt
        self.yfposit  = self.yposit + self.yvel * self.dt
        self.ptype    = rng.integers(low = 1, high = 5)
        self.mass     = float(self.ptype)
        self.radius   = (0.5 - (0.1)) * rng.random() + (0.1)
    
    def updatecondition(self):
        self.xposit  = self.xposit + self.xvel * self.dt
        self.yposit  = self.yposit + self.yvel * self.dt
        self.xfposit = self.xposit + self.xvel * self.dt
        self.yfposit = self.yposit + self.yvel * self.dt 
        self.xvel    = self.xvel + self.xacc * self.dt
        self.yvel    = self.yvel + self.yacc * self.dt
        
    def updatexvel(self, k): #futuramente, será usado para colisões. Esse e o próximo.
        self.xvel = k
        
    def updateyvel(self, k):
        self.yvel = k
        
    def generateparticlelist(somelist, num): #Gera list com 'num' partículas. 
        for i in range(num):
            somelist.append(particula())
        return somelist
    
    def getparticleposits(particlelist, time):
        xposits = [list() for _ in particlelist]
        yposits = [list() for _ in particlelist]
        updates = int(time/particlelist[0].dt)
        for i in range(0, updates):
            zetta = -1
            for particle in particlelist:
                zetta = zetta + 1
                xposits[zetta].append(particle.xposit)
                yposits[zetta].append(particle.yposit)
                particle.updatecondition()
        return xposits, yposits

def getparticleposits(particlelist, time):
    xposits = [list() for _ in particlelist]
    yposits = [list() for _ in particlelist]
    updates = int(time/particlelist[0].dt)
    for i in range(0, updates):
        zetta = -1
        for particle in particlelist:
            zetta = zetta + 1
            xposits[zetta].append(particle.xposit)
            yposits[zetta].append(particle.yposit)
            particle.updatecondition()
    return xposits, yposits
        
particlelist = list()
for i in range(20):
    particlelist.append(particula())

runtime = 20
dt = 0.001
fig = plt.figure()
ax = fig.add_subplot()
ax.set(xlim=(-100, 100))                                 #*seta limites do gráfico.
ax.set(ylim=(-100, 100))
lines = [ax.plot([],[])[0] for particle in particlelist]

xdata, ydata = getparticleposits(particlelist, runtime)

def update(i, lines, xposits, yposits):
    for line, xposit, yposit in zip(lines, xposits, yposits):  #goes through lines and particles
        #line.clear()
        line.set_data(xposit[:i],yposit[:i], linewidth=5)       
                  
    return lines

anim = FuncAnimation (fig, update, frames= range(1, int(20/dt), 200), fargs = (lines, ydata, xdata), interval = 1, blit=True)
#anim = FuncAnimation (fig, update, frames= range(1, int(20/dt), 200), fargs = (lines, ydata, xdata), interval = 1)
plt.show()
anim.save('particlemove.gif', writer='imagemagick')



