import numpy as np
import cmath as cmath
import matplotlib.pyplot as plt
N=1000
nciclos=100
l=0.3 #lambda
n=0
j=0

k0=np.zeros(nciclos)
s=np.zeros(nciclos)

Vj=np.zeros(N,dtype=complex)
fi=np.zeros(N,dtype=complex)

Ajmenos=1
Ajmas=1
Aj0=np.zeros(N,dtype=complex)

a=np.zeros(N,dtype=complex)
a[N-2]=0+0j

gamma=np.zeros(N,dtype=complex)


#generamos k0 y s:
'''
while n < nciclos:
    k0[n]=2*np.pi*(n+1)/N #k0[0] es n=1, k0[1] es n=2...
    s[n]=1/(4*k0[n]**2)
    n=n+1
n=0
'''
k0=2*np.pi*nciclos/N
s=1/(4*k0**2)


#generamos Vj y fi n=0:
while j<N:
    if 2*N/5<=j<=3*N/5:
        Vj[j]=l*k0**2
    else:
        Vj[j]=0

    fi[j]=np.exp(1j*k0*j)*np.exp((-8*(4*j-N)**2)/(N**2))
    j=j+1

fi[0]=0
fi[N-1]=0

norma=np.sum(abs(fi))
#print(norma)
j=0
n=0

#generamos alfa:

for j in range(N):
    Aj0[j]=-2+2j/s-Vj[j]
    


'''
f=N-1
while f>=0:
    gamma[f]=1/(Aj0[f]+a[f])
    a[f-1]=-1*gamma[f]
    a[N-2]=0
    f=f-1 
'''

for i in range(N):
        #alfa
        h=N-i
        if i<N-2:
            a[N-2]=0
            a[0]=0
            gamma[h-1]=1/(Aj0[h-1]+a[h-1])
            a[h-2]=(-1)*gamma[h-1]
            a[N-2]=0
            a[0]=0
                



#calculamos beta, chi, fij+1 
beta=np.zeros(N,dtype=complex)
b=np.zeros(N,dtype=complex)
chi=np.zeros(N,dtype=complex)



n=0

fig,ax=plt.subplots(1,1)

with open("schrodinger_data.dat", "w") as f:

    while n<=N:
        for i in range(N):
            #beta
            h=N-i
            if h<N:
                beta[N-2]=0
                beta[0]=0
                b[h-1]=4j*fi[h-1]/s
                beta[h-2]=gamma[h-1]*(b[h-1]-beta[h-1])
                beta[N-2]=0
                beta[0]=0
        

        for i in range(N):
            #chi
            if i<N-1:
                    #chi[h-1]=a[h-2]*chi[h-2]+beta[h-2]
                chi[0]=0    
                chi[i+1]=a[i]*chi[i]+beta[i]
            chi[N-1]=0

            #fi
                    #    fi[h]=chi[h-1]-fi[h-1]
            fi[i]=chi[i]-fi[i] 
            fi[0]=0
            fi[N-1]=0

            modulo=np.zeros(N,dtype=float)

            fireal=fi.real
            fimag=fi.imag

            modulo=abs(fi)
            norma=np.sqrt(modulo[8])





            f.write(f"{i},{modulo[i]},{Vj[i].real}\n")

        f.write(f"\n")


        linea1=ax.plot(n,norma,'o',mfc='w',mec='k',ms=1)
        
        
    
        
        
        n=n+1

plt.show()

