import numpy as np
import matplotlib.pyplot as plt


def recta(x,a,b):
    return a+b*x

x=np.array([1.5,1.7,1.9,2.1,2.3,2.5,2.7,2.9,3.1,3.3])
N=10000


##########################################################################
#N=16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 16 
'''
#MAGNETIZACION
y=np.array([0.986363,0.970283,0.938573,0.869509,0.675744,0.392659,0.252065,0.192716,0.157929,0.138862])
sy=np.array([0.973928,0.943697,0.887106,0.786270,0.628503,0.360519,0.185131,0.113804,0.078948,0.061514])

sy=2*np.sqrt(sy/10000)


fig,ax=plt.subplots(1,1)

ax.tick_params(axis='x',length=6, width=1,labelsize=15)
ax.tick_params(axis='y',length=6, width=1,labelsize=15)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('$T$',fontsize=20)
ax.set_ylabel('$m_N(T)$',fontsize=20)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3,label='Error N=16')
ax.plot(x,y,color='blue')



axins=ax.inset_axes([0.1,0.15,0.1,0.15])
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=1.4998,1.5002,0.98633,0.98644
axins.set_xlim(x1,x2)
axins.set_ylim(y1,y2)
axins.grid()
axins.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins,edgecolor='black')


axins2=ax.inset_axes([0.26,0.16,0.1,0.15])
axins2.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=1.6998,1.7002,0.9695,0.9705
axins2.set_xlim(x1,x2)
axins2.set_ylim(y1,y2)
axins2.grid()
axins2.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins2,edgecolor='black')


axins3=ax.inset_axes([0.5,0.8,0.1,0.15])
axins3.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=1.8998,1.9002,0.9375,0.939
axins3.set_xlim(x1,x2)
axins3.set_ylim(y1,y2)
axins3.grid()
axins3.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins3,edgecolor='black')


axins4=ax.inset_axes([0.7,0.4,0.1,0.15])
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=2.0998,2.1002,0.868,0.87
axins4.set_xlim(x1,x2)
axins4.set_ylim(y1,y2)
axins4.grid()
axins4.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins4,edgecolor='black')


#N=32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 
#MAGNETIZACION
y=np.array([0.986367,0.970022,0.938312, 0.868840,0.570438,0.200778,0.122177,0.093219,0.077577,0.068282])
sy=np.array([0.973469,0.941881,0.882334,0.763014,0.492971,0.121396,0.048547,0.028504,0.019363,0.015185])

sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3,label='Error N=32')
ax.plot(x,y,color='red')

axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
axins2.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
axins3.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)

#N=64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64
y=np.array([0.986344,0.969899, 0.938125,0.868683, 0.449221,0.099693, 0.061041,0.046981,0.039028,0.034062])
sy=np.array([0.973303,0.941293,0.880891, 0.756938,0.355150 ,0.032134,0.012156,0.007223, 0.004998 ,0.003797])

sy=2*np.sqrt(sy/10000)


ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3,label='Error N=64')
ax.plot(x,y,color='green')
plt.legend(fontsize=15)
plt.grid(True)
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)
axins2.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)
axins3.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)


#N=128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 
y=np.array([0.986428,0.969998,0.938285,0.868857,0.285705, 0.049019,0.030516,0.023261, 0.019714,0.016854])
sy=np.array([0.973440,0.941399,0.880917,0.755774,0.198898,0.007836, 0.003049,0.001808 ,0.001283,0.000939 ])

sy=2*np.sqrt(sy/10000)


ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3,label='Error N=128')
ax.plot(x,y,color='purple')
plt.legend(fontsize=15)
plt.grid(True)
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3)
axins2.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3)
axins3.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3)
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3)
plt.show()
'''


'''
#ENERGIA MEDIA
y=np.array([-15.542590,-15.127107,-14.417002,-13.250893,-11.254504,-9.043109, -7.751721,-6.897768,-6.247492,-5.718821])
sy=np.array([ 4.331964,8.644271, 17.187422,35.321197,64.751266, 54.612119, 36.847174,30.804470,28.152605,25.696548 ])
sy=2*np.sqrt(sy/10000)

fig,ax=plt.subplots(1,1)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3,label='Error N=16')
ax.plot(x,y,color='blue')


#N=32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 
#ENERGIA MEDIA
y=np.array([-31.182570,-30.341687,-28.925259,-26.569536,-22.016130,-17.725238,-15.412276,-13.776893,-12.460838,-11.427416])
sy=np.array([13.332723,21.762719,37.679435,73.039892,161.270799,92.916880,72.543778,62.421512,55.674799,50.559215])
sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3,label='Error N=32')
ax.plot(x,y,color='red')


#N=64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 
#ENERGIA MEDIA
y=np.array([-62.407935,-60.713742,-57.875386,-53.166267,-43.468387,-35.369133,-30.832509,-27.517853, -24.931200,-22.846740])
sy=np.array([64.011334,79.085778,107.375630,172.995672 ,381.404256,190.523309,148.869698 ,134.377970 ,116.920144 , 108.492384])
sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3,label='Error N=64')
ax.plot(x,y,color='green')


#N=128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 
#en
y=np.array([-124.855714,-121.464884,-115.792468,-106.368156,-86.190654,-70.784198,-61.647652,-55.023907,-49.875352,-45.700054])
sy=np.array([427.152033,440.510633 ,472.253671,556.408054,920.709539, 470.789810 ,371.116861,319.708906, 281.464096 ,260.071745])
sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3,label='Error N=128')
ax.tick_params(axis='x',length=6, width=1,labelsize=15)
ax.tick_params(axis='y',length=6, width=1,labelsize=15)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')
ax.plot(x,y,color='purple')
ax.set_xlabel('$T$',fontsize=20)
ax.set_ylabel('$e_N(T)$',fontsize=20)



plt.legend(fontsize=25)
plt.grid(True)

plt.show()
'''




'''
#CALOR ESPECIFICO
y=np.array([0.360997,0.635576,1.130695,2.102350,3.518899,2.730282,1.705635,1.327620,1.135061,0.973247])
sy=np.array([ 0.130319 ,0.403970,1.278511,4.420003,12.383089,7.455679, 2.909936,1.762866,1.288541,0.947339])
sy=2*np.sqrt(sy/10000)

fig,ax=plt.subplots(1,1)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3,label='Error N=16')
ax.plot(x,y,color='blue')

axins=ax.inset_axes([0.4,0.1,0.1,0.15])
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=2.6998,2.7002,1.66,1.75
axins.set_xlim(x1,x2)
axins.set_ylim(y1,y2)
axins.grid()
axins.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins,edgecolor='black')

axins2=ax.inset_axes([0.55,0.8,0.1,0.15])
axins2.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=2.8998,2.9002,1.30,1.375
axins2.set_xlim(x1,x2)
axins2.set_ylim(y1,y2)
axins2.grid()
axins2.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins2,edgecolor='black')

axins3=ax.inset_axes([0.72,0.62,0.1,0.15])
axins3.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=3.0998,3.1002,1.10,1.15
axins3.set_xlim(x1,x2)
axins3.set_ylim(y1,y2)
axins3.grid()
axins3.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins3,edgecolor='black')

axins4=ax.inset_axes([0.85,0.4,0.1,0.15])
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=3.2998,3.3002,0.94,1.05
axins4.set_xlim(x1,x2)
axins4.set_ylim(y1,y2)
axins4.grid()
axins4.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins4,edgecolor='black')

#N=32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 
#CALOR ESPECIFICO
y=np.array([0.555530, 0.800051,1.239384,2.173694,4.382160,2.322519,1.679039,1.345135,1.122350, 0.957455])
sy=np.array([0.308614, 0.640112,1.536135,4.725100,19.203800,5.396014 ,2.819712,1.809670,1.259850 ,0.916847 ])
sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3,label='Error N=32')
ax.plot(x,y,color='red')
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
axins2.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
axins3.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)

#N=64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 
#CALOR ESPECIFICO
y=np.array([1.333569,1.453665, 1.765916,2.574181,5.181888,2.381065,1.722808,1.447878,1.178495,1.027279])
sy=np.array([1.778408,2.113320,3.118672 , 6.626717 ,26.852626 ,5.672154 ,2.968636,2.096648 , 1.389060, 1.055442 ])
sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3,label='Error N=64')
ax.plot(x,y,color='green')
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)

#N=128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 
#cn
y=np.array([4.449500,4.048418, 3.883303,4.139589,6.254442,2.941861,2.147395, 1.722370,1.418509,1.231267])
sy=np.array([19.798053 ,16.391671 ,15.081680,17.137709,39.119762,8.658457,4.612169 ,2.967018,2.012464 ,1.516220 ])
sy=2*np.sqrt(sy/10000)

ax.tick_params(axis='x',length=6, width=1,labelsize=15)
ax.tick_params(axis='y',length=6, width=1,labelsize=15)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('$T$',fontsize=20)
ax.set_ylabel('$c_N(T)$',fontsize=20)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3,label='Error N=128')
ax.plot(x,y,color='purple')

plt.legend(fontsize=15)
plt.grid(True)
plt.show()
'''

'''
#FUNCION DE CORRELACION
y=np.array([0.975294, 0.949230,0.904719,0.831628,0.706136,0.566983,0.485564,0.432267,0.391380,0.358294])
sy=np.array([0.000542,0.001104,0.002230,0.004605, 0.008569 ,0.007673,0.005695,0.005006,0.004811,0.004556])
sy=2*np.sqrt(sy/10000)

fig,ax=plt.subplots(1,1)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3,label='Error N=16')
ax.plot(x,y,color='blue')

axins=ax.inset_axes([0.07,0.65,0.1,0.15])
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=1.4998,1.5002,0.9752,0.9756
axins.set_xlim(x1,x2)
axins.set_ylim(y1,y2)
axins.grid()
axins.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins,edgecolor='black')

axins4=ax.inset_axes([0.8,0.3,0.1,0.15])
axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3)
x1,x2,y1,y2=3.2998,3.3002,0.3565,0.3585
axins4.set_xlim(x1,x2)
axins4.set_ylim(y1,y2)
axins4.grid()
axins4.tick_params(which='both',direction='in',top='on',right='on')
ax.indicate_inset_zoom(axins4,edgecolor='black')

#N=32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 32 
#FUNCION DE CORRELACION
y=np.array([0.975405,0.949127,0.904922,0.831106,0.688670,0.554205,0.481534,0.430664,0.389475,0.357149])
sy=np.array([0.000207 ,0.000346 ,0.000605,0.001176,0.002614,0.001649, 0.001379,0.001264,0.001162,0.001129])
sy=2*np.sqrt(sy/10000)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3,label='Error N=32')
ax.plot(x,y,color='red')
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)

axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3)
#N=64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 64 
#FUNCION DE CORRELACION
y=np.array([0.975381,0.948933, 0.904540,0.831002,0.679287,0.552720,0.481781, 0.429778,0.389524,0.356918])
sy=np.array([ 0.000123 , 0.000153 ,0.000211,0.000346 ,0.000761 ,0.000423, 0.000352 ,0.000335,0.000310 , 0.000294 ])
sy=2*np.sqrt(sy/10000)


ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3,label='Error N=64')
ax.plot(x,y,color='green')
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)

axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3)
#N=128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 128 
#fi
y=np.array([ 0.975491,0.948996,0.904684,0.831060, 0.673336,0.552988,0.481627,0.429877,0.389604, 0.357025])
sy=np.array([0.000102 ,0.000106,0.000114, 0.000137,0.000230 ,0.000127,0.000104,0.000097 ,0.000088 ,0.000083 ])
sy=2*np.sqrt(sy/10000)

ax.tick_params(axis='x',length=6, width=1,labelsize=15)
ax.tick_params(axis='y',length=6, width=1,labelsize=15)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('$T$',fontsize=20)
ax.set_ylabel('$f(i)$',fontsize=20)

ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3,label='Error N=128')
ax.plot(x,y,color='purple')
axins.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3)

axins4.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3)
plt.legend(fontsize=25)
plt.grid(True)
plt.show()'''







'''
##########################################
#Calculo de beta

#vamos a hacer una regresion y=b*x coomo ln(mn)=beta*ln(t)

tc=2.3
t=np.array([1.5, 1.7, 1.9, 2.1])
x=np.log(-(t-tc)/tc)


mn=np.array([0.986363, 0.970283, 0.938573,0.869509])

y=np.log(mn)

sy=np.array([0.973928,0.943697,0.887106,0.786270])
sy=2*np.sqrt(sy/10000)/mn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))

fig,ax=plt.subplots(1,1)

ax.plot(x,recta(x,a,b),color='blue',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3,label='Error N=16')

print('b 16: ',b)
print('a 16 : ',a)
print('sb 16: ',sb)
print('r 16:',r)
ax.tick_params(axis='x',length=6, width=1,labelsize=20)
ax.tick_params(axis='y',length=6, width=1,labelsize=20)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('ln($t$)',fontsize=30)
ax.set_ylabel('ln($m_N$)',fontsize=30)

plt.legend(fontsize=25)
plt.grid(True)
plt.show()
####################
# N=32

mn=np.array([0.986367, 0.970022, 0.938312, 0.868840])
y=np.log(mn)

sy=np.array([0.973469,0.941881,0.882334,0.763014])
sy=2*np.sqrt(sy/10000)/mn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))

fig,ax=plt.subplots(1,1)

ax.plot(x,recta(x,a,b),color='red',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3,label='Error N=32')

print('b 32: ',b)
print('a 32: ',a)
print('sb 32: ',sb)
print('r 32:',r)
ax.tick_params(axis='x',length=6, width=1,labelsize=20)
ax.tick_params(axis='y',length=6, width=1,labelsize=20)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('ln($t$)',fontsize=30)
ax.set_ylabel('ln($m_N$)',fontsize=30)

plt.legend(fontsize=25)
plt.grid(True)
plt.show()
####################
# N=64

mn=np.array([0.986344,0.969899, 0.938125,0.868683])
y=np.log(mn)

sy=np.array([0.973303,0.941293,0.880891, 0.756938])
sy=2*np.sqrt(sy/10000)/mn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))

fig,ax=plt.subplots(1,1)

ax.plot(x,recta(x,a,b),color='green',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3,label='Error N=64')

print('b 64: ',b)
print('a 64: ',a)
print('sb 64: ',sb)
print('r 64:',r)
ax.tick_params(axis='x',length=6, width=1,labelsize=20)
ax.tick_params(axis='y',length=6, width=1,labelsize=20)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('ln($t$)',fontsize=30)
ax.set_ylabel('ln($m_N$)',fontsize=30)

plt.legend(fontsize=25)
plt.grid(True)
plt.show()

####################
# N=128

mn=np.array([0.986428,0.969998,0.938285,0.868857])
y=np.log(mn)

sy=np.array([0.973440,0.941399,0.880917,0.755774])
sy=2*np.sqrt(sy/10000)/mn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))

fig,ax=plt.subplots(1,1)

ax.plot(x,recta(x,a,b),color='purple',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3,label='Error N=128')

print('b 128: ',b)
print('a 128: ',a)
print('sb 128: ',sb)
print('r 128:',r)




#REPRESENTAMOS
ax.tick_params(axis='x',length=6, width=1,labelsize=20)
ax.tick_params(axis='y',length=6, width=1,labelsize=20)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('ln($t$)',fontsize=30)
ax.set_ylabel('ln($m_N$)',fontsize=30)

plt.legend(fontsize=25)
plt.grid(True)
plt.show()

def mediaaritmetica(x,sx):
    w=1/(sx)**2 #Peso estadistico

    mmx=(np.sum(x*w))/(np.sum(w)) #Valor medio de x
    scx=1/(np.sqrt(np.sum(w))) #Incertidumbre de x

    return mmx,scx


betas=np.array([0.0924,0.0930,0.0931,0.0930])
sbetas=np.array([0.008,0.008,0.0079,0.008])
beta,sbeta=mediaaritmetica(betas,sbetas)

print('beta: ',beta)
print('sbeta: ', sbeta)
'''


##########################################
#Calculo de alfa

#vamos a hacer una regresion y=b*x coomo ln(mn)=beta*ln(t)

tc=2.3
t=np.array([2.5,2.7,2.9,3.1,3.3])
x=np.log((t-tc)/tc)


cn=np.array([2.730282,1.705635,1.327620,1.135061,0.973247])

y=np.log(cn)

sy=np.array([7.455679, 2.909936,1.762866, 1.288541,0.947339   ])
sy=2*np.sqrt(sy/10000)/cn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))

fig,ax=plt.subplots(1,1)

ax.plot(x,recta(x,a,b),color='blue',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='blue',ecolor='blue', capsize=3,label='Error N=16')

print('b 16: ',b)
print('a 16 : ',a)
print('sb 16: ',sb)
print('r 16:',r)


##########################3
#N=32 32 32 32 32 32 32
cn=np.array([2.322519,1.679039,1.345135,1.122350,0.957455])

y=np.log(cn)

sy=np.array([5.396014,2.819712,1.809670,1.259850, 0.916847  ])
sy=2*np.sqrt(sy/10000)/cn

n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))



ax.plot(x,recta(x,a,b),color='red',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='red',ecolor='red', capsize=3,label='Error N=32')

print('b 32: ',b)
print('a 32: ',a)
print('sb 32: ',sb)
print('r 32:',r)





###################
#N=64 64 64 64 64 64

cn=np.array([ 2.381065,1.722808,1.447878,1.178495,1.027279])
y=np.log(cn)

sy=np.array([5.672154,2.968636,2.096648,1.389060, 1.055442  ])
sy=2*np.sqrt(sy/10000)/cn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))


ax.plot(x,recta(x,a,b),color='green',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='green',ecolor='green', capsize=3,label='Error N=64')

print('b 64: ',b)
print('a 64: ',a)
print('sb 64: ',sb)
print('r 64:',r)


####################
# N=128

cn=np.array([2.941861,2.147395,1.722370, 1.418509,1.231267])
y=np.log(cn)

sy=np.array([8.658457,4.612169,2.967018,2.012464,1.516220 ])
sy=2*np.sqrt(sy/10000)/cn


n=len(y)

a=(np.sum(y)*np.sum(x**2)-np.sum(x)*np.sum(x*y))/(n*np.sum(x**2)-np.sum(x)**2)
b=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(n*np.sum(x**2)-np.sum(x)**2)

s=np.sqrt((np.sum((y-a-b*x)**2))/(n-2))

sa=s*(np.sqrt((np.sum(x**2))/(n*np.sum(x**2)-np.sum(x)**2)))
sb=s*(np.sqrt((n)/(n*np.sum(x**2)-np.sum(x)**2)))
r=(n*np.sum(x*y)-np.sum(x)*np.sum(y))/(np.sqrt((n*np.sum(x**2)-np.sum(x)**2)*(n*np.sum(y**2)-np.sum(y)**2)))


ax.plot(x,recta(x,a,b),color='purple',lw=2.)
ax.errorbar(x,y,yerr=sy,linestyle='None', marker='o',color='purple',ecolor='purple', capsize=3,label='Error N=128')

print('b 128: ',b)
print('a 128: ',a)
print('sb 128: ',sb)
print('r 128:',r)


#REPRESENTAMOS
ax.tick_params(axis='x',length=6, width=1,labelsize=20)
ax.tick_params(axis='y',length=6, width=1,labelsize=20)
ax.minorticks_on()
ax.tick_params(which='both',direction='in',top='on',right='on')

ax.set_xlabel('ln($t$)',fontsize=30)
ax.set_ylabel('ln($m_N$)',fontsize=30)

plt.legend(fontsize=25)
plt.grid(True)
plt.show()


def mediaaritmetica(x,sx):
    w=1/(sx)**2 #Peso estadistico

    mmx=(np.sum(x*w))/(np.sum(w)) #Valor medio de x
    scx=1/(np.sqrt(np.sum(w))) #Incertidumbre de x

    return mmx,scx


alfas=np.array([0.635,0.545,0.516,0.540])
salfas=np.array([0.013,0.026,0.029,0.027])
alfa,salfa=mediaaritmetica(alfas,salfas)

print('alfa: ',alfa)
print('salfa: ', salfa)

