
"""
@author: olal
"""

from numpy import *
import matplotlib.pyplot as plt

f_upper = []  #oppretter en tom vektor f_upper

f = open('input_oppgave5_upper_curve.txt', 'r')
for line in f:
    f_upper.append(float(line)) #Her lagres verdiene fra fil i vektoren f_upper


g_lower = []  #oppretter en tom vektor g_lower

g = open('input_oppgave5_lower_curve.txt', 'r')
for line in g:
    g_lower.append(float(line)) #Her lagres verdiene fra fil i vektoren g_lower


x=linspace(0,3,20) #Her er x-verdiene for observasjonene f_upper and g_lower

     
plt.plot(x,g_lower,'r*',x,f_upper, 'b*')
plt.axis([0, 9, -1, 8])
plt.show()



#Under her kan du naa skrive koden for oppgave 5



