#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:44:55 2022

@author: Locust, The Eater

TASKS
1. LINHA 28 - INSERIR NORMA CENTRO POSICAO DA PARTICULA
2. LINHA 67 - INSERIR CONSTANTE GRAVITACIONAL
3. LINHA 87 - ESCREVER DRAG
4. 
"""

import numpy as np
lista = list()

class particula: #PLACEHOLDER! VERDADEIRA CLASSE NO GABINETE GRANDE!
    
    pass
class mola:
    k = float()
    
    def __init__(self, seed):
        try:
            self.rng = np.random.default_rng(seed)
        except:
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
        forcex = -1*self.kconstanx*distx
        forcey = -1*self.kconstanty*disty
        accx, accy = forcex/part.mass, forcey/part.mass
        vecacc = np.array([accx, accy])
        return vecacc

def gravidade(part1, part2):
    #def vals
    kgrav = float() #TASK 2
    vec1, vec2   = part1.gpos, part2.gpos
    mass1, mass2 = part1.mass, part2.mass
    
    #calcs
    distx        = abs(vec1[0] - vec2[0])
    disty        = abs(vec1[1] - vec2[1])
    forcex       = (mass1*mass2*kgrav)/distx**2
    forcey       = (mass1*mass2*kgrav)/disty**2
    accx1        = forcex/mass1
    accx2        = forcex/mass2
    accy1        = forcey/mass1
    accy2        = forcex/mass2
    vecacc1      = np.array([accx1, accy1])
    vecacc2      = np.array([accx2, accy2])
    
    #return values obtained
    return vecacc1, vecacc2
        
def resist(part1, part2): #TASK 3
    
    pass

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

def norma():
    """
        Serve só como placeholder. A verdadeira norma está no 
        script colisor.py
    """
    pass

def positfixer(particlelist, seed):
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
    try:
        randomseeder = np.random.default_rng(seed)
    except:
        randomseeder = np.random.default_rng(123456)
        
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
            seed = randomseeder.integers(800, 10000)
            particlelist[vec[0]] = particula(seed)
            particlelist[vec[1]] = particula(seed)
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
        positfixer(particlelist, randomseeder.integers(800, 10000)) #Usa número previsivelmente aleatório como próxima tentativa
    
    else:
        print("posições concertadas com sucesso!")
    
    

       
     
    
    
        
    
            
            
            
            
        
        
        
        
        
        
    