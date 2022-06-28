# -*- coding: utf-8 -*-
"""
Created on Sat May 28 09:45:43 2022

@author: Locust
"""

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

class particula:
    global rng
    #rng     = np.random.default_rng(seed=85420)
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
    gpos    = list()
    gvel    = list()
    
    def __init__(self, seed):
        try:
            self.rng     = np.random.default_rng(seed=seed)
        except:
            self.rng     = np.random.default_rng(seed=85420)
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
        self.gpos     = [self.xposit, self.yposit]
        self.gfpos    = [self.fxposit, self.fyposit]
        self.gvel     = [self.xvel, self.yvel]
        self.gacc     = [self.xacc, self.yacc]
    
    def updatecondition(self):
        self.xposit  = self.xposit + self.xvel * self.dt
        self.yposit  = self.yposit + self.yvel * self.dt
        self.xfposit = self.xposit + self.xvel * self.dt
        self.yfposit = self.yposit + self.yvel * self.dt 
        self.xvel    = self.xvel + self.xacc * self.dt
        self.yvel    = self.yvel + self.yacc * self.dt
        self.gpos    = np.array([xposit, yposit])
        self.gfpos   = [self.fxposit, self.fyposit]
        self.gvel    = np.array([xvel, yvel])

    def updatexvel(self, k): #futuramente, será usado para colisões. Esse e o próximo.
        self.xvel = k
        
    def updateyvel(self, k):
        self.yvel = k
  
    def updategvel(self, tdvel):
        self.gvel = np.array(tdvel)
        self.xvel = tdvel[0]
        self.yvel = tdvel[1]
    
    def updateacc(self, tdacc):
        self.gacc = tdacc
        self.xacc = tdacc[0]
        self.yacc = tdacc[1]
        
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
    
    def collision(particle1, particle2):
        masses = particle1.mass + particle2.mass
        return True
        pass
def distget(x1, x2):
    dist = np.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)
    return dist

def radiuscheck(plist): #verifica se algum par de posits está na dangerzone; guarda partículas em perigo para checagem de colisão
    colparts = list() #list of already collided particles. Enables ignoring in special conditions
    for i in range(plist):
        for j in range(plist):
            cdist   = plist[i].radius + plist[j].radius
            ctuple1 = (i, j)
            ctuple2 = (j, i)
            if i == j: #jumps same particle collision
                print("samepartcol. jumped")
                continue
            if ctuple1 in colparts or ctuple2 in colparts:
                print("alreadydone. jumped")
                continue
            if distget(plist[i].gfpos, plist[j].gfpos) <= cdist: #If distance bet. fpositions is 
                
                colparts.append(ctuple1)                         #is lesser or equal than sum of  
                colparts.append(ctuple2)                         #radius, collision is a thing.
                
            else:
                print("collisionavoided, fetching next pair")

def collisionman(particle1, particle2):
    