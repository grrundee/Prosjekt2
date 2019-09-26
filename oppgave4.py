
"""
@author: olal
"""

import numpy as np 
import matplotlib.pyplot as plt
import math as m 

f = []  #oppretter en tom vektor f

g = open('c:\\Users\\gregd\\OneDrive - USN\\Skole\\3. Semester\\FB1012-1-19H Mattematikk 1\\Dataverktøy\\Prosjekter\\Prosjekt2\\'+'input_oppgave4.txt', 'r')

for line in g:
    f.append(float(line)) #Her lagres verdiene fra fil i vektoren f


x = np.linspace(0,15,47) #Her er x-verdiene for observasjonene f


plt.plot(x,f,'r', linewidth=4) #viser sammenhengende kurve 
plt.show()

plt.plot(x,f,'r*', linewidth=4) #viser bare datapunktene
plt.show()


#Under her kan du naa skrive koden for oppgave 4
n = 46

delta_x = (15 - 0)/n

volum= m.pi * (0.5*(m.pow(f[0],2) + m.pow(f[-1],2)) * delta_x)

for i in range(1,n,1):
    volum = volum + m.pi*(m.pow(f[i],2) * delta_x)

print(round(volum,4))