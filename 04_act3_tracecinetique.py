from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

print("")
print("**************************************")
print("* Tracé de courbe de suivi cinétique *")
print("*   Activité 3 p. 120                *")
print("*************************Hatier 2020**")

print("")
print("Attention : le séparateur décimal est le point")
print("")

listet=[0.0,10.0,20.0,30.0,60.0,90.0]
listec=[124.0,92.0,68.0,50.0,20.0,8.0]
# première ligne à compléter
plt.plot(listet,listec,color="blue")
# seconde ligne à compléter
plt.title("Concentration c (en mmol/L) en fonction de t (en min)")
plt.xlabel("t (en min)")
plt.ylabel("Concentration c (en mmol/L)")
plt.show()
