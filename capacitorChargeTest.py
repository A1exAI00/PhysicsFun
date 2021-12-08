# -*- coding: utf-8 -*-
"""
Created on ---UNKNOWN---

@author: Alex Akinin

Симуляция зарядки конденсатора
"""


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


# Задать t_span
T_min, T_max, T_num = 0, 10, 10000
T_span = np.linspace(T_min, T_max, T_num)
dt = (T_max - T_min)/T_num

E = 145
R = 1e6
C = 1e-6

# Дифф уравнения зарядки конденсатора
diff_eq_1 = lambda U: (E-U)/(R*C)

# Интегрирование методом Эйлера
U0 = 0
U_t = []
for t in T_span:
    func = diff_eq_1
    U_cur = U0 + func(U0)*dt
    U_t.append(U_cur)
    U0 = U_cur

T_span = list(T_span)

plt.plot(T_span, U_t)
plt.grid(True)
plt.show()