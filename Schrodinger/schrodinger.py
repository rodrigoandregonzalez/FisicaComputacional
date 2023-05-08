import numpy as np

N=40
nciclos=N/4 #n maximo
l=0.3 #lambda
n=1

while n<nciclos:
    
    k0=2*np.pi*n/N
    s=1/(4*k0**2)


    Vj=np.zeros(N,dtype=complex)
    fij0=np.zeros(N,dtype=complex)

    for j in range(N):

        if 2*N/5<=j<=3*N/5:
            Vj[j]=l*k0**2
        else:
            Vj[j]=0

        if j==0 or j==N:
            fij0[j]=0
        else:
            fij0[j]=np.e**(complex(0,k0*j))*np.e**((-8*(4*j-N)**2)/N**2)

        Ajmenos=1
        Ajmas=1
        Aj0=np.zeros(N,dtype=complex)
        Aj0[j]=complex(-2,2j/s)-Vj[j]


        a=np.zeros(N-1,dtype=complex)
        a[N-2]=0
        h=N-2-j
        gamma=np.zeros(N,dtype=complex)
        if h>1:
            gamma[h]=Aj0+Ajmas*a[h]
            a[h-1]=-Ajmenos/gamma[h]

        


    


    n=n+1




