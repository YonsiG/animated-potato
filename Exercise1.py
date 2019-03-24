import random
ran = [random.random() for _ in range(1000)]

import numpy as np
import math
import matplotlib.pyplot as plot
plot.hist(ran,50,facecolor="g",alpha=0.75)
plot.xlabel("Num")
plot.ylabel("Number of events")
plot.title("uniform distribution")
plot.axis([0,1,0,35])
plot.grid(True)
plot.show()

ran2 = [random.random()*10+5 for _ in range(1000)]
plot.hist(ran2,50,facecolor="g",alpha=0.75)
plot.xlabel("Num")
plot.ylabel("Number of events")
plot.title("uniform distribution")
plot.axis([5,15,0,35])
plot.grid(True)
plot.show()
