import matplotlib
from pylab import *
import numpy as np
from tkinter import *
import tkinter
import tkinter as tk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import os.path
import time


root = Tk()
root.grid_rowconfigure(0, weight=2)
root.grid_rowconfigure(1, weight=2)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=2)
root.state("zoomed")


#class GUI:
   # def __init__(self, master):

root.title("Capacity")
        #title = Title(master, text = 'Hello')



        #print(pos)
        #print(pos1)
fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
ax5.text(0.35, 0.6, 'Network : ', fontsize=13)


ax5.get_xaxis().set_visible(False)
ax5.get_yaxis().set_visible(False)
fig1.patch.set_facecolor('white')
fig5.patch.set_facecolor('white')
ax5.set_title('Network ')
fig6 = plt.figure()
fig6.patch.set_facecolor('white')
plt.subplot(211)


plt.title('Active Devices')
plt.tick_params(
    axis='both',
    which='both',
    bottom='off',
    top='off',
    left='off',
    right='off',
    labelleft='off',
    labelbottom='off')

plt.subplot(212)
plt.subplot(212)
plt.text(35, 0.7, 'FPS : 2')
plt.text(35, 0.3, 'Battery : 300 minutes left')

plt.tick_params(
    axis='both',
    which='both',
    bottom='off',
    top='off',
    left='off',
    right='off',
    labelleft='off',
    labelbottom='off')
fig6.patch.set_facecolor('white')
plt.title('VR Parameters')
canvas = FigureCanvasTkAgg(fig, root)
canvas1 = FigureCanvasTkAgg(fig1, root)
canvas2 = FigureCanvasTkAgg(fig2, root)
canvas3 = FigureCanvasTkAgg(fig3, root)
canvas4 = FigureCanvasTkAgg(fig6, root)

canvas5 = FigureCanvasTkAgg(fig5, root)

canvas.show()
canvas1.show()
canvas2.show()
canvas3.show()
canvas4.show()
canvas5.show()

        # canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
canvas2.get_tk_widget().grid(row=0, column=0, columnspan=2, sticky='WE')
        # canvas3.get_tk_widget().grid(row=0, column=3)
        # label1.grid(row=0, column = 2)
canvas.get_tk_widget().grid(row=1, column=0)
canvas4.get_tk_widget().grid(row=0, column=2)
canvas1.get_tk_widget().grid(row=1, column=1)
canvas5.get_tk_widget().grid(row=1, column=2)



        #fig3, ax3 = plt.subplots()
plt.xlim(0, 100)

for tic in ax5.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax5.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax4.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax4.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax3.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax3.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax1.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax1.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax2.xaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

for tic in ax2.yaxis.get_major_ticks():
    tic.tick1On = tic.tick2On = False

val = [100, 100, 100, 100]
val2 = [2.6, 20, 59.1, 14.7]
val3 = [97.4, 80, 40.9, 85.3]
print(val)
label = ['DISK', 'MEMORY', 'CPU', 'GPU']
pos = np.arange(len(label))
ax.set_yticks(pos)
ax.set_yticklabels(label)
ax2.set_yticks(pos)
ax2.set_yticklabels(label)
ax1.set_yticks(pos)
ax1.set_yticklabels(label)

if not os.path.exists('C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/fps.txt'):
    pass
            #time.sleep(1)

#if os.path.isfile('C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/fps.txt'):

file1 = open('C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/fps.txt', 'r', encoding="utf8", errors='ignore')

for i in file1:
    if 'samsung SM-G930V' in i:

        ax.barh(pos, val, align='center', height=0.1, color='g')
        ax2.barh(pos, val2, align='center', height=0.1, color='g', label='Host')
        print(pos)
        ax.text(89, 0.1, '32 GB')
        ax.text(91, 1.1, '4 GB')
        ax.text(66, 2.1, '2.15 Ghz + 1.6 Ghz')
        ax.text(74, 2.8, '407.4 GFLOPS')
        ax2.text(3, -0.05, '32 GB')
        ax2.text(21.5, 0.95, '4 GB')
        ax2.text(60, 1.95, '2.15 Ghz + 1.6 Ghz')
        ax2.text(15, 2.95, '407.4 GFLOPS')
        #plt.text(0.35, 0.3, 'Peer 1 :')
        ax1.set_title('Peer 1 :')
        ax.set_xlabel('Percentage')
        ax1.set_xlabel('Percentage')
        ax2.set_xlabel('Percentage')
        ax.set_title('HOST : Samsung S7')
        plt.subplot(211)
        plt.text(0.35, 0.3, 'Peer 1 :')
        ax2.set_title('Collaborative Computing')
        fig.patch.set_facecolor('white')
        fig2.patch.set_facecolor('white')
        fig1.patch.set_facecolor('white')
        ax1.set_yticks(pos)
        ax1.set_yticklabels(['DISK', 'MEMORY', 'CPU', 'GPU'])
        ax1.set_xlim(0,100)
        ax2.set_xlim(0,100)
        plt.subplot(211)
        plt.text(0.35, 0.7, 'Host : ')
        plt.text(0.5, 0.6, '+ Samsung  S7')
        root.update_idletasks()
        root.update()
        time.sleep(1)
        print(1)

ax2.cla()
ax2.set_yticks(pos)
ax2.set_yticklabels(label)
while not os.path.exists('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt'):
    pass
if os.path.isfile('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt'):

    #pass
    #file2 = open('C:/Users/venka_pwbgtmt/Desktop/palace_S7/peer/peer_extragui_Data/output_log.txt', 'r')
    #for j in file2:
        #if 'PRS2: Number of active clients changed to:2' in j:
    #pos = np.arange(len(label)) + 0.5

    ax1.barh(pos, val, align='center', height=0.1, color='b')
    ax2.barh(pos, val2, align='center', height=0.1, color='g', label='Host')
    ax2.barh(pos, val3, align='center', height=0.1, color='b', left=val2, label='Peer1')
    print(pos)
    ax1.set_title('Peer 1 : MSI Laptop')
    ax2.set_title('Collaborative Computing')
    #ax1.set_yticks(pos)
    #ax1.set_yticklabels(['DISK', 'MEMORY', 'CPU', 'GPU'])
    ax1.text(85, 0.1, '1171 GB')
    ax1.text(89, 1.1, '16 GB')
    ax1.text(86, 2.1, '2.6 GHz')
    ax1.text(76, 2.8, '2365 GFLOPS')
    ax2.text(85, 0.1, '32 GB + 1171 GB')
    ax2.text(88, 1.1, '4 GB + 16 GB')
    ax2.text(74, 2.1, '2.15 GHz + 1.6 GHz + 2.6 GHz')
    ax2.text(74, 2.8, '407.4 GFLOPS + 2365 GFLOPS')
        # fig2.patch.set_facecolor('white')
    plt.text(0.5, 0.2, '+ MSI Laptop')
    ax5.text(0.55, 0.5, '+ WiFi ', fontsize=13)
    plt.subplot(212)
    plt.cla()
    plt.title('VR Parameters')
    plt.text(35, 0.7, 'FPS : 60')
    plt.text(35, 0.3, 'Battery : 325 minutes left')

    root.update_idletasks()
    root.update()
    time.sleep(1)
##print(10)
#out = GUI(root)
root.mainloop()
