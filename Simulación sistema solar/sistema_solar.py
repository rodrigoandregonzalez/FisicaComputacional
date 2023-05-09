#ENTREGAR:
#   ~VIDEO ORBITAS
#   ~PLOT ENERGIA(T)
#   ~PERIODO ROTACION PLANETAS
#   ~EL SISTEMA ES ESTABLE FRENTE A PERTURBACIONES

#############################################################
import numpy as np 
import matplotlib.pyplot as plt
#############################################################
'''
#Datos de las masas, distancia del semieje mayor y su velocidad
'''
UA=149597870700 #expresada en metros
G=6.67*10**(-11) 
Ms=1.99*10**(30)

masas=np.array([1.99*10**(30),3.302*10**(23),4.869*10**(24),5.9736*10**(24),6.4185*10**(23),1.899*10**(27),5.688*10**(26),8.686*10**(25),1.024*10**(26)])

#para r(0) usamos el radio orbital medio

#x0=np.array([0,0.387*UA,0.72333199*UA,0.999855*UA,1.523662*UA,5.20336301*UA,9.53707032*UA,19.19126393*UA,30.06896341*UA])
x0=np.array([0,57.9,	108.2,	149.6,	227.9,	778.6,	1433.5,	2872.5,	4495.1])*10**(9) #en m
y0=np.array([0,0,0,0,0,0,0,0,0])

r0=np.array([x0,y0])

#Para v(0) usamos la velocidad orbital media
vx0=np.array([0,0,0,0,0,0,0,0,0])
#vy0=np.array([0,47.8725*10**(3),35.5*10**(3),29.78*10**(3),24.077*10**(3),13.0697*10**(3), 9672.4 ,6.81*10**(3),5.4778*10**(3)])
vy0=np.array([0,47.9,	35.0,	29.8,		24.1,	13.1,	9.7,	6.8,	5.4])*10**3 #en m/s

v0=np.array([vx0,vy0])

#c= distancia de la tierra al sol (1.469*10**(11))m
c=1.469*10**(11)

#reescalado
masasp=masas/Ms
r0p=r0/c

'''
def tiempo(t):
    tp=(G*Ms/c**3)**(1/2)*t
    return tp
'''
##########################################################################################################################################

t=0
h=0.2 #cuanto tiempo le vamos a sumar a cada calculo

#necesitamos una funcion para a, r, w y v
#PRIMERO calculamos a(t) usando r(0)
#SEGUNDO calculamos r(t+h) y wi=vi(t)+h/2a(t)
#TERCERO calculamos a(t+a) utilizando la r(t+h)
#CUARTO calculamos v(t+h)=wi+h/2a(t+h)
#repetimos con t=t+h desde el segundo paso (vamos sumando h a cada bucle)



'''def aceleracion(m,r):     #INTENTO DE ACELERACION
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    a=np.array([x,y])
    

    for i in range(len(m)):
        for j in range(len(m)):
            if j==i:
                lista=lista+0
            else:
                for k in range(0,1):
                    akj=(-1)*(m[j]*(r[k][i]-r[k][j]))/(np.sqrt((r[0][i]-r[0][j])**2+(r[1][i]-r[1][j])**2))**3
                lista=lista+    
            
                    #rvector-rvector)/modulo r-r vectores**3    HAY QUE SUMAR TODAS LAS J
    return a
'''

#FUNCION PARA LA ACELERACION
def aceleracion(m,r):  #~Funciona bien~
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    a=np.array([x,y])
    

    for i in range(len(m)):
        
        for k in range(2):
            lista=0
            for j in range(len(m)):
                akj=0
                if j==i:
                    lista=lista+0
                    
                else:
                    akj=(m[j]*(r[k][i]-r[k][j]))/(np.sqrt((r[0][i]-r[0][j])**2+(r[1][i]-r[1][j])**2))**3
                    
                    lista=lista-akj    
            a[k][i]=lista

                    #rvector-rvector)/modulo r-r vectores**3    HAY QUE SUMAR TODAS LAS J
    return a


#FUNCION PARA r(t+h):
'''
def posicion(pos,vel,ac,m,h):
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    r=np.array([x,y])
    
    for i in range(len(m)):
        
        for k in range(2):
            
            r[k][i]=pos[k][i]+h*vel[k][i]+(h**2)/2*ac[k][i]
    
    return r
'''

#FUNCION PARA w(t+h):
def uvedoble(vel,ac,m,h):
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    w=np.array([x,y])
    
    for i in range(len(m)):
        for k in range(2):
            w[k][i]=vel[k][i]+(h/2)*ac[k][i]
    
    return w
    
'''Posicion pero usando la w

def posicion(pos,vel,ac,m,h):
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    r=np.array([x,y])
    
    for i in range(len(m)):
        
        for k in range(2):
            
            r[k][i]=pos[k][i]+h*uvedoble(vel,ac,m,h)[k][i]
    
    return r
'''
'''

Posicion pero usando la w
'''
def posicion(pos,w,m,h):
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    r=np.array([x,y])
    
    for i in range(len(m)):
        
        for k in range(2):
            
            r[k][i]=pos[k][i]+h*w[k][i]
    return r


#FUNCION PARA VELOCIDAD:
def velocidad(w,ac,m,h):
    x=np.zeros(len(m))
    y=np.zeros(len(m))
    v=np.array([x,y])
        
    for i in range(len(m)):
        for k in range(2):
            v[k][i]=w[k][i]+(h/2)*ac[k][i]

    return v


#calculamos la energía de cada órbita
def Energia(pos,vel,m):
    E=0
    T=0
    V=0
    for i in range(len(m)):
        T=T+(1/2)*m[i]*(vel[1][i]**2+vel[0][i]**2)
    
        for j in range(len(m)):
            if j!=i:
                V=V-m[i]*m[j]/((pos[0][i]-pos[0][j])**2+(pos[1][i]-pos[1][j])**2)**(1/2)
                E=T+V
    return E



#lo que hay que hacer ahora es un bucle que vaya aumentando h cada vuelta y grabe la posicion en un texto
#1)evaluar aceleracion para t=0
#2)evaluar w para t=0
#3)evaluar r para t+h
#4)evaluar a para t+h usando r(t+h)
#5)evaluar v para t+h
#6)repetir desde (2) haciendo t=t+h


a=aceleracion(masasp,r0p)
v=v0*(1/c)*((G*Ms)/c**3)**(-1/2)
r=r0p


f=open('planets_data.dat','w')
np.savetxt(f,np.transpose(r0p),newline='\n',delimiter=',')
f.write('\n')


#PLOT DE ENERGIA para t=0
E=Energia(r0p,v,masasp)
fig,ax=plt.subplots(1,1)
plt.plot(t,E)
linea1=ax.plot(E,0,'o',mfc='w',mec='k',ms=1)
ax.tick_params(axis='x',length=6, width=1,labelsize=5)
ax.tick_params(axis='y',length=6, width=1,labelsize=5)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')
ax.set_xlabel('t',fontsize=20)
ax.set_ylabel('E',fontsize=20)
plt.grid(True)


periodos=np.zeros(len(masasp))

n=1000
for i in range(n):
    w=uvedoble(v,a,masasp,h)
    r=posicion(r,w,masasp,h)
    a=aceleracion(masasp,r)
    v=velocidad(w,a,masasp,h)
    
    #Calculo de los periodos
    posiciones=np.transpose(r)
    
    if i!=0:
        for j in range(9):
            if posiciones[j][1]>0 and prepos[j][1]<0 and periodos[j]==0:
                periodos[j]=t
    
    prepos=posiciones
 
    #Energia para t+h
    E=Energia(r,v,masasp)
    plt.plot(t,E)
    linea1=ax.plot(t,E,'o',mfc='w',mec='k',ms=1)
    
    t=t+h
    
    
    np.savetxt(f,posiciones,newline='\n',delimiter=',')
    f.write('\n')

periodostab=np.array([0,88.0,224.7,365.2,687.0,4331,10747,30589,59800])

eabs=abs(periodos*58.1-periodostab)
er=eabs/periodostab*100

print('Periodos calculados: ',periodos*58.1) #La primera componente de la array es el sol
print('Periodos tabulados: ',periodostab)
print('error relativo: ',er) 


plt.show()

f.close()





