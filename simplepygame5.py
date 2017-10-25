import sys
import random
import math

import pygame
import pygame.gfxdraw as gfxdraw 
from pygame.locals import *
import numpy as np
import time
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
from pygame import gfxdraw

cordsAndColor = []

def mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
    X = np.linspace(xmin, xmax, xn, dtype=np.float32)
    Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
    C = X + Y[:, None]*1j
    N = np.zeros(C.shape, dtype=int)
    Z = np.zeros(C.shape, np.complex64)
    for n in range(maxiter):
        I = np.less(abs(Z), horizon)
        N[I] = n
        Z[I] = Z[I]**2 + C[I]
    N[N == maxiter-1] = 0
    return Z, N

xmin, xmax, xn = -2.25, +0.75, 3000/2
ymin, ymax, yn = -1.25, +1.25, 2500/2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log(np.log(horizon))/np.log(2)
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
#print(Z)
with np.errstate(invalid='ignore'):
    M = np.nan_to_num(N + 1 - np.log(np.log(abs(Z)))/np.log(2) + log_horizon)

light = colors.LightSource(azdeg=315, altdeg=10)
M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,norm=colors.PowerNorm(0.3), blend_mode='hsv')
#print(M[1])

def makearray(M):
    x=0
    y=0
    cordsAndColor = []
    print(len(M))
    for line in M:
        #print(len(line))
        for item in line:
            c = 0
            for rgba in item:
                
                #r=rgba[1]
                if c == 0:
                    r=rgba
                if c == 1:
                    g=rgba
                if c == 2:
                    b=rgba
                c+=1
                if c == 4:
                    c=0
                    
                    
                #print(rgba)
               # g=0#int(rgba[2]*255)
               # b=0#int(rgba[3]*255)
            if x<=1499 and y<=1249:
                r=round(255*r)
                r=int(r)

                g=round(255*g)
                g=int(g)
                
                b=round(255*b)
                b=int(b)
            if x == 1499:
                x=0
            #print(x, y, r, g, b)
            temp=x, y, r, g, b
            #print(temp)
            #creating pixel for array with rectified rgb
            temp=list(temp)
            

            cordsAndColor.append(temp)
    
            #gfxdraw.pixel(DS, x, y, (r, g, b))
            x+=1
        y+=1
    return cordsAndColor
cordsAndColor = makearray(M)        
''' It maybe important to point out that i use CAPS to show a constant variable, ie has the same value all the way through the program. '''
''' This is personal choice and others may not use this distinction '''

# initialise the pygame library
pygame.init()

DISPLAY_WIDTH = 1500 # screen width in pixels
DISPLAY_HEIGHT = 1250 # screen height in pixels
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT # screen area in pixels

# create the primary display surface (DS) based on our chosen resolution
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))


# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS

# this function handles window controls [x] and key presses [esc].
def event_handler():
    for event in pygame.event.get():
        # if [esc]
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            # ... then quit!
            pygame.quit()
            sys.exit() 
		
# MAIN ----------------------------------------------------------------------------------------------------- MAIN

# the main program loop. this will loop forever
# others don't structure their programs like this however i do, it a personal choice.
while True:
    event_handler() # check for [esc] 
    
    #print(M.type())
    # update the screen. this is important as drawing graphics (square, lines, circles) won't appear until you have called update()
    pygame.display.update()
    print(len(cordsAndColor))
    for pix in cordsAndColor:
        gfxdraw.pixel(DS, pix[0], pix[1], (pix[2], pix[3], pix[4]))
    print('end')
    

        #DS.update()        
            
            #gfxdraw.pixel(DS, x, y, (255, 255, 255))
           # x+=1
        #
        
        
        
        #   to = 
        #
        
    #gfxdraw.pixel(DS, x, y, (255, 255, 255))
    # clear the surfuce to black.
    #DS.fill([0,0,0])
