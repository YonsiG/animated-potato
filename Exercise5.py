import random
import numpy as np
import matplotlib.pyplot as plot
def drawhist(ran, nbins, Xlabel, Ylabel, Title, xmin, xmax, ymin, ymax):
    plot.hist(ran, nbins, facecolor="g", alpha=0.75)
    plot.xlabel(Xlabel)
    plot.ylabel(Ylabel)
    plot.title(Title)
    plot.axis([xmin,xmax,ymin,ymax])
    plot.grid(True)
    plot.show()
    
def connection(par):
    plot.plot([par.initX, par.finalX],[par.initY, par.finalY])
    plot.scatter([par.initX],[par.initY])
    
class particle(object):
    def _init_(self,x0,y0):
        self.initX = x0
        self.initY = y0
#        self.initZ = z0
        
    def state(self,px,py,e):
        self.Px = px
        self.Py = py
#        self.Pz = pz
        self.E = e
    
    def final(self,xt,yt):
        self.finalX = xt
        self.finalY = yt
#        self.finalZ = zt

    def setzero(self):
        self.initX = 0
        self.initY = 0
        self.finalX = 0
        self.finalY = 0
        self.Px = 0
        self.Py = 0
        self.E = 0
        
    def set_init(self,InE):
        self.initX = 0
        self.initY = 0
        self.Px = InE
        self.Py = 0
        self.E = InE

def GetZ():
    ran = random.random()*np.log(2)
    Z = np.exp(ran)-1
    return Z

def GetTheta():
    ran = random.random()*np.log(1+np.pi/2)
    theta = np.exp(ran)-1
    return theta

def GetTime():
    ran = 3*random.random()
    return ran
    
    
InE = 10
E0 = 2
null = particle()
null.setzero()
p0 = particle()
t = GetTime()
p0.final(t*InE,0)
p0.set_init(InE)
parts=[]
parts.append(p0)

iseq = 0
icount = 1
while(icount != 0):
    icount = 0 
    for inum in range(2**iseq):
        if parts[inum+2**iseq-1].E>E0:
            E_r = parts[inum+2**iseq-1].E
            Px_r = parts[inum+2**iseq-1].Px
            Py_r = parts[inum+2**iseq-1].Py
            X_r = parts[inum+2**iseq-1].finalX
            Y_r = parts[inum+2**iseq-1].finalY
            
            theta = GetTheta()+np.arctan(Py_r/Px_r)
            z = GetZ()
            t = GetTime()
                       
            p1 = particle()
            p2 = particle()
             
            E1 = z*E_r
            E2 = E_r - E1
            Px1 = E1*np.cos(theta)
            Py1 = E1*np.sin(theta)
            Px2 = Px_r - E1*np.cos(theta)
            Py2 = Py_r - E1*np.sin(theta)
            x1f = X_r + t*Px1
            x2f = X_r + t*Px2
            y1f = Y_r + t*Py1
            y2f = Y_r + t*Py2
            p1._init_(X_r,Y_r)
            p2._init_(X_r,Y_r)
            p1.state(Px1,Py1,E1)
            p2.state(Px2,Py2,E2)
            p1.final(x1f,y1f)
            p2.final(x2f,y2f)
            
            icount = icount+1
            
        else:
            p1 = null
            p2 = null
            
        parts.append(p1)
        parts.append(p2)
    iseq = iseq+1

for ipart in range(len(parts)):
    connection(parts[ipart])
plot.show()
    
