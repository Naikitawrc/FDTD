import numpy as np
import math as mt
import matplotlib.pyplot as plt

#GROUND CONDITIONS###########
size=500;maxTime=20000
imp0=377.0
eps=5
dt=3.3e-18
dx=1e-9
c=3e8
Sc=c*dt/dx
print('SCourant',Sc)
#############################
ez=np.zeros((size))
hy=np.zeros((size))
ez_snap=np.zeros((maxTime))
hy_snap=np.zeros((maxTime))
snap_moment=size/2-1
#Source Parameters###########
source_width=10
delay = 20*source_width
#############################
#for snap_moment in range(5,10,1):
i=0
#while (count < 9)
plt.ion()
fig = plt.figure()
for qtime in np.arange(0,maxTime+1,1):

    #print(qtime)
    #Source inizialization############################
    ez[size/2-1] += 0.5*mt.exp(-(qtime-delay) ** 2 / (2.0 * source_width**2));
    ##################################################
    #ABS BOUNDARIES FOR H_FIELD###
    hy[size-1]=hy[size-2]
    ##############################
    for mm in range(0,size-1):
        #update magnetic field
        hy[mm]=hy[mm]+Sc*(ez[mm+1]-ez[mm])/imp0
    #ABS BOUNDARIES FOR E_FIELD###
    ez[0]=ez[1]
    ##############################
    for mm in range(1,size):
         #pdate electric field
        ez[mm] = ez[mm] + Sc*(hy[mm] - hy[mm - 1]) * imp0/eps
    #ez_snap[i]=ez[snap_moment]
    #hy_snap[i]=hy[snap_moment]
   # if((max(ez)>0)&(max(ez)<1e-15)&(qtime>50)): break
    i=i+1
    #if (ez[size/2-1]<-0.99 and ez[size/2-1]>-1) and (hy[size/2-1]<0.1 and hy[size/2-1]>0): break

#PLOT GRAPH#####################
    eZ=plt.plot(range(0,size,1),ez,'-',color='b')
    hY=plt.plot(range(0,size,1),hy*imp0,'-',color='g')
    plt.ylabel('Ez-field, V/m')
    plt.xlabel('x, nm')
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    ax.set_title('Time = {0} ats'.format(qtime))
    plt.ylim([1.1*min([min(ez),min(hy*imp0)]),1.1*max([max(ez),max(hy*imp0)])])
    ax.ticklabel_format(axis='y', style='sci', scilimits=(-2,2))
    plt.show()
    plt.pause(0.00001)
    l1 = eZ.pop(0)
    l1.remove()
    l2 = hY.pop(0)
    l2.remove()
################################

#fig.savefig('/Users/nikitapavlov/Library/Mobile Documents/com~apple~CloudDocs/University/Kostya/step0_inizavanish.pdf')
 #plt.pause(0.5)

