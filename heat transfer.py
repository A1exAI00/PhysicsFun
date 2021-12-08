# -*- coding: utf-8 -*-
"""
Created on ---UNKNOWN---

@author: Alex Akinin

Симуляция теплопроводности
Задумка прикольная 
Но результаты ❌РАСХОДЯТСЯ❌ с опытными
"""


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


import matplotlib.pyplot as plt
import time


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


def redraw(self):
    line.set_ydata(self)
    fig.canvas.draw()
    fig.canvas.flush_events()


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


#p = 0: условие при постоянной мощности P
#p = 1: условие при постоянной температуре T_max
p = 0

length = 50
k = 2
s = 2
density = 2
power = 50
heat_capacity = 2
dx = 1
cycles = 1
T_min = 10
T_max = 20
delta_t = 1
delta_tt = 0
t=0

T = [T_min for h in range(length)]; X = [h for h in range(length)]

plt.ion()
fig, ax = plt.subplots(); line, = ax.plot(X,T)

ax.set_xlim(0, length)
T_end = T_min + (power*length)/(2*k*s)

if p == 0:
    ax.set_ylim(T_min,T_end)
    while T[0]<T_end/2:
        T[0] = T[0]+power*delta_t/(heat_capacity*density*s*dx)
        for i in range(cycles):
            for j in range(length-1):
                delta_T = T[j+1]-T[j]
                T[j] += (k*delta_T)/(heat_capacity*density*dx)
                if j<length-2:
                    T[j+1] += -(k*delta_T)/(heat_capacity*density*dx)
        t += 1
        #print(t," : ",T[0])
        redraw(T)
        time.sleep(delta_tt)

else:
    ax.set_ylim(T_min,T_max)
    T[0] = T_max
    while True:
        for i in range(cycles):
            for j in range(length-1):
                delta_T = T[j+1]-T[j]
                if j>0:
                    T[j] += (k*delta_T)/(heat_capacity*density*dx)
                if j<length-2:
                    T[j+1] += -(k*delta_T)/(heat_capacity*density*dx)
        t += 1
        redraw(T)


print("t =",t)
plt.ioff()
plt.show()
