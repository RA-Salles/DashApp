#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 08:17:55 2022

@author: locust
"""
import numpy as np

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
    
    
    






































