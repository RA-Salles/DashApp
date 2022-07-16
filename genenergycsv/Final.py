#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:13:00 2022

@author: locust, The Eater.
"""

"""
Avisos Gerais
1. As posições são pré computadas
2. Colocar o rng como uma variável local causa partículas literalmente iguais 
se você usar seeds.
"""

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


class particula:
    global rng
    rng = np.random.default_rng(seed=85420)
    dt = 0.001
    xposit = float()
    yposit = float()
    xfposit = float()
    yfposit = float()
    xvel = float()
    yvel = float()
    xacc = float()
    yacc = float()
    ptype = int()
    mass = float()
    radius = float()
    charge = float()
    gpos = list()
    gvel = list()
    gpoint = int()

    def __init__(self):
        # try:
        #    self.rng     = np.random.default_rng(seed=seed)
        # except:
        #    self.rng     = np.random.default_rng(seed=85420)
        # self.rng     = np.random.default_rng(seed=85420)
        self.xposit = (90 - (-90)) * rng.random() + (-90)
        self.yposit = (90 - (-90)) * rng.random() + (-90)
        self.xvel = (2 - (-2)) * rng.random() + (-2)
        self.yvel = (2 - (-2)) * rng.random() + (-2)
        self.xacc = (5 - (-5)) * rng.random() + (-5)
        self.yacc = (5 - (-5)) * rng.random() + (-5)
        # self.xacc     = 0
        # self.yacc     = 0
        self.xfposit = self.xposit + self.xvel * self.dt
        self.yfposit = self.yposit + self.yvel * self.dt
        self.ptype = rng.integers(low=1, high=5)
        self.mass = 2 * (float(self.ptype))
        self.radius = (1 - (2)) * rng.random() + (
            2
        )  # Raios massivamente aumentados para garantir ao menos algumas colisões visíveis
        self.charge = (20 - (-20)) * rng.random() + (-20)
        self.gpos = [self.xposit, self.yposit]
        self.gfpos = [self.xfposit, self.yfposit]
        self.gvel = [self.xvel, self.yvel]
        self.gacc = [self.xacc, self.yacc]
        self.ogacc = self.gacc
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
        self.xvel = self.xvel + self.xacc * self.dt
        self.yvel = self.yvel + self.yacc * self.dt
        self.xposit = self.xposit + self.xvel * self.dt
        self.yposit = self.yposit + self.yvel * self.dt
        self.xfposit = self.xposit + self.xvel * self.dt
        self.yfposit = self.yposit + self.yvel * self.dt
        self.gpos = np.array([self.xposit, self.yposit])
        self.gfpos = np.array([self.xfposit, self.yfposit])
        self.gvel = np.array([self.xvel, self.yvel])
        self.updateacc(self.ogacc)
        self.wallcolide()
        self.updategrid()

    def updatexvel(self, k):  # futuramente, será usado para colisões. Esse e o próximo.
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

    def generateparticlelist(somelist, num):  # Gera list com 'num' partículas.
        for i in range(num):
            somelist.append(particula())
        return somelist

    def getparticleposits(particlelist, time):
        xposits = [list() for _ in particlelist]
        yposits = [list() for _ in particlelist]
        updates = int(time / particlelist[0].dt)
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

        self.rng = np.random.default_rng(124237)  # Provenha seed ou morra tentando!
        # self.centerx   = (16 - 15) * self.rng.random() + 15
        # self.centery   = (16 - 15) * self.rng.random() + 15
        self.centerx = 0
        self.centery = 0
        self.konstantx = (30 - 15) * self.rng.random() + 15
        self.konstanty = (30 - 15) * self.rng.random() + 15
        # self.konstantx = (5 - 1) * self.rng.random() + 1
        # self.konstanty = (5 - 1) * self.rng.random() + 1
        # self.konstantx =  self.rng.random()
        # self.konstanty =  self.rng.random()

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

        vec1 = np.array(part.gpos)  # Vetor1 assignado a posicao da particula em 2d
        distx = self.centerx - vec1[0]  # TASK1
        disty = self.centery - vec1[1]  # TASK1
        # forcex = -1*self.konstantx*distx
        # forcey = -1*self.konstanty*disty
        forcex = self.konstantx * distx
        forcey = self.konstanty * disty
        accx, accy = forcex / part.mass, forcey / part.mass
        vecacc = np.array([accx, accy])
        return vecacc


def norma(vec1, vec2):
    vec3 = np.array(vec1) - np.array(vec2)
    dist = np.sqrt(vec3[0] ** 2 + vec3[1] ** 2)
    return dist


def colisor(plist, i, j):
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
    # Constantes Iniciais
    x1, x2 = np.array(plist[i].gfpos), np.array(plist[j].gfpos)
    vel1, vel2 = np.array(plist[i].gvel), np.array(plist[j].gvel)
    mass1, mass2 = plist[i].mass, plist[j].mass
    mass_sum = mass1 + mass2

    # Cálculos em partes
    konst1 = (2 * mass1) / (mass_sum)
    konst2 = (2 * mass2) / (mass_sum)
    dotp1 = np.dot(vel1 - vel2, x1 - x2)
    dotp2 = np.dot(vel2 - vel1, x2 - x1)
    norm1 = norma(x1, x2)
    norm1 = norm1 ** 2
    norm2 = norma(x1, x2)
    norm2 = norm2 ** 2
    diff1 = x1 - x2
    diff2 = x2 - x1

    # Calculo das velocidades finais
    lvel1 = vel1 - konst1 * dotp1 / norm1 * diff1
    lvel2 = vel2 - konst2 * dotp2 / norm2 * diff2

    # Assignação de novos valores às partículas
    print("part1 vel goes from", vel1, "to", lvel1)
    print("part2 vel goes from", vel2, "to", lvel2)
    plist[i].updategvel(lvel1)
    plist[j].updategvel(lvel2)


def distget(x1, x2):
    dist = np.sqrt((x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2)
    return dist


def radiuscheck(
    plist,
):  # verifica se algum par de posits está na dangerzone; guarda partículas em perigo para checagem de colisão
    colparts = (
        list()
    )  # list of already collided particles. Enables ignoring in special conditions
    zetta = -1
    for i in range(len(plist)):
        j = i + 1
        for j in range(len(plist)):
            zetta = zetta + 1
            cdist = plist[i].radius + plist[j].radius
            ctuple1 = (i, j)
            ctuple2 = (j, i)
            if plist[i].gpoint != plist[i].gpoint:  # too far away to ever colide
                colparts.append(ctuple1)
                # colparts[zetta] = tuple1
                colparts.append(ctuple2)
                continue
            if i == j:  # jumps same particle collision
                # print("samepartcol. jumped")
                continue
            if ctuple1 in colparts or ctuple2 in colparts:
                # print("alreadydone. jumped")
                continue
            if (
                distget(plist[i].gfpos, plist[j].gfpos) <= cdist
            ):  # If distance bet. fpositions is
                colparts.append(ctuple1)  # is lesser or equal than sum of
                colparts.append(ctuple2)  # radius, collision is a thing.
                colisor(plist, i, j)
                # print("Collision done! Parts", i, "and", j, "just colided!")
            # else:
            # print("collisionavoided, fetching next pair")


def gravidade(part1, part2):
    # def vals
    kgrav = 6.67430 * 10 ** -11  # TASK 2
    vec1, vec2 = part1.gpos, part2.gpos
    mass1, mass2 = part1.mass, part2.mass

    # calcs
    distx = abs(vec1[0] - vec2[0])
    disty = abs(vec1[1] - vec2[1])
    forcex = (mass1 * mass2 * kgrav) / distx ** 2
    forcey = (mass1 * mass2 * kgrav) / disty ** 2
    accx1 = forcex / mass1
    accx2 = forcex / mass2
    accy1 = forcey / mass1
    accy2 = forcex / mass2
    vecacc1 = np.array([accx1, accy1])
    vecacc2 = np.array([accx2, accy2])

    # return values obtained
    return vecacc1, vecacc2


def gravityman(
    plist,
):  # Para todo par de partículas, calcula interaãço gravitacional. Gera 1 lista para cada partícula
    forces = [list() for particle in plist]
    colparts = list()
    zetta = -1
    for i in range(len(plist)):
        j = i + 1
        for j in range(len(plist)):
            zetta = zetta + 1
            cdist = plist[i].radius + plist[j].radius
            ctuple1 = (i, j)
            ctuple2 = (j, i)
            if plist[i].gpoint != plist[i].gpoint:  # too far away to ever influence gra
                colparts.append(ctuple1)
                # colparts[zetta] = tuple1
                colparts.append(ctuple2)
                continue
            if i == j:  # jumps same particle collision
                # print("samepartcol. jumped")
                continue
            if ctuple1 in colparts or ctuple2 in colparts:
                # print("alreadydone. jumped")
                continue
            if (
                distget(plist[i].gfpos, plist[j].gfpos) <= 10 * cdist
            ):  # If distance between future positions
                forcei, forcej = gravidade(
                    plist[i], plist[j]
                )  # is lesser than this, gravity is suficiently strong(?)
                forces[i].append(forcei)
                forces[j].append(forcej)
                # print("Collision done! Parts", i, "and", j, "just colided!")
            # else:
            # print("collisionavoided, fetching next pair")
    return forces


def eletricidade(
    part1, part2
):  # É literalmente a gravidade reaproveitada. Simplesmente resolve para forças negativas e positivas
    # def vals
    kgrav = 8.987551 * 10 ** 9  # TASK 2
    vec1, vec2 = part1.gpos, part2.gpos
    mass1, mass2 = part1.charge, part2.charge  # AQUI. AQUI É A ÚNICA COISA QUE MUDA!

    # calcs
    distx = abs(vec1[0] - vec2[0])
    disty = abs(vec1[1] - vec2[1])
    forcex = (mass1 * mass2 * kgrav) / distx ** 2
    forcey = (mass1 * mass2 * kgrav) / disty ** 2
    if mass1 > 0 and mass2 > 0:
        accx1 = -forcex / mass1
        accx2 = -forcex / mass2
        accy1 = -forcey / mass1
        accy2 = -forcex / mass2
    else:
        accx1 = forcex / mass1
        accx2 = forcex / mass2
        accy1 = forcey / mass1
        accy2 = forcex / mass2
    vecacc1 = np.array([accx1, accy1])
    vecacc2 = np.array([accx2, accy2])

    # return values obtained
    return vecacc1, vecacc2


def electroman(plist):  # Para todo par de partículas, calcula interação elétrica.
    forces = [list() for particle in plist]
    colparts = list()
    zetta = -1
    for i in range(len(plist)):
        j = i + 1
        for j in range(len(plist)):
            zetta = zetta + 1
            cdist = plist[i].radius + plist[j].radius
            ctuple1 = (i, j)
            ctuple2 = (j, i)
            if plist[i].gpoint != plist[i].gpoint:  # too far away to ever influence gra
                colparts.append(ctuple1)
                # colparts[zetta] = tuple1
                colparts.append(ctuple2)
                continue
            if i == j:  # jumps same particle collision
                # print("samepartcol. jumped")
                continue
            if ctuple1 in colparts or ctuple2 in colparts:
                # print("alreadydone. jumped")
                continue
            if (
                distget(plist[i].gfpos, plist[j].gfpos) <= 10 * cdist
            ):  # If distance bet. fpositions is
                colparts.append(ctuple1)  # is lesser or equal than sum of
                colparts.append(ctuple2)  # radius, collision is a thing.
                forcei, forcej = gravidade(plist[i], plist[j])
                forces[i].append(forcei)
                forces[j].append(forcej)
                # print("Collision done! Parts", i, "and", j, "just colided!")
            # else:
            # print("collisionavoided, fetching next pair")
    return forces


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
    # Inicialização
    incolisionrange = list()
    donechecked = list()
    # try:
    #    randomseeder = np.random.default_rng(seed)
    # except:
    # randomseeder = np.random.default_rng(123456)

    # Check inicial
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

    # Se houver partículas em colisão, ele rerrola elas
    if len(incolisionrange) > 0:
        for vec in incolisionrange:
            # seed = randomseeder.integers(800, 10000)
            particlelist[vec[0]] = particula()
            particlelist[vec[1]] = particula()
    # Clean up!
    incolisionrange.clear()
    donechecked.clear()

    # Check final
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

    if len(incolisionrange) > 0:  # Não funcionou? TRY TRY AGAIN!
        print("Particulas insatisfatorias detectadas. Tentando novamente.")
        positfixer(particlelist)

    else:
        print("posições concertadas com sucesso!")


def forcesum(forcelist):
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
    resultvec = np.array([0, 0])
    i = 0
    for forcevec in forcelist:
        i = i + 1
        # print("force", i, ":", forcevec) #verbose. For debugging purposes :D
        resultvec = resultvec + np.array(forcevec)
    # print("Totalforce:", resultvec)
    return resultvec


def resist(
    part, rand
):  # ALTERADO PARA UMA ÚNICA PARTÍCULA! DRAG AGE SOB UMA PARTÍCULA POR VEZ, QUE NEM A MOLA!
    velx = part.xvel
    vely = part.yvel
    mass = part.mass
    konstantx = (0.1 - (1)) * rand.random() + 1
    konstanty = (0.1 - (1)) * rand.random() + 1

    if velx > 0:
        forcex = konstantx * velx ** 2
        accx = -1 * forcex / mass
    else:
        forcex = konstantx * velx ** 2
        accx = forcex / mass

    if vely > 0:
        forcey = konstanty * vely ** 2
        accy = -1 * forcey / mass
    else:
        forcey = konstanty * vely ** 2
        accy = forcey / mass
    vecacc = np.array([accx, accy])
    # print("resistforce:", vecacc)
    return vecacc


def energyget(plist):
    energy = float()
    for particle in plist:
        scalarvel = np.dot(particle.xvel, particle.yvel)
        energy = energy + abs(1 / 2 * particle.mass * scalarvel ** 2)
    return energy


rand = np.random.default_rng(123456)

print(
    "Escolha tipo de simulação: \n\
      1. Elétrica\n\
      2. Atrativa/Gravitacional\n\
      3. Restauradora\n\
      4. Resistência\n"
)
try:
    tipodesimulacao = int(input())
except:
    print("Valor inválido!")
    quit()
print(
    "Escolha o tipo de output:\n",
    "1. Particulas no tempo\n",
    "2. Energia Cinética no tempo\n",
)
if __name__ == "__main__":
    try:
        tipodegrafico = int(input())
    except:
        print("Valor inválido!")
        quit()


if tipodesimulacao == 4:

    def getparticleposits(particlelist, time, umamola):
        xposits = [list() for _ in particlelist]
        yposits = [list() for _ in particlelist]
        energyintime = [[], []]
        updates = int(time / particlelist[0].dt)
        for i in range(0, updates):
            energyintime[0].append(energyget(particlelist))
            energyintime[1].append(i)
            # gravitationforces = list()
            zetta = -1
            print("running for timeframe", i)
            radiuscheck(particlelist)
            # gravitationforces = gravityman(particlelist)
            # electroforces     = electroman(particlelist)
            for particle in particlelist:
                zetta = zetta + 1
                xposits[zetta].append(particle.xposit)
                yposits[zetta].append(particle.yposit)
                allforce = list()
                allforce.append(resist(particle, rand))
                # for item in electroforces[zetta]:
                #    allforce.append(item)
                # allforce.append(umamola.restaurador(particle))
                allforce.append(particle.gacc)
                particle.updateacc(forcesum(allforce))  # :)
                particle.updatecondition()
        return xposits, yposits, energyintime


elif tipodesimulacao == 3:

    def getparticleposits(particlelist, time, umamola):
        xposits = [list() for _ in particlelist]
        yposits = [list() for _ in particlelist]
        energyintime = [[], []]
        updates = int(time / particlelist[0].dt)
        for i in range(0, updates):
            energyintime[0].append(energyget(particlelist))
            energyintime[1].append(i)
            # gravitationforces = list()
            zetta = -1
            print("running for timeframe", i)
            radiuscheck(particlelist)
            # gravitationforces = gravityman(particlelist)
            # electroforces     = electroman(particlelist)
            for particle in particlelist:
                zetta = zetta + 1
                xposits[zetta].append(particle.xposit)
                yposits[zetta].append(particle.yposit)
                allforce = list()
                # allforce.append(resist(particle, rand))
                # for item in electroforces[zetta]:
                #    allforce.append(item)
                allforce.append(umamola.restaurador(particle))
                allforce.append(
                    particle.gacc
                )  # NAO TIRAR DO COMENTARIO. GERA FORÇA PERPETUA E CRESCENTE; VELOCIDADES ILEGÍVEIS ABSURDAS! Dor!
                particle.updateacc(forcesum(allforce))  # :)
                particle.updatecondition()
        return xposits, yposits, energyintime


elif tipodesimulacao == 2:

    def getparticleposits(particlelist, time, umamola):
        xposits = [list() for _ in particlelist]
        yposits = [list() for _ in particlelist]
        energyintime = [[], []]
        updates = int(time / particlelist[0].dt)
        for i in range(0, updates):
            energyintime[0].append(energyget(particlelist))
            energyintime[1].append(i)
            gravitationforces = list()
            zetta = -1
            print("running for timeframe", i)
            radiuscheck(particlelist)
            gravitationforces = gravityman(particlelist)
            # electroforces     = electroman(particlelist)
            for particle in particlelist:
                zetta = zetta + 1
                xposits[zetta].append(particle.xposit)
                yposits[zetta].append(particle.yposit)
                allforce = gravitationforces[zetta]
                # allforce.append(resist(particle, rand))
                # for item in electroforces[zetta]:
                #    allforce.append(item)
                # allforce.append(umamola.restaurador(particle))
                allforce.append(particle.gacc)  # NAO TIRAR DO COMENTARIO. GERA FORÇA PERPETUA E CRESCENTE; VELOCIDADES ILEGÍVEIS ABSURDAS! Dor!
                particle.updateacc(forcesum(allforce))  # :)
                particle.updatecondition()
        return xposits, yposits, energyintime


elif tipodesimulacao == 1:

    def getparticleposits(particlelist, time, umamola):
        xposits = [list() for _ in particlelist]
        yposits = [list() for _ in particlelist]
        energyintime = [[], []]
        updates = int(time / particlelist[0].dt)
        for i in range(0, updates):
            energyintime[0].append(energyget(particlelist))
            energyintime[1].append(i)
            # gravitationforces = list()
            zetta = -1
            print("running for timeframe", i)
            radiuscheck(particlelist)
            # gravitationforces = gravityman(particlelist)
            electroforces = electroman(particlelist)
            for particle in particlelist:
                zetta = zetta + 1
                xposits[zetta].append(particle.xposit)
                yposits[zetta].append(particle.yposit)
                allforce = electroforces[zetta]
                # allforce.append(resist(particle, rand))
                #for item in electroforces[zetta]:
                #    allforce.append(item)
                # allforce.append(umamola.restaurador(particle))
                allforce.append(
                    particle.gacc
                )  # NAO TIRAR DO COMENTARIO. GERA FORÇA PERPETUA E CRESCENTE; VELOCIDADES ILEGÍVEIS ABSURDAS! Dor!
                particle.updateacc(forcesum(allforce))  # :)
                particle.updatecondition()
        return xposits, yposits, energyintime


if __name__ == "__main__":
    if tipodegrafico == 1:
        print("Insira número de partículas desejado\n")
        try:
            numparticles = int(input())
        except:
            print("valor inválido!")
            quit()
        centromola = mola()
        # numparticles = 10
        particlelist = list()
        for i in range(numparticles):
            particlelist.append(particula())

        positfixer(particlelist)

        print("Insira tempo de rodagem desejado\n")
        try:
            runtime = int(input())
        except:
            print("valor inválido!")
            quit()
        # runtime = 20
        # dt = 0.001
        dt = 0.001
        fig = plt.figure()
        ax = fig.add_subplot()

        xdata, ydata, kinetic = getparticleposits(particlelist, runtime, centromola)

        def update(i, xposits, yposits):
            ax.clear()
            xintime = list()
            yintime = list()
            for xposit, yposit in zip(
                xposits, yposits
            ):  # goes through lines and particles
                xintime.append(xposit[i])  # Contem posições para tempo determinado
                yintime.append(yposit[i])
            ax.set(xlim=(-100, 100))
            ax.set(ylim=(-100, 100))
            # for i in range(len(xintime)): #Para colorir por tipo, adaptar essa parte da função para detectar tipo.
            #    ax.scatter(xintime[i], yintime[i], s = 20.0)
            ax.scatter(xintime, yintime, s=30)
            # xintime.clear()
            # yintime.clear()

        # anim = FuncAnimation (fig, update, frames= range(1, int(20/dt), 200), fargs = (scatter, ydata, xdata), interval = 1, blit=True)
        anim = FuncAnimation(
            fig,
            update,
            frames=range(1, int(runtime / dt), 100),
            fargs=(xdata, ydata),
            interval=1,
            blit=False,
        )
        plt.show()
        print("Você gostaria de salvar essa animação?\n", "1. Sim!\n", "2. Não!")
        try:
            decis = int(input())
        except:
            print("valor inválido!")
            quit()
        if decis == 1:
            nome = input("Insira o nome para o gif: ")
            anim.save(nome, writer="imagemagick")
    else:
        print("Insira número de partículas desejado\n")
        try:
            numparticles = int(input())
        except:
            print("valor inválido!")
            quit()
        centromola = mola()
        # numparticles = 10
        particlelist = list()
        for i in range(numparticles):
            particlelist.append(particula())

        positfixer(particlelist)

        print("Insira tempo de rodagem desejado\n")
        try:
            runtime = int(input())
        except:
            print("valor inválido!")
            quit()
        # runtime = 20
        # dt = 0.001
        dt = 0.001
        fig = plt.figure()
        ax = fig.add_subplot()

        xdata, ydata, kinetic = getparticleposits(particlelist, runtime, centromola)

        ax.plot(kinetic[1], kinetic[0])
        plt.show()

else:
    import pandas as pd
    numparticles = 20
    centromola = mola()
    particlelist = list()
    for i in range(numparticles):
        particlelist.append(particula())
    positfixer(particlelist)
    runtime = 20
    dt = 0.001
    fig = plt.figure()
    ax = fig.add_subplot()
    xdata, ydata, kinetic = getparticleposits(particlelist, runtime, centromola)
    pddict = {'energydata': kinetic[0],'timeframe':kinetic[1]}
    print("selectnameforcsv: ")
    name = input()
    df = pd.DataFrame(pddict)
    df.to_csv(name)
    
    
