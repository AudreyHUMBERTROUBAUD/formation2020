# -*- coding: utf-8 -*-
from math import *
from pylab import *
print("bienvenue, nous allons tracer une fonction sin X, sin (X + déphasage) et la somme des deux fonctions")
print("veuillez saisir le déphasage en écrivant tracé(valeur du déphasage), par exemple tracé(3*pi/2)")
def tracé(dephasage):
    x = linspace(0, 2*pi, 30)
    y1 = sin(x)
    y2 = sin(x+dephasage)
    y3 = y1 + y2
    plot(x, y1, label="sin(x)")
    plot(x, y2, label="sin(x+dephasage)")
    plot(x, y3, label="somme des deux fonctions : sin(x)+sin (x+dephasage)")
    legend()

    show()
    