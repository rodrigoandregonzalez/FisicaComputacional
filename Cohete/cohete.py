import numpy as np
import matplotlib as plt

G=6.67*10**(-11) #N·m^2 kg^(-2)
Mt=5.9736*10**(24) #kg
Ml=0.07349*10**(24) #kg
dtl=3.844*10**(8) #m
w=2.6617*10**(-6) #s^(-1)

Rt=6.378160*10**(6) #m
Rl=1.7374*10*(6) #m

D=G*Mt/dtl**3
mu=Ml/Mt

###########################################################################

h=60
t=0

mcohete=100

epsilon=h**5

r0=Rt
teta0=0
vr0=mcohete*11200  #mcohete*vescapetierra
vteta0=0




