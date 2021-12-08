# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:58:27 2021

@author: Alex Akinin

Простенькая симуляция широв в жидкости
с возможностью их попинать 
"""


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


import pygame as pg
import numpy as np


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


class Ball:
    def __init__(self, r) -> None:
        ''' 
        Метод инициализации шара
        
        Parameters
        ----------
        r : float/int
            Радиус шара
        '''

        V_max = 5
        self.r = r
        self.mass = self.r
        self.x = (WIDTH - 2*self.r) * np.random.rand()
        self.y = (HEIGHT - 2*self.r) * np.random.rand()
        self.Vx = V_max * np.random.rand()
        self.Vy = V_max * np.random.rand()
        self.color = tuple([round(250*np.random.rand() + 2) for _ in range(3)])
    
    
    def movement(self) -> None:
        ''' Метод обновления позиции шара '''
        self.x += self.Vx/FPS
        self.y += self.Vy/FPS
    
    
    def gravity(self) -> None:
        ''' Метод обновления скорости шара под действием гравитации '''
        self.Vy += g/FPS
    
    
    def viscosity(self) -> None:
        ''' Метод обновления скорости шара под действием вязкости '''
        k_slow = -1
        V = np.sqrt(self.Vx**2 + self.Vy**2)
        if self.Vx > 0:
            self.Vx += k_slow*V/FPS
        if self.Vx < 0:
            self.Vx -= k_slow*V/FPS
        if self.Vy > 0:
            self.Vy += k_slow*V/FPS
        if self.Vy < 0:
            self.Vy -= k_slow*V/FPS
    
    
    def draw(self) -> None:
        ''' Метод отрисовки шара в Pygame окне '''
        pos = (self.x, self.y)
        pg.draw.circle(DISPLAYSURF, self.color, pos, self.r)
    
    
    def check_pos(self) -> None:
        ''' Метод проверки столкновения шара со стенкой '''
        if self.x > WIDTH - self.r:
            self.Vx = -abs(self.Vx)
            self.x = WIDTH - self.r
        if self.x < self.r:
            self.Vx = abs(self.Vx)
            self.x = self.r
        if self.y > HEIGHT - self.r:
            self.Vy = -abs(self.Vy)
            self.y = HEIGHT - self.r
        if self.y < self.r:
            self.Vy = abs(self.Vy)
            self.y = self.r
    

    def getEnergy(self):
        ''' Getter для всей полной энергии шара'''
        return g*(HEIGHT - self.y) + np.sqrt(self.Vx**2 + self.Vy**2)**2 / 2
    
    
    def blackHole(self, pos, k):
        ''' Метод обновления скорости под действием силы от курсора '''
        imp = 20000
        x, y = pos
        r_min = 15
        dx = (self.x - x)
        dy = (self.y - y)
        r = np.sqrt(dx**2 + dy**2)
        if r < r_min:
            r = r_min
        self.Vx += k*imp *dx/r**3
        self.Vy += k*imp *dy/r**3
    
    def getInfo(self):
        ''' Getter полной информации о шаре'''
        return self.x, self.y, self.Vx, self.Vy, self.r, self.mass


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


BGCOLOR = (255,255,255)
FPS = 60
WIDTH = 700
HEIGHT = 700
NUM_BALLS = 2
g = 50

# Инициализация Pygame 
DISPLAYSURF = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Hello")
clock = pg.time.Clock()
clock.tick(FPS)
DISPLAYSURF.fill(BGCOLOR)

# Создание шаров
balls = [Ball(10*np.random.rand()+5) for _ in range(NUM_BALLS)]

running = True
while running:
    DISPLAYSURF.fill(BGCOLOR)

    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
        
        mp = pg.mouse.get_pressed()
        if mp[0]:
            for ball in balls:
                ball.blackHole(pg.mouse.get_pos(), 1)
        if mp[2]:
            for ball in balls:
                ball.blackHole(pg.mouse.get_pos(), -1)
    
    for ball in balls:
        ball.movement()
        ball.draw()
        ball.gravity()
        ball.viscosity()
        ball.check_pos()
    
    pg.display.update()
    clock.tick(FPS)


pg.quit()
