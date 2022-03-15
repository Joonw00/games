import pygame, sys
from pygame.locals import *

def adjx(x):
    if x%40 <= 20:
        a = x%40
        x-=a
        return x

def adjy(y):
    if y%40 > 20:
        a = y%40
        y-=a+40
        return y