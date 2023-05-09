# include <stdio.h>
# include <math.h>
# include <complex>
#include <iostream>

using namespace std;

int main()
{

    //FIJAMOS N, nciclos(max), Lambda y j=0 EL RESTO A UN BUCLE 
    double pi=3.14159265359;
    int N=40;
    int nciclos=N/4;  //hasta N/4
    double l=0.3;   //lambda

    FILE* fichero= fopen("schrodinger_data.dat","a");

    for ( int n=0;n<=nciclos;n++)
    {
        //generamos k0 y s que vayan cambiando para cada n
        double k0=2*pi*n/N;
        double s=1/(4*k0*k0);


        //Bucle que vaya disminuyendo j
        for (int p=0;p==N;p++)
        {
            //generamos Vj
            int j=N-p;
            double Vj;
            if (2*N/5<=j<=3*N/5)
            {
                Vj=l*k0*k0;
            }
            else
            {
                Vj=0;
            }

            //Fi_j,0
            complex<double>c,fijn;
            c=complex<double>(0,k0*j);
            fijn=exp(c)*exp(-8*(4*j-N)*(4*j-N)/(N*N));

        

            if (j==0 and n==0)
            {
                fijn=0;
            }
            if (j==N and n==0)
            {
                fijn=0;
            }

            //cosas de la alfa y la beta
            complex<double> Ajmas,Ajmenos,Aj0,gamma,bjn,a[N],b[N],x;
            Ajmenos=(1,0);
            Ajmas=(1,0);
            Aj0=complex<double> (-2,2/s-Vj);
            
            bjn=4.*fijn/s;

            


            if(j==N-1)
            {
                a[j]=0;
                b[j]=0;
            }

            if(j!=N and j!=N-1)
            {
                gamma=1./(Aj0+Ajmas*a[j+1]);

                a[j]=-Ajmenos*gamma;
                b[j]=gamma*(bjn-Ajmas*bjn);
                
            }

            for (int d=0;d<N;d++)
            {
                x=a[d]*x+b[d];
                fijn=x-fijn;

                //fprintf(fichero,"%f",real(fijn));
                //fprintf(fichero,"\n");
                
            }
            
        }
    
    }


    fclose(fichero);


    return 0;
}
