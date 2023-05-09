import numpy as np

N=40
nciclos=int(N/4) #n maximo
l=0.3 #lambda
n=0

k0=np.zeros(nciclos)
s=np.zeros(nciclos)

Vj=np.zeros(N,dtype=complex)
fij0=np.zeros(N,dtype=complex)

Ajmenos=1
Ajmas=1
Aj0=np.zeros(N,dtype=complex)

a=np.zeros(N,dtype=complex)
a[N-1]=0

gamma=np.zeros(N,dtype=complex)

#GENERAMOS LOS PARAMETROS QUE VAN A SER CONSTANTES
for n in range(nciclos):
    k0[n]=2*np.pi*(n+1)/N

    s[n]=1/(4*k0[n]**2)

    for j in range(N):

        if 2*N/5<=j<=3*N/5:
            Vj[j]=l*k0[n]**2
        else:
            Vj[j]=0

        if j==0 or j==N:
            fij0[j]=0
        else:
            fij0[j]=np.e**(complex(0,k0[n]*j))*np.e**((-8*(4*j-N)**2)/N**2)


        Aj0[j]=complex(-2,2/s[n])-Vj[j]

        h=N-2-j
        
        gamma[h]=Aj0[h]+Ajmas*a[h]

        a[h-1]=-Ajmenos*gamma[h]

    
print(a)

#BUCLE PARA LOS PASOS 2,3,4








