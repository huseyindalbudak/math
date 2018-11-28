# dynamic line graph
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

import time

fig = plt.figure()
ax1 = p3.Axes3D(fig)
#fig2 = plt.figure()
#ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open("av_Data.txt","r").read()
    dataArray = pullData.split('\n')  #each line has 3 integer numbers
    xar = []
    yar = []
    zar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y,z = eachLine.split(',')
            xar.append(float(x))
            yar.append(float(y))
            zar.append(float(z))
    ax1.clear()
    ax1.plot(xar,yar,zar)
ani = animation.FuncAnimation(fig, animate, interval=10)
#ani = animation.FuncAnimation(fig2, animate, interval=100)


plt.show()
