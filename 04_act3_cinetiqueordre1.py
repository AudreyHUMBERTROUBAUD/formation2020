from math import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

print("")
print("**************************************")
print("* Cinétique d'ordre 1                *")
print("*   Activité 3 p. 120                *")
print("*************************Hatier 2020**")

print("")
print("Attention : le séparateur décimal est le point")
print("")

# définition extensive d'une liste (extrait d'un tableau de mesures)
listet=[0.0,10.0,20.0,30.0,60.0,90.0]
listec=[124.0,92.0,68.0,50.0,20.0, 8.0]
listelnc=[0.0,0.0,0.0,0.0,0.0,0.0]
modelelinY=[0.0,0.0,0.0,0.0,0.0,0.0]

# calcul de la liste des logarithmes des concentrations
for i in range(0,6):
    listelnc[i]=np.log(listec[i])
    
# tracé du graphique donnant ln(c) en fonction de t
plt.plot(listet,listelnc,"*",color="red")

# calcul des paramètres de la régression linéaire
(a,b,rho,_,_)=linregress(listet,listelnc)
# a : coefficient directeur
# b : ordonnée à l'origine
# rho : coefficient de corrélation linéaire
print("ln(c)=",a,"t+",b,"coef. de corr. =",rho)
for i in range(0,6):
    modelelinY[i]=a*listet[i]+b
    
# tracé de la droite de régression linéaire
plt.plot(listet,modelelinY,color="blue")
plt.xlabel("t (en min)")
plt.ylabel("ln(c)")
plt.show()
