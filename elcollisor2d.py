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
    gpos    = list()
    gvel    = list()
    gpoint  = int()
    
    def __init__(self):
        #try:
        #    self.rng     = np.random.default_rng(seed=seed)
        #except:
        #    self.rng     = np.random.default_rng(seed=85420)
        #self.rng     = np.random.default_rng(seed=85420)
        self.xposit   = (21 - (-20)) * rng.random() + (-20)
        self.yposit   = (21 - (-20)) * rng.random() + (-20)
        self.xvel     = (2 - (-2)) * rng.random() + (-2)
        self.yvel     = (2 - (-2)) * rng.random() + (-2)
        self.xacc     = (5 - (-5)) * rng.random() + (-5)
        self.yacc     = (5 - (-5)) * rng.random() + (-5)
        self.xfposit  = self.xposit + self.xvel * self.dt
        self.yfposit  = self.yposit + self.yvel * self.dt
        self.ptype    = rng.integers(low = 1, high = 5)
        self.mass     = float(self.ptype)
        self.radius   = (1 - (0.5)) * rng.random() + (0.5)
        self.gpos     = [self.xposit, self.yposit]
        self.gfpos    = [self.xfposit, self.yfposit]
        self.gvel     = [self.xvel, self.yvel]
        self.gacc     = [self.xacc, self.yacc]
        self.updategrid()
        
    def updategrid(self):
        if self.xposit > 0 and self.yposit > 0:
            self.gpoint = 1
        if self.xposit < 0 and self.yposit > 0:
            self.gpoint = 2
        if self.xposit < 0 and self.yposit < 0:
            self.gpoint = 3
        if self.xposit > 0 and self.yposit < 0:
            self.gpoint = 4
    
    def wallcolide(self):
        if self.xfposit >= 100 or self.xfposit <= -100:
            self.xvel = -self.xvel
        if self.yfposit >= 100 or self.yfposit <= -100:
            self.yvel = -self.yvel
            
    def updatecondition(self):
        self.xposit  = self.xposit + self.xvel * self.dt
        self.yposit  = self.yposit + self.yvel * self.dt
        self.xfposit = self.xposit + self.xvel * self.dt
        self.yfposit = self.yposit + self.yvel * self.dt 
        self.xvel    = self.xvel + self.xacc * self.dt
        self.yvel    = self.yvel + self.yacc * self.dt
        self.gpos    = np.array([self.xposit, self.yposit])
        self.gfpos   = np.array([self.xfposit, self.yfposit])
        self.gvel    = np.array([self.xvel, self.yvel])
        self.wallcolide()
        self.updategrid()

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

class mola:
    k = float()
    
    def __init__(self):
        
        self.rng   = np.random.default_rng(124237) # Provenha seed ou morra tentando!
        self.centerx   = (16 - 15) * self.rng.random() + 15
        self.centery   = (16 - 15) * self.rng.random() + 15
        self.konstantx = (30 - 15) * self.rng.random() + 15
        self.konstanty = (30 - 15) * self.rng.random() + 15
        
        
    def restaurador(self, part):
        """
        Função restaurador: 
            Calcula influência da força restauradora
            da 'mola' sob uma partícula. 
        
            *Funcionamento*
                Utilizando as constantes geradas pelo rng, calcula
                segundo a lei de hooke a força gerada. Faz isso 
                separadamente por vetor. Posteriormente, une variáveis
                a vetor único, que é retornado.
            *Uso*
                Após obter o retorno do vetor de influência, basta
                somar a aceleração do dado instante à aceleração da partícula
                no dado momento, o que simula toscamente a soma das forças
                gerando uma dada força resultante. A maneira correta, todavia,
                é gerar uma função para calcular a soma das forças atuando
                na partícula para então descobrir a resultante. Do contrá-
                rio, é possível que partícula gradativamente salte distân-
                cias progressivamente mais distantes da mola.
                
        """
        
        vec1 = np.array(part.gpos) #Vetor1 assignado a posicao da particula em 2d
        distx = self.centerx - vec1[0]            #TASK1
        disty = self.centery - vec1[1]            #TASK1
        forcex = -1*self.konstantx*distx
        forcey = -1*self.konstanty*disty
        accx, accy = forcex/part.mass, forcey/part.mass
        vecacc = np.array([accx, accy])
        return vecacc
    
def norma(vec1, vec2):
    vec3 = np.array(vec1) - np.array(vec2)
    dist = np.sqrt(vec3[0]**2 + vec3[1]**2)
    return dist

def colisor(part1, part2):
    """
    Parameters
    ----------
    part1 : classe tipo particula.
    part2 : "
    
    Vars
    ---------
    x1 e 2 - representam posição bidimensional do particulado
    vel1 e 2 - representam velocidade vetorial do particulado
    mass1 e 2 - massa
    demais - variáveis temporárias para cálculo
    
    Returns
    -------
    Nada. Apenas seta velocidades de forma bruta. Não recalcula 
    velocidades, porém. Isso deve ser feito manualmente depois.

    """
    #Constantes Iniciais
    x1, x2       = np.array(part1.gfpos), np.array(part2.gfpos)
    vel1, vel2   = np.array(part1.gvel) , np.array(part2.gvel)
    mass1, mass2 = part1.mass , part2.mass
    mass_sum     = mass1 + mass2
    
    #Cálculos em partes
    konst1 = (2*mass1)/(mass_sum)
    konst2 = (2*mass2)/(mass_sum)
    dotp1  = np.dot(vel1 - vel2, x1 - x2)
    dotp2  = np.dot(vel2 - vel1, x2 - x1)
    norm1  = norma(x1, x2)
    norm1  = norm1**2
    norm2  = norma(x1, x2)
    norm2  = norm2**2
    diff1  = x1 - x2
    diff2  = x2 - x1
    
    #Calculo das velocidades finais
    lvel1 = vel1 - konst1*dotp1/norm1*diff1 
    lvel2 = vel2 - konst2*dotp2/norm2*diff2
    
    #Assignação de novos valores às partículas
    part1.vel1 = lvel1
    part2.vel2 = lvel2
        
def distget(x1, x2):
    dist = np.sqrt((x1[0] - x2[0])**2 + (x1[1] - x2[1])**2)
    return dist

def radiuscheck(plist): #verifica se algum par de posits está na dangerzone; guarda partículas em perigo para checagem de colisão
    colparts = list() #list of already collided particles. Enables ignoring in special conditions
    zetta = -1
    for i in range(len(plist)):
        j = i + 1
        for j in range(len(plist)):
            zetta = zetta + 1
            cdist   = plist[i].radius + plist[j].radius
            ctuple1 = (i, j)
            ctuple2 = (j, i)
            if plist[i].gpoint != plist[i].gpoint: #too far away to ever colide
                colparts.append(ctuple1)
                #colparts[zetta] = tuple1
                colparts.append(ctuple2)
                continue
            if i == j: #jumps same particle collision
                #print("samepartcol. jumped")
                continue
            if ctuple1 in colparts or ctuple2 in colparts:
                #print("alreadydone. jumped")
                continue
            if distget(plist[i].gfpos, plist[j].gfpos) <= cdist: #If distance bet. fpositions is 
                colparts.append(ctuple1)                         #is lesser or equal than sum of  
                colparts.append(ctuple2)                         #radius, collision is a thing.
                colisor(plist[i], plist[j])  
                #print("Collision done! Parts", i, "and", j, "just colided!")
            #else:
                #print("collisionavoided, fetching next pair")

def positfixer(particlelist):
    """
    POSITFIXER! A solução para todas as suas partículas criadas
    perto demais!
    
    Funcionamento: 
        Roda por todas as partículas procurando quem 
    nasceu perto demais. Ao detectar particulas próximas
    o suficiente para colidir, refaz elas. Feito para rodar
    até as partículas estarem em posição satisfatória. 
    
    """
    #Inicialização
    incolisionrange = list()
    donechecked     = list()
    #try:
    #    randomseeder = np.random.default_rng(seed)
    #except:
    #randomseeder = np.random.default_rng(123456)
        
    #Check inicial
    for i in range(len(particlelist)):
        for j in range(len(particlelist)):
            if [i, j] or [j, i] in donechecked or j == i: 
                continue
            coldist = particlelist[i].radius + particlelist[j].radius
            actdist = norma(particlelist[i].gpos + particlelist[j].gpos)
            if actdist <= coldist:
                incolisionrange.append([i, j])
            donechecked.append([i, j])
            donechecked.append([j, i])
            
    #Se houver partículas em colisão, ele rerrola elas
    if len(incolisionrange) > 0:
        for vec in incolisionrange:
            #seed = randomseeder.integers(800, 10000)
            particlelist[vec[0]] = particula()
            particlelist[vec[1]] = particula()
    #Clean up!
    incolisionrange.clear()
    donechecked.clear()
    
    #Check final
    for i in range(len(particlelist)):
        for j in range(len(particlelist)):
            if [i, j] or [j, i] in donechecked or j == i: 
                continue
            coldist = particlelist[i].radius + particlelist[j].radius
            actdist = norma(particlelist[i].gpos + particlelist[j].gpos)
            if actdist <= coldist:
                incolisionrange.append([i, j])
            donechecked.append([i, j])
            donechecked.append([j, i])
            
    if len(incolisionrange) > 0: #Não funcionou? TRY TRY AGAIN!
        print("Particulas insatisfatorias detectadas. Tentando novamente.")
        positfixer(particlelist)
    
    else:
        print("posições concertadas com sucesso!")

def forcesum(*args): 
    """
    Parameters
    ----------
    *args : vetores. Numpy array ou lista. Será transformado em array de qualquer forma.
        forças vetoriais a serem somadas.

    Returns
    -------
    resultvec : Numpy Array
        Vetor Resultante.
    """
    resultvec = np.array([])
    for forcevec in args:
        resultvec = resultvec + np.array(forcevec)
    return resultvec

def getparticleposits(particlelist, time, umamola):
    xposits = [list() for _ in particlelist]
    yposits = [list() for _ in particlelist]
    updates = int(time/particlelist[0].dt)
    for i in range(0, updates):
        zetta = -1
        print("running for timeframe", i)
        for particle in particlelist:
            #print("running for timeframe", i)
            zetta = zetta + 1
            xposits[zetta].append(particle.xposit)
            yposits[zetta].append(particle.yposit)
            radiuscheck(particlelist)                       #checa colisões
            restauringforce = umamola.restaurador(particle) #checa elasticidade de centro
            particle.updateacc(
                forcesum(particle.gacc,
                         restauringforce
                         )
                )
            particle.updatecondition()
    return xposits, yposits

centromola = mola()
numparticles = 5
particlelist = list()
for i in range(numparticles):
    particlelist.append(particula())

positfixer(particlelist)

runtime = 20
#dt = 0.001
dt = 0.001
fig = plt.figure()
ax = fig.add_subplot()


xdata, ydata = getparticleposits(particlelist, runtime, centromola)

def update(i, xposits, yposits):
    ax.clear()
    xintime = list()
    yintime = list()
    for xposit, yposit in zip(xposits, yposits):  #goes through lines and particles
          xintime.append(xposit[i]) # Contem posições para tempo determinado
          yintime.append(yposit[i])
    ax.set(xlim=(-100, 100))                                 
    ax.set(ylim=(-100, 100))
    #for i in range(len(xintime)): #Para colorir por tipo, adaptar essa parte da função para detectar tipo.
    #    ax.scatter(xintime[i], yintime[i])
    ax.scatter(xintime, yintime)
    #xintime.clear()
    #yintime.clear()
    

    
#anim = FuncAnimation (fig, update, frames= range(1, int(20/dt), 200), fargs = (scatter, ydata, xdata), interval = 1, blit=True)
anim = FuncAnimation (fig, update, frames = range(1, int(runtime/dt), 200), fargs = (xdata, ydata), interval = 1, blit=False)
plt.show()
