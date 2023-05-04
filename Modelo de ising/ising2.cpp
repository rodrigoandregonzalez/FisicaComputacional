# include <stdio.h>
# include <math.h>
# include "gsl_rng.h" 

gsl_rng *tau;

using namespace std;

int main()
{
    int N=100;  //filas y columnas de la matriz de espin
    double T=0.01; //Temperatura 

    int matriz[N][N]; //definimos matriz

    int semilla=177013;
    tau=gsl_rng_alloc(gsl_rng_taus);
    gsl_rng_set(tau,semilla);


    FILE* fichero= fopen("ising_data.dat","a");

    for (int l=0; l<N; l++) //SPINES ALEATORIOS 
    {
        for (int k=0; k<N; k++)
        {
            int y=gsl_rng_uniform_int(tau,2);  //número aleatorio entero [0,1]

            matriz[l][k]=pow(-1,y);

        }
    } 


    for (int a=0;a<N*N;a++)
    {
        for(int b=0;b<N*N;b++)
        {
            int n=gsl_rng_uniform_int(tau,N); 
            int m=gsl_rng_uniform_int(tau,N); 
            
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


            double DE=2*matriz[n][m]*(matriz[aux1][m]+matriz[aux2][m]+matriz[n][aux3]+matriz[n][aux4]);
            double p;

            if (1<exp(-DE/T))
            {
                p=1;
            }

            if (1>exp(-DE/T))
            {
                p=exp(-DE/T);
            }
        
            double x=gsl_rng_uniform(tau);
            printf("%f",x);
            if(x<p)
            {
                matriz[n][m]=-matriz[n][m];
            }
        
        }

        for (int i=0;i<N;i++)
        {
            for (int j=0;j<N;j++)
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


    }

    fclose(fichero);

    return 0;
}








