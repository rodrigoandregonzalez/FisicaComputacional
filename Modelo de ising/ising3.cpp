
#include <stdio.h>
#include <cmath>
#include <cstdlib>
#include <time.h>
#include <iostream>

int main()
{
    srand(time(NULL));

    double T=1; //TEMPERATURA
    
    int N=100; //TAMAÑO DE LA MATRIZ
    int matriz[N][N];
    
    int d=0;
    FILE* fichero= fopen("ising_data.dat","a");

    for ( int i = 0; i< N ; i++) //GENERAMOS MATRIZ DE 1 Y -1
    {
        for (int j=0 ; j<N; j++)
        {
            int y=rand()%(2);
            
            matriz[i][j]=pow(-1,y);

        }
    }


    for (int a=0;a<100000*pow(N,2);a++) // BUCLE PARA CAMBIAR LOS SPINES
    {
        int n=rand()%N;
        int m=rand()%N;

        int aux1=n+1;
        int aux2=n-1;
        int aux3=m+1;
        int aux4=m-1;
       
        if (aux1==N)
        {
            aux1=0;
        }
        if (aux2==-1)
        {
            aux2=N-1;
        }
        if (aux3==N)
        {
            aux3=0;
        }
        if (aux4==-1)
        {
            aux4=N-1;
        }

        double de=2*matriz[n][m]*(matriz[aux1][m]+matriz[aux2][m]+matriz[n][aux3]+matriz[n][aux4]);
        double p;

        if(1<exp(-de/T))
        {
            p=1;
        }
         if(1>exp(-de/T))
        {
            p=exp(-de/T);
        }

        double x = ((double) rand())/((double) RAND_MAX);
        if(x<p)
        {
            matriz[n][m]=-matriz[n][m];
        }

        

        if(d==100*pow(N,2))
        {
            for(int i=0;i<N;i++)
            {
                for(int j=0;j<N;j++)
                {
                    if (j<N-1)
                    {
                        //fichero << matriz[i][j]<<", ";
                        fprintf(fichero,"%d," , matriz[i][j]);
                    }

                    else
                    {
                        //fichero<<matriz[i][j+1]<<endl;
                        fprintf(fichero,"%d \n" , matriz[i][j]);
                    }    
            
                }
                
            }
            fprintf(fichero,"\n");
            d=0;
        }
        else
        {
            d=d+1;
        }
        
        

    }


    fclose(fichero);

    return 0;
}