import random
import numpy as np
import matplotlib.pyplot as plot
def drawplot(ran, nbins, Xlabel, Ylabel, Title, xmin, xmax, ymin, ymax):
    plot.hist(ran, nbins, facecolor="g", alpha=0.75)
    plot.xlabel(Xlabel)
    plot.ylabel(Ylabel)
    plot.title(Title)
    plot.axis([xmin,xmax,ymin,ymax])
    plot.grid(True)
    plot.show()
    
Pi=[]
for ipis in range(100):
    Pi.append(0)
    accept=0
    ran1 = [random.random() for _ in range(10000)]
    ran2 = [random.random() for _ in range(10000)]
    for irun in range(10000):
        judge = ran1[irun]*ran1[irun]+ran2[irun]*ran2[irun]
        if judge<1:
            accept=accept+1
    Pi[ipis]=4*accept/10000
    
drawplot(Pi,20,"Pi value","Number of events","calculating each Pi 10000 points",3.08,3.2,0,17)

Pi.clear()
for ipis in range(1000):
    Pi.append(0)
    accept=0
    ran1 = [random.random() for _ in range(1000)]
    ran2 = [random.random() for _ in range(1000)]
    for irun in range(1000):
        judge = ran1[irun]*ran1[irun]+ran2[irun]*ran2[irun]
        if judge<1:
            accept=accept+1
    Pi[ipis]=4*accept/1000
    
drawplot(Pi,20,"Pi value","Number of events","calculating Pi 1000 times",3.0,3.3,0,160)

Pi.clear()
for ipis in range(100):
    Pi.append(0)
    accept=0
    ran1 = [random.random() for _ in range(1000)]
    ran2 = [random.random() for _ in range(1000)]
    for irun in range(1000):
        judge = ran1[irun]*ran1[irun]+ran2[irun]*ran2[irun]
        if judge<1:
            accept=accept+1
    Pi[ipis]=4*accept/1000
    
drawplot(Pi,20,"Pi value","Number of events","calculating Pi",3.0,3.3,0,15)

