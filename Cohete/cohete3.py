import numpy as np
import matplotlib.pyplot as plt

#constantes
G=6.67*10**(-11) #N·m^2 kg^(-2)
Mt=5.9736*10**(24) #kg
Ml=0.07349*10**(24) #kg
dtl=3.844*10**(8) #m
w=2.6617*10**(-6) #s^(-1)

Rt=6.378160*10**(6) #m
Rl=1.7374*10*(6) #m

D=G*Mt/dtl**3
mu=Ml/Mt

h=60

mcohete=100
#####################################################################
#vec=[r,teta,pr,pteta,t]
def resc(vec):
    v=np.zeros(len(V))
    v[0]=vec[0]/dtl
    v[1]=vec[1]
    v[2]=vec[2]/(mcohete*dtl)
    v[3]=vec[3]/(mcohete*dtl**2)
    return v

def rprima(vec):
    p=np.sqrt(1+vec[0]**2-2*vec[0]*np.cos(vec[1]-w*vec[4]))
    return p

def difvec(vec):
    dvec=np.zeros(len(V))
    dvec[0]=vec[2]
    dvec[1]=vec[3]/vec[0]**2
    dvec[2]=vec[3]**2/vec[0]**3-D*(1/vec[0]**2+mu/rprima(vec)**3*(vec[0]-np.cos(vec[1]-w*vec[4])))
    dvec[3]=-D*mu*vec[0]/rprima(vec)**3*np.sin(vec[1]-w*vec[4])
    return dvec

#funciones para k:
def kfun(vector):
    n=len(vector)
    k=np.zeros(n)
    k[n-1]=h
    for i in range(n-1):
        k[i]=h*vector[i]
    return k

def sumak23(vector,k): #suma para k2 y k3
    n=len(vector)
    suma=np.zeros(n)
    for i in range(n):
        suma[i]=vector[i]+k[i]/2        
    return suma

def sumak4(vector,k): #suma para k4
    n=len(vector)
    suma=np.zeros(n)
    for i in range(n):
        suma[i]=vector[i]+k[i]        
    return suma

#funciones para el hamiltoniano
def rl(vec):
    l=np.sqrt(vec[0]**2+dtl**2-2*vec[0]*dtl*np.cos(vec[1]-w*vec[4]))
    return l

def hamilton(vec):
    H=vec[2]**2/(2*mcohete)+vec[3]**2/(2*mcohete*vec[0]**2)-G*mcohete*Mt/vec[0]-G*mcohete*Ml/rl(vec)
    return H

def noresc(vec):
    nv=np.zeros(len(vec))
    nv[0]=vec[0]*dtl
    nv[1]=vec[1]
    nv[2]=vec[2]*(mcohete*dtl)
    nv[3]=vec[3]*(mcohete*dtl**2)

    return nv
#####################################################################

r0=Rt
teta0=25*np.pi/180
pr0=mcohete*11200  #mcohete*vescapetierra
pteta0=0
t=0

V=np.array([r0,teta0,pr0,pteta0,t])
V=resc(V)
dV=difvec(V)

n=len(V)

VH=np.zeros(n)
hamiltoniano=0

f=open('cohete_data.dat','w')
g=open('hamiltoniano.dat','w')

f.write(str(0.0)+','+str(0.0)+'\n') #posicion tierra
f.write(str(V[0]*np.cos(V[1]))+','+str(V[0]*np.sin(V[1]))+'\n') #posicion cohete
f.write(str(np.cos(w*V[4]))+','+str(np.sin(w*V[4]))+'\n') #posicion luna
f.write('\n')

VH=noresc(V)
hamiltoniano=hamilton(VH)

g.write(str(hamiltoniano)+'\n')
g.write('\n')

fig,ax=plt.subplots(1,1)

for i in range(10000):
    aux=0
    k1=kfun(dV)

    aux=sumak23(V,k1)
    aux=(difvec(aux))
    k2=kfun(aux)

    aux=sumak23(V,k2)
    aux=(difvec(aux))
    k3=kfun(aux)

    aux=sumak4(V,k3)
    aux=(difvec(aux))
    k4=kfun(aux)

    for i in range(n-1):
        V[i]=V[i]+1/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])

    V[n-1]=V[n-1]+h
   
    dV=difvec(V)
    
    f.write(str(0.0)+','+str(0.0)+'\n') #posicion tierra
    f.write(str(V[0]*np.cos(V[1]))+','+str(V[0]*np.sin(V[1]))+'\n') #posicion cohete
    f.write(str(np.cos(w*V[4]))+','+str(np.sin(w*V[4]))+'\n') #posicion luna
    f.write('\n')

    #Hamiltoniano:
    VH=noresc(V)
    hamiltoniano=hamilton(VH)


    linea1=ax.plot(V[4],hamiltoniano,'o',mfc='w',mec='k',ms=1)
    ax.set_xlabel('t',fontsize=20)
    ax.set_ylabel('H',fontsize=20)

    g.write(str(hamiltoniano)+'\n')
    g.write('\n')


f.close()
g.close()

plt.show()
#parece que furrula, falta hamiltoniano y cambiar los V[4] por n-1 que queda mas generico y eso siempre esta bien uwu   