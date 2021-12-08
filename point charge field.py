# -*- coding: utf-8 -*-
"""
Created on Fri Oct 8 18:25:30 2021

@author: Alex Akinin

Симуляция поля точечных зарядов 

TODO: Починить масштаб вектров векторного поля (вблизи зарядов они очень большие)
"""


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


from matplotlib import pyplot as plt 
import numpy as np


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def create_charge_wall() -> None:
    ''' Функция создания цепочки из зарядов '''
    global charge_list
    for i in range(-50, 50):
        charge_list.append([i, -15, 5])


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def field_vectors(cg_l) -> None:
    '''
    Функция отрисовки поля векторов

    Paramerets
    ----------
    cg_l : list 
        Список ТЗ
    '''
    U_sum, V_sum = 0, 0
    U, V = [], []
    X, Y = np.mgrid[-n:n+1, -n:n+1]
    for i in range(len(cg_l)):
        tmp_X, tmp_Y, tmp_sign = cg_l[i][0], cg_l[i][1], cg_l[i][2]
        X1 = X - tmp_X
        Y1 = Y - tmp_Y
        U.append(tmp_sign * X1/((X1**2 + Y1**2)))
        V.append(tmp_sign * Y1/((X1**2 + Y1**2)))
    U_sum = sum(U)
    V_sum = sum(V)
    fig = plt.figure(facecolor='white')
    ax=fig.gca()
    ax.quiver(X, Y, U_sum, V_sum, edgecolor='k', facecolor='Red', linewidth=.5, alpha=.5)
    plt.show()


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def field_potential(cg_l):
    '''
    Функция отрисовки эквипотенциальных линий

    Paramerets
    ----------
    cg_l : list 
        Список ТЗ
    '''
    Z = []
    Z_sum = 0
    vals = np.linspace(-1, 10, num=100)
    for i in range(len(cg_l)):
        tmp_X, tmp_Y, tmp_sign = cg_l[i][0], cg_l[i][1], cg_l[i][2]
        X1 = X - tmp_X
        Y1 = Y - tmp_Y
        Z.append(tmp_sign / (np.sqrt(X1**2 + Y1**2)))
    Z_sum = sum(Z)
    fig = plt.figure(facecolor='white')
    
    ax1 = fig.add_subplot(1,2,1)
    curves = ax1.contour(X, Y, Z_sum, vals, alpha=0.9)
    # ax1.clabel(curves)
    
    ax2 = fig.add_subplot(1,2,2)
    ax2.contourf(X, Y, Z_sum, vals, alpha=0.9, cmap='jet') 
    plt.show()


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


# Задать сетку 
n = 20
t = np.linspace(-20, 20, num=100);
X, Y = np.meshgrid(t, t);

# Создать ТЗ - координаты и заряд (x, y, q)
charge_list = [[-10, 0, 10], [10, 0, 10]]

# Отрисовка
# create_charge_wall()
# field_vectors(charge_list)
field_potential(charge_list)


