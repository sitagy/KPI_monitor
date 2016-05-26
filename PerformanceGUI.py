import matplotlib
import psutil
import matplotlib.pyplot as plt
from drawnow import *
import numpy
from tkinter import *
from matplotlib.figure import Figure
import os.path
import time

n=0
p=0
o=0
q=0
x = []
y = []
z = []

fps = []
host_mem = []
count = 0
host_disk = []
host_cpu = []
count1 = 0
count2 = 0
count3 = 0
count4 = 0

plt.ion()

def fig():
    #time.sleep(30)
    fig1 = plt.figure(1)
    fig1.patch.set_facecolor('white')
    plt.subplot(221)

    plt.plot(x,'b-', label = 'peer 1')
    plt.plot(host_cpu,'g-', label = 'Host')
    plt.tick_params(axis='y', which='both', labelleft='off', labelright='on')
    plt.ylim(0,100)
    plt.xlim(60,0)
    plt.ylabel('CPU %ge usage')
    plt.xlabel('Number of Samples')
    plt.grid(True)
    plt.legend()
    plt.title('CPU')
    plt.legend()
    plt.subplot(222)

    plt.plot(y,'b-',label = 'peer 1')
    plt.plot(host_mem, 'g-', label = 'host')
    plt.tick_params(axis='y', which='both', labelleft='off', labelright='on')
    plt.ylim(0, 100)
    plt.xlim(60, 0)
    plt.ylabel('Memory %ge usage')
    #plt.xlabel('Time')
    plt.grid(True)
    plt.xlabel('Number of Samples')
    plt.title('Memory')
    plt.legend()
    plt.subplot(223)

    plt.plot(z, 'b-',label = 'peer 1')
    plt.tick_params(axis='y', which='both', labelleft='off', labelright='on')
    plt.plot(host_disk, 'g-',label = 'host')
    plt.ylim(0, 100)
    plt.xlim(60, 0)
    plt.xlabel('Number of Samples')
    plt.ylabel('Disk %ge usage')
    plt.grid(True)
    plt.title('Disk')
    plt.legend()
    plt.subplot(224)
    plt.tick_params(axis='y', which='both', labelleft='off', labelright='on')
    plt.plot(fps, 'g-', label = 'fps')
    plt.ylim(0,60)
    plt.xlim(60,0)
    plt.ylabel('FPS')
    plt.xlabel('Time')
    plt.grid(True)
    plt.title('FPS')
    plt.legend()


while not os.path.exists('C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/Logs/mem.txt'):
    pass

f3 = open("C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/Logs/disk.txt", "r")

f8 = open("C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/Logs/fps.txt", "r", encoding="utf8", errors='ignore')
f2 = open("C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/Logs/mem.txt", "r")
f5 = open('C:/Users/venka_pwbgtmt/AppData/Local/Android/sdk/platform-tools/Logs/top.txt', 'r')


while True:


    cpu = psutil.cpu_percent(interval=2)
    cpu = float(cpu)

    x.append(cpu)
    x.insert(0, x.pop())
    for i in f5:
        if 'System' in i:
            # print(i)
            j = i.split(',')
            m = j[1].split(' ')
            k = m[2]
            a1 = k[:-1]
            a1 = float(a1)
            n = j[0].split(' ')
            l = n[1]
            b1 = l[:-1]
            b1 = float(b1)
            sum = a1 + b1
            if not os.path.exists('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt'):

                #print(sum)
                # print(1)
                host_cpu.append(sum)
                host_cpu.insert(0, host_cpu.pop())

            if os.path.isfile('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt'):

                f6 = open('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt', 'r')

                # print(2)

                for j in f6:
                    if 'PRS: Launched OBS' in j:
                        count1 += 1
                        #print('count1:', count1)

                    if 'onDestroy called. Killing OBS appplication' in j:
                        count2 += 1
                        #print('count2:', count2)

                sum1 = sum - (count1 * 30) + (count2 * 30)
                #print('sum:', sum)
                #print('sum1:', sum1)
                host_cpu.insert(0, host_cpu.pop())
                host_cpu.append(sum1)












                # print(sum)
            #host_cpu.append(sum)
            #host_cpu.insert(0, host_cpu.pop())
    #print('cpu', x)

            #print('android:',m)

    mem = psutil.virtual_memory()
    out = mem.percent
    #time.sleep(2.5)
    y.append(out)
    y.insert(0, y.pop())
    a = (psutil.disk_usage('C:/'))
    b = (psutil.disk_usage('D:/'))
    c = (psutil.disk_usage('E:/'))
    a1 = (a.percent * 239) / 100
    b1 = (b.percent * 834) / 100
    c1 = (c.percent * 98) / 100
    s = ((a1 + b1 + c1) * 100) / 1171
    z.append(s)
    z.insert(0, z.pop())
    for i in f2:
        if "MemTotal" in i:
            n = re.findall(r'\d{1,10}', i)
            p = n[0]
            p = int(p)
            #print(p)
        if "MemFree" in i:
            o = re.findall(r'\d{1,10}', i)
            # o = int(o)
            q = o[0]
            q = int(q)
            #print(q)
    diff = ((p - q) * 100) / p
    if not os.path.exists('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt'):


        host_mem.append(diff)
        host_mem.insert(0, host_mem.pop())

    if os.path.isfile('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt'):
        f7 = open('C:/Users/venka_pwbgtmt/Desktop/palace_s7_latest/peer/palace_reconnect_package_noGUI/peer_nogui_Data/output_log.txt', 'r')
        for j in f7:
            if 'PRS: Launched OBS' in j:
                count3 += 1
                print('count1:', count1)

            if 'onDestroy called. Killing OBS appplication' in j:
                count4 += 1
                print('count2:', count2)

        diff1 = diff - (count1 * 30) + (count2 * 30)
        host_mem.append(diff1)
        host_mem.insert(0, host_mem.pop())




    for i in f3:
        if "Data-Free" in i:
            j = i.split(' ')
            k = j[6]
            e = k[0:2]
            e = float(e)
            # print(e)
            disk_used = 100 - e
            host_disk.append(disk_used)
            host_disk.insert(0, host_disk.pop())


    for i in f8:
        if "[GR] FPS" in i:
            print(1)
            j = i.split(':')
            s = j[4]
            print(s)
            fps.append(s)
            fps.insert(0, fps.pop())

    drawnow(fig)


    plt.pause(.000001)

    if (count > 60):
        x.pop(0),host_cpu.pop(0), y.pop(0), host_mem.pop(0), z.pop(0), host_disk.pop(0), fps.pop(0)


    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0






