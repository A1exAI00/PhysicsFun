# -*- coding: utf-8 -*-
"""
Created on ---UNKNOWN---

@author: Alex Akinin

Симуляция колебаний в ЛАБЕ 'Разряд в неоновой лампе'
Слегка ❌НЕ СХОДИТСЯ❌ с опытом
"""


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def neon_lamp_oscillation(E_loc=None, R_loc=None, C_loc=None, show=False):
    ''' 
    Функция симуляции колебаний 
    Отрисовывает зарядку и первые 2 периода колебаний

    Parameters
    ----------
    E_loc : float/int
        Локальное значение ЭДС
    R_loc : float/int
        Локальное значение сопротивления
    C_loc : float/int
        Локальное значение ёмкости конденсатора
    show : bool
        True : отрисуется график
        False : не отрисуется график
    '''

    # Наследование переменных 
    if E_loc == None:
        E_loc = E
    if R_loc == None:
        R_loc = R
    if C_loc == None:
        C_loc = C

    # Дифференциальные уравнения для зарядки и разрядки конденсатора
    dU_1 = lambda U: (E_loc-U)/(R_loc*C_loc)
    dU_2 = lambda U: -U/(R_loc*C_loc)

    # Цикл интегрирования
    U_prev, U_prev2 = 0, -1
    i = 0
    U_t = []
    i_maxes = []
    charge = True
    maxes = 0
    while maxes < 3:

        # Проверка напряжения для смены режима работы лампы (разрядка или зарядка) 
        if U_prev < U1:
            charge = True
        if U_prev > U2:
            charge = False
        
        # Выбор дифференциального уравнения в зависимости от режима (разрядка или зарядка) 
        if charge:
            func = dU_1
        else:
            func = dU_2
        
        # Интегрирование
        U_cur = U_prev + func(U_prev)*(dt)
        
        # Проверка, является ли предыдущая точка максимумом
        if U_prev2 < U_prev and U_cur < U_prev:
            i_maxes.append(i)
            maxes += 1
    
        
        U_t.append(U_cur)
        U_prev2 = U_prev
        U_prev = U_cur
        i += 1

    # Переменная чтоб запомнить максимальный индекс массива
    i_max = i

    TT = np.linspace(0, i_max*dt, i_max)
    UU = lambda t: E_loc - (E_loc)*np.exp(-t/(R_loc*C_loc))
    UU_t = list(map(UU, TT))
    plt.plot(TT, UU_t)

    period = (i_maxes[1] - i_maxes[0])*dt
    print(f'Период колебаний (сим) T = {period}')

    T_span = np.linspace(0, i_max*dt, i_max)
    # Вывод гравика
    if show:
        plt.plot(T_span, U_t)
        plt.xlabel('t, c')
        plt.ylabel('U, B')
        plt.grid(True)
        plt.show()

    return period


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def neon_lamp_formulas(E_loc=None, R_loc=None, C_loc=None):
    ''' Рассчет периода по формулам из методички '''

    # Наследование переменных 
    if E_loc == None:
        E_loc = E
    if R_loc == None:
        R_loc = R
    if C_loc == None:
        C_loc = C
    
    # Рассчет τ1 и τ2
    tau1 = R_loc * C_loc * np.log((E_loc - U1)/(E_loc - U2))

    ro = 1/(1/R_loc + 1/R0)
    in_log = ((U2-V0)*R_loc + (U2-E_loc)*R0) / ((U1-V0)*R_loc + (U1-E_loc)*R0)
    tau2 = ro * C_loc * np.log(in_log)

    period = tau1 + tau2
    print(tau1, tau2)
    print(f'Период колебаний (форм) T = {period}')
    return period


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


dt = 1e-6

E = 144.75  # В
R = 300*1000  # Ом
C = 8.50e-07  # Ф

R0 = 5829 # Ом (сопротивление идеальной лампы)
V0 = 110.6 # В (нулевое напряжение идеальной лампы)

# Напряжение гашения и напряжение зажигания
U1 = 114.5  # В
U2 = 130.2  # В

# Варианты параметров из второго задания
E_arr = [144.72, 150.17, 155.06, 160.23, 165.23, 170.5, 175.6]
R_arr = [220000, 300000, 350000, 450000, 500000, 660000, 880000, 2200000, 4300000]
C_arr = [3.30e-07, 5.00e-07, 7.50e-07, 8.50e-07, 1.00e-06, 1.25e-06, 1.33e-06, 1.50e-06, 2.00e-06]

T_arr = []
T_arr2 = []
for i in C_arr:
    T_arr.append(neon_lamp_oscillation(C_loc=i, show=False))
    # T_arr2.append(neon_lamp_formulas(R_loc=i,))


print(T_arr)