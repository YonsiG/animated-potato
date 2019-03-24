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

def findf(x):
    return -np.log(1-x)
    
trueran=[]
ran1 = [random.random() for _ in range(1000)]
for iran in range(1000):
    trueran.append(findf(ran1[iran]))
drawplot(trueran, 50, "Number", "Number of events", "Exponent distribution(transformation)", 0,5,0,160)

trueran2=[]
ran2 = [random.random() for _ in range(1000)]
ran3 = [random.random()*5 for _ in range(1000)]
for i in range(1000):
    judge = np.exp(-ran3[i])
    if ran2[i]<judge:
        trueran2.append(ran3[i])
drawplot(trueran2,50,"Number","Number of events", "Exponent distribution(Accept-Reject)", 0, 5, 0, 30)

