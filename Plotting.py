import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np
from pylab import *

orbital_7 = open("OH 270 7.txt","r")
MP2_7 = open("OH MP2 7.txt","r")
orbital_8 = open("OH 270 8.txt","r")
MP2_8 = open("OH MP2 8.txt","r")
orbital_9 = open("OH 270 9.txt","r")
MP2_9 = open("OH MP2 9.txt","r")
orbital_10 = open("OH 270 10.txt","r")
MP2_10 = open("OH MP2 10.txt","r")

# read in all data as one long string
orbital_data_7 = orbital_7.read()
MP2_data_7 = MP2_7.read()
orbital_data_8 = orbital_8.read()
MP2_data_8 = MP2_8.read()
orbital_data_9 = orbital_9.read()
MP2_data_9 = MP2_9.read()
orbital_data_10 = orbital_10.read()
MP2_data_10 = MP2_10.read()

orbital_data_7 = orbital_data_7.replace("  ", " ")
orbital_data_7 = orbital_data_7.replace("\n", "")
orbital_data_7 = orbital_data_7.replace("E", "e")
spin_orbital_7 = orbital_data_7.split(" ")
spin_orbital_spin_7 = spin_orbital_7

orbital_data_8 = orbital_data_8.replace("  ", " ")
orbital_data_8 = orbital_data_8.replace("\n", "")
orbital_data_8 = orbital_data_8.replace("E", "e")
spin_orbital_8 = orbital_data_8.split(" ")
spin_orbital_spin_8 = spin_orbital_8

orbital_data_9 = orbital_data_9.replace("  ", " ")
orbital_data_9 = orbital_data_9.replace("\n", "")
orbital_data_9 = orbital_data_9.replace("E", "e")
spin_orbital_9 = orbital_data_9.split(" ")
spin_orbital_spin_9 = spin_orbital_9

orbital_data_10 = orbital_data_10.replace("  ", " ")
orbital_data_10 = orbital_data_10.replace("\n","")
orbital_data_10 = orbital_data_10.replace("E", "e")
spin_orbital_10 = orbital_data_10.split(" ")
spin_orbital_spin_10 = spin_orbital_10

MP2_data_7 = MP2_data_7.replace("  ", " ")
MP2_data_7 = MP2_data_7.replace("\n", "")
MP2_data_7 = MP2_data_7.replace("E", "e")
spin_MP2_7 = MP2_data_7.split(" ")

MP2_data_8 = MP2_data_8.replace("  ", " ")
MP2_data_8 = MP2_data_8.replace("\n", "")
MP2_data_8 = MP2_data_8.replace("E", "e")
spin_MP2_8 = MP2_data_8.split(" ")

MP2_data_9 = MP2_data_9.replace("  ", " ")
MP2_data_9 = MP2_data_9.replace("\n", "")
MP2_data_9 = MP2_data_9.replace("E", "e")
spin_MP2_9 = MP2_data_9.split(" ")

MP2_data_10 = MP2_data_10.replace("  ", " ")
MP2_data_10 = MP2_data_10.replace("\n", "")
MP2_data_10 = MP2_data_10.replace("E", "e")
spin_MP2_10 = MP2_data_10.split(" ")

for i in range(len(spin_orbital_spin_7)):
    spin_orbital_spin_7[i] = float(spin_orbital_spin_7[i])
    #spin_orbital_spin_7[i] = spin_orbital_spin_7[i]*spin_orbital_spin_7[i]
for i in range(1000):
    spin_MP2_7[i] = float(spin_MP2_7[i])
spin_MP2_7 = spin_MP2_7[::2]
for i in range(len(spin_orbital_spin_8)):
    spin_orbital_spin_8[i] = float(spin_orbital_spin_8[i])
    #spin_orbital_spin_8[i] = spin_orbital_spin_8[i]*spin_orbital_spin_8[i]
for i in range(1000):
    spin_MP2_8[i] = float(spin_MP2_8[i])
spin_MP2_8 = spin_MP2_8[::2]
for i in range(len(spin_orbital_spin_9)):
    spin_orbital_spin_9[i] = float(spin_orbital_spin_9[i])
    #spin_orbital_spin_9[i] = spin_orbital_spin_9[i]*spin_orbital_spin_9[i]
for i in range(1000):
    spin_MP2_9[i] = float(spin_MP2_9[i])
spin_MP2_9 = spin_MP2_9[::2]
for i in range(len(spin_orbital_spin_10)):
    spin_orbital_spin_10[i] = float(spin_orbital_spin_10[i])
    #spin_orbital_spin_10[i] = spin_orbital_spin_10[i]*spin_orbital_spin_10[i]
for i in range(1000):
    spin_MP2_10[i] = float(spin_MP2_10[i])
spin_MP2_10 = spin_MP2_10[::2]

#pruning MP2 data
x1 = np.arange(-20,20,0.04)
x2 = np.arange(-20,20,0.08)
b7 = (max(x2)-min(x2))**2 / (max(spin_MP2_7)-min(spin_MP2_7))**2
b8 = (max(x2)-min(x2))**2 / (max(spin_MP2_8)-min(spin_MP2_8))**2
b9 = (max(x2)-min(x2))**2 / (max(spin_MP2_9)-min(spin_MP2_9))**2
b10 = (max(x2)-min(x2))**2 / (max(spin_MP2_10)-min(spin_MP2_10))**2

for i in range(1,len(spin_MP2_7)):
    for j in range(i):
        z = (x2[i] - x2[j])**2 + b7*(spin_MP2_7[i] - spin_MP2_7[j])**2
        if z < 5:
            spin_MP2_7[i] = -100

for i in range(1,len(spin_MP2_8)):
    for j in range(i):
        z = (x2[i] - x2[j])**2 + b8*(spin_MP2_8[i] - spin_MP2_8[j])**2
        if z < 5:
            spin_MP2_8[i] = -100

for i in range(1,len(spin_MP2_9)):
    for j in range(i):
        z = (x2[i] - x2[j])**2 + b9*(spin_MP2_9[i] - spin_MP2_9[j])**2
        if z < 5:
            spin_MP2_9[i] = -100

for i in range(1,len(spin_MP2_10)):
    for j in range(i):
        z = (x2[i] - x2[j])**2 + b10*(spin_MP2_10[i] - spin_MP2_10[j])**2
        if z < 5:
            spin_MP2_10[i] = -100


#for i in range(1,len(spin_MP2_7)):
#    j = i
#    while spin_MP2_7[j-1] == -100:
#        j -= 1
#    z = (x2[i] - x2[j-1])**2 + b7*(spin_MP2_7[i] - spin_MP2_7[j-1])**2
#    print(z)
#    if z < 9:
#        spin_MP2_7[i] = -100

for i in range(1,len(spin_MP2_8)):
    j = i
    while spin_MP2_8[j-1] == -100:
        j -= 1
    z = (x1[i] - x1[j-1])**2 + b8*(spin_MP2_8[i] - spin_MP2_8[j-1])**2
    if z < 9:
        spin_MP2_8[i] = -100

for i in range(1,len(spin_MP2_9)):
    j = i
    while spin_MP2_9[j-1] == -100:
        j -= 1
    z = (x1[i] - x1[j-1])**2 + b9*(spin_MP2_9[i] - spin_MP2_9[j-1])**2
    if z < 9:
        spin_MP2_9[i] = -100

for i in range(1,len(spin_MP2_10)):
    j = i
    while spin_MP2_10[j-1] == -100:
        j -= 1
    z = (x2[i] - x2[j-1])**2 + b10*(spin_MP2_10[i] - spin_MP2_10[j-1])**2
    if z < 9:
        spin_MP2_10[i] = -100

for i in range(len(spin_MP2_7)):
    spin_MP2_7[i] = 1000 * spin_MP2_7[i]
for i in range(len(spin_MP2_8)):
    spin_MP2_8[i] = 1000 * spin_MP2_8[i]
for i in range(len(spin_MP2_9)):
    spin_MP2_9[i] = 1000 * spin_MP2_9[i]
for i in range(len(spin_MP2_10)):
    spin_MP2_10[i] = 1000 * spin_MP2_10[i]
for i in range(len(spin_orbital_spin_7)):
    spin_orbital_spin_7[i] = 1000*spin_orbital_spin_7[i]
for i in range(len(spin_orbital_spin_8)):
    spin_orbital_spin_8[i] = 1000*spin_orbital_spin_8[i]
for i in range(len(spin_orbital_spin_9)):
    spin_orbital_spin_9[i] = 1000*spin_orbital_spin_9[i]
for i in range(len(spin_orbital_spin_10)):
    spin_orbital_spin_10[i] = 1000*spin_orbital_spin_10[i]
    

# close the file
orbital_7.close()
MP2_7.close
orbital_8.close()
MP2_8.close
orbital_9.close()
MP2_9.close
orbital_10.close()
MP2_10.close

#Plotting section
plt.rcParams['figure.figsize'] = (3.3, 6.6)
plt.rcParams['xtick.direction'] = 'in'#将x周的刻度线方向设置向内
plt.rcParams['ytick.direction'] = 'in'#将y轴的刻度方向设置向内

xminorLocator = MultipleLocator(5)
sminorLocator = MultipleLocator(2)
sminorLocator2 = MultipleLocator(1)
yminorLocator = MultipleLocator(0.25)
s_major_locator=MultipleLocator(4)
s_minor_locator=MultipleLocator(2)
y_major_locator=MultipleLocator(0.5)
pot_7 = .5*(10**-7)*(x1**8) - 0.015167*x1
pot_8 = .5*(10**-8)*(x1**8) - 0.015167*x1
pot_9 = .5*(10**-9)*(x1**8) - 0.015167*x1
pot_10 = .5*(10**-10)*(x1**8) - 0.015167*x1

#Setting 4 subplots and axis labels
fig, axs = plt.subplots(4, sharex=True, sharey=False, gridspec_kw={'hspace': 0})
plt.xlabel("z displacement (Bohr)")

#confining potential -7
minorticks_on()
axs[0].set_ylim([-3,15])
axs[0].xaxis.set_minor_locator(xminorLocator)
axs[0].plot(x1, spin_orbital_spin_7, label = 'line', color = 'black',linewidth=0.75) 
axs[0].plot(x2,spin_MP2_7,'o',markerfacecolor='none',color = 'black',markersize=2)
spin_orbital_spin_7, = axs[0].plot(x1,spin_orbital_spin_7, label = 'line', color = 'black',linewidth=0.75)
spin_MP2_7, = axs[0].plot(x2,spin_MP2_7,'o',markerfacecolor='none',color = 'black',markersize=2)
ax2 = axs[0].twinx()
ax2.tick_params(axis='y',colors='blue')
ax2.set_ylim([-0.2,1])
axs[0].tick_params(axis='x',which='both',top='on',bottom='on')
ax2.plot(x1,pot_7,linestyle=':',color='blue',linewidth=0.75)
ax2.yaxis.set_major_locator(y_major_locator)
ax2.yaxis.set_minor_locator(yminorLocator)
axs[0].yaxis.set_major_locator(s_major_locator)
axs[0].yaxis.set_minor_locator(sminorLocator)
ax2.text( -18, 0.8,'(a) $k_z$=$10^{-7}$', fontsize=8,bbox=dict(boxstyle='square',edgecolor='white',facecolor='white',alpha=0.7))
ax2.text( -22, 1.0,'$X10^{-3}$', fontsize=8)
ax2.legend(handles=[spin_orbital_spin_7, spin_MP2_7],labels=["wPBEh","MP2"],loc='upper right',fontsize=8,edgecolor='black',facecolor='white',framealpha = 1,fancybox=True)
 #confining potential -8
axs[1].set_ylim([-3,15])
axs[1].plot(x1, spin_orbital_spin_8, label = 'line', color = 'black',linewidth=0.75)
axs[1].plot(x2,spin_MP2_8,'o',markerfacecolor='none',color = 'black',markersize=2)
ax2 = axs[1].twinx()
ax2.tick_params(axis='y',colors='blue')
ax2.set_ylim([-0.2,1])
axs[1].xaxis.set_minor_locator(xminorLocator)
axs[1].tick_params(axis='x',which='both',top='on',bottom='on')
ax2.plot(x1,pot_8,linestyle=':',color='blue',linewidth=0.75)
ax2.set_ylabel('Confining Potential (Hartree)',color='blue')
axs[1].set_ylabel("Spin Density (Bohr$^{-3}$)",labelpad=-5)
ax2.yaxis.set_major_locator(y_major_locator)
ax2.yaxis.set_minor_locator(yminorLocator)
axs[1].yaxis.set_major_locator(s_major_locator)
axs[1].yaxis.set_minor_locator(sminorLocator)
ax2.text( -18, 0.8,'(b) $k_z$=$10^{-8}$', fontsize=8,bbox=dict(boxstyle='square',edgecolor='white',facecolor='white',alpha=0.7))
#confining potential -9
axs[2].set_ylim([-1,5])
axs[2].plot(x1, spin_orbital_spin_9, label = 'line', color = 'black',linewidth=0.75) 
axs[2].plot(x2,spin_MP2_9,'o',markerfacecolor='none',color = 'black',markersize=2)
ax2 = axs[2].twinx()
ax2.tick_params(axis='y',colors='blue')
ax2.set_ylim([-0.2,1])
axs[2].xaxis.set_minor_locator(xminorLocator)
axs[2].tick_params(axis='x',which='both',top='on',bottom='on')
ax2.plot(x1,pot_9,linestyle=':',color='blue',linewidth=1)
ax2.yaxis.set_major_locator(y_major_locator)
ax2.yaxis.set_minor_locator(yminorLocator)
axs[2].yaxis.set_major_locator(s_minor_locator)
axs[2].yaxis.set_minor_locator(sminorLocator2)
ax2.text( -18, 0.8,'(c) $k_z$=$10^{-9}$', fontsize=8,bbox=dict(boxstyle='square',edgecolor='white',facecolor='white',alpha=0.7))
#confining potential -10
axs[3].set_xlim([-20,20])
axs[3].xaxis.set_minor_locator(xminorLocator)
axs[3].set_ylim([-1,5])
axs[3].plot(x1, spin_orbital_spin_10, label = 'line', color = 'black',linewidth=0.75) 
axs[3].plot(x2,spin_MP2_10,'o',markerfacecolor='none',color = 'black',markersize=2)
ax2 = axs[3].twinx()
ax2.tick_params(axis='y',colors='blue')
ax2.set_ylim([-0.2,1])
axs[3].xaxis.set_minor_locator(xminorLocator)
axs[3].tick_params(axis='x',which='both',top='on',bottom='on')
ax2.plot(x1,pot_10,linestyle=':',color='blue',linewidth=1)
ax2.yaxis.set_major_locator(y_major_locator)
ax2.yaxis.set_minor_locator(yminorLocator)
axs[3].yaxis.set_major_locator(s_minor_locator)
axs[3].yaxis.set_minor_locator(sminorLocator2)
ax2.text( -18, 0.8,'(d) $k_z$=$10^{-10}$', fontsize=8,bbox=dict(boxstyle='square',edgecolor='white',facecolor='white',alpha=0.7))

for ax in axs:
    ax.label_outer()


plt.subplots_adjust(left=0.2, bottom=0.1, right=0.8, top=0.95,hspace=0.1,wspace=0.1)

plt.draw()  # 显示绘图
plt.savefig("OH w270 neut.pdf")  #保存图象
plt.pause(5)
#plt.show()
plt.close()