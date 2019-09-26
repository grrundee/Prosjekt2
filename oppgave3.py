
"""
@author: olal
"""

import numpy as np 
import matplotlib.pyplot as plt

v = []  #oppretter en tom vektor v

g = open('C:\\Users\\gregd\\OneDrive - USN\\Skole\\3. Semester\\FB1012-1-19H Mattematikk 1\\Dataverktøy\\Prosjekter\\Prosjekt2\\input_oppgave3.txt', 'r')
for line in g:
    v.append(float(line)) #Her lagres verdiene fra fil i vektoren v


t=np.linspace(0,200,201)  #Her er tidspunktene for observasjonene v


plt.plot(t,v,'r', linewidth=4) #viser sammenhengende kurve 
plt.axis([0,200,0,80])
plt.show()

#Her kan du skrive programmet ditt

#comment
#comment          