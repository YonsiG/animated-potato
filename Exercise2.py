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
    
trueran=[]
ran1 = [random.random() for _ in range(6000)]
ran2 = [random.random()*10 for _ in range(6000)]
for i in range(6000):
    judge = 1/(2*np.sqrt(2*np.pi))*np.exp(-(ran2[i]-5)*(ran2[i]-5)/8)
    if ran1[i]<judge:
        trueran.append(ran2[i])
drawplot(trueran,50,"Number","Number of events", "Gaussian distribution", 0, 10, 0, 35)
