#include <iostream>
# include <stdio.h>
# include <math.h>
#include <fstream>
#include <cstdlib>

using namespace std;

int main()
{
    int N=100;
    float T=2.2;


    int matriz[N][N];

    //num=1+rand()%(101-1);

 
    FILE* fichero= fopen("ising_data.dat","a");

    for ( int i = 0; i< N ; i++)
    {
        for (int j=0 ; j<N; j++)
        {
            int y=1+rand()%(2);
            matriz[i][j]=pow(-1,y);
            cout << matriz[i][j];
        }
    }


    for (int l=0;l<N;l++)
    {
        for (int k=0;k<pow(N,2);k++)
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


            float de= 2*matriz[n][m]*(matriz[aux1][m]+matriz[aux2][m]+matriz[n][aux3]+matriz[n][aux4]);
            float p;
            
            if(1<exp(de/T))
            {
                p=1;
            }

            if(1>exp(de/T))
            {
                p=exp(de/T);
            }

            double x=(double) rand() /RAND_MAX;
            
            if(x<p)
            {
                matriz[n][m]=-matriz[n][m];
            }
            
        }

        for (int i=0;i<N;i++)
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

        //fichero << endl;
        fprintf(fichero,"\n");
       
    }

    //fichero.close();  
    fclose(fichero);

    return 0;
}





