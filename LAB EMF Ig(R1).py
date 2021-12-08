# -*- coding: utf-8 -*-
"""
Created on Fri Oct 8 18:25:30 2021

@author: Alex Akinin

Симуляция тока Ig через НГ из лабы ЭДС
"""


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


E, R, r, Ex = 9, 11111, 600, 1

R1 = np.linspace(0, 11111, 1111000)
Ig = np.array([])

EXPR1 = lambda x: (E*x - Ex*R)/(r*R + x*(R-x))

Ig = EXPR1(R1)


plt.plot(R1, Ig)

# косметические дополнения на графике
plt.yscale('linear')
plt.ylabel('Ig')
plt.xlabel('R1')
plt.grid(True)
plt.axhline(0, color=(0,0,0))
plt.axvline(0, color=(0,0,0))