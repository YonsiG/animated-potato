import random
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

def drawhist(ran, nbins, Xlabel, Ylabel, Title):
    plot.hist(ran, nbins, facecolor="g", alpha=0.75)
    plot.xlabel(Xlabel)
    plot.ylabel(Ylabel)
    plot.title(Title)
#    plot.axis([xmin,xmax,ymin,ymax])
    plot.grid(True)
    plot.show()
    
def connection(par,ax1):
    ax1.plot3D([par.initX, par.finalX],[par.initY, par.finalY],[par.initZ, par.finalZ])
    ax1.scatter3D([par.initX],[par.initY],[par.initZ])
    
class particle(object):
    def _init_(self,x0,y0,z0):
        self.initX = x0
        self.initY = y0
        self.initZ = z0
        
    def state(self,px,py,pz,e,theta,phi,s):
        self.Px = px
        self.Py = py
        self.Pz = pz
        self.E = e
        self.Theta = theta
        self.Phi = phi
        self.splitable = s
    
    def final(self,xt,yt,zt):
        self.finalX = xt
        self.finalY = yt
        self.finalZ = zt

    def setzero(self):
        self.initX = 0
        self.initY = 0
        self.initZ = 0
        self.finalX = 0
        self.finalY = 0
        self.finalZ = 0
        self.Px = 0
        self.Py = 0
        self.Pz = 0
        self.E = 0
        self.Theta = 0
        self.Phi = 0
        self.splitable = 0
        
    def set_init(self,InE):
        self.initX = 0
        self.initY = 0
        self.initZ = 0
        self.Px = 0
        self.Py = 0
        self.Pz = 0
        self.E = InE
        self.Theta = 0
        self.Phi = 0
        self.splitable = 1

def GetZ():
    ran = random.random()*np.log(2)
    Z = np.exp(ran)-1
    return Z

def GetTheta():
    ran = random.random()*np.log(1+np.pi/2)
    theta = np.exp(ran)-1
    return theta

def GetPhi():
    ran = random.random()*2*np.pi
    return ran
    
def GetTime():
    ran = 3*random.random()
    return ran

def Init_Energy():
    ran = random.random()
    return -20*np.log(1-ran)
    
    
E0 = 3
null = particle()
null.setzero()
p0 = particle()
p0.final(0,0,0)
parts=[]
finalNum=[]
count=[]

for irunning in range(1000):
    parts.clear()
    p0.set_init(Init_Energy())
    parts.append(p0)
    finalNum.append(0)

    iseq = 0
    icount = 1
    while(icount != 0):
        icount = 0 
        for inum in range(2**iseq):
            if parts[inum+2**iseq-1].E>E0:
                E_r = parts[inum+2**iseq-1].E
                Px_r = parts[inum+2**iseq-1].Px
                Py_r = parts[inum+2**iseq-1].Py
                Pz_r = parts[inum+2**iseq-1].Pz
                X_r = parts[inum+2**iseq-1].finalX
                Y_r = parts[inum+2**iseq-1].finalY
                Z_r = parts[inum+2**iseq-1].finalZ
            
                theta = GetTheta()+parts[inum+2**iseq-1].Theta
                phi = GetPhi()+parts[inum+2**iseq-1].Phi
                theta2 = 2*parts[inum+2**iseq-1].Theta-theta
                phi2 = 2*parts[inum+2**iseq-1].Phi-phi
                z = GetZ()
                t = GetTime()
                       
                p1 = particle()
                p2 = particle()
             
                E1 = z*E_r
                E2 = E_r - E1
                Px1 = E1*np.cos(theta)*np.cos(phi)
                Py1 = E1*np.sin(theta)*np.cos(phi)
                Pz1 = E1*np.sin(phi)
                Px2 = Px_r - Px1
                Py2 = Py_r - Py1
                Pz2 = Pz_r - Pz1
                x1f = X_r + t*Px1
                x2f = X_r + t*Px2
                y1f = Y_r + t*Py1
                y2f = Y_r + t*Py2
                z1f = Z_r + t*Pz1
                z2f = Z_r + t*Pz2

                if E1>E0:
                    s1=1
                else:
                    s1=0
                    finalNum[irunning]=finalNum[irunning]+1
                if E2>E0:
                    s2=1
                else:
                    s2=0
                    finalNum[irunning]=finalNum[irunning]+1
            
                p1._init_(X_r,Y_r,Z_r)
                p2._init_(X_r,Y_r,Z_r)
                p1.state(Px1,Py1,Pz1,E1,theta,phi,s1)
                p2.state(Px2,Py2,Pz2,E2,theta2,phi2,s2)
                p1.final(x1f,y1f,z1f)
                p2.final(x2f,y2f,z2f)
            
                icount = icount+1
              
            else:
                p1 = null
                p2 = null
            
            parts.append(p1)
            parts.append(p2)
        iseq = iseq+1
    
#fig = plot.figure(）
#ax1 = plot.axes(projection='3d')
#for ipart in range(len(parts)):
#    connection(parts[ipart],ax1) 

#plot.show()
    n = -1
    R = 0.5
    p_raw = particle()
    count.append(0)
    for ipart1 in range(len(parts)):
        if parts[ipart1]==null:
            continue
        if parts[ipart1].splitable==1:
            continue
        
        #calculate dij
        dij = 10000
        for ipart2 in range(len(parts)):
            if ipart2<=ipart1:
                continue
            if parts[ipart2]==null:
                continue
            if parts[ipart2].splitable==1:
                continue
            theta1 = parts[ipart1].Theta
            theta2 = parts[ipart2].Theta
            phi1 = parts[ipart1].Phi
            phi2 = parts[ipart2].Phi
            delta = np.sqrt(np.square(theta1-theta2) + np.square(phi1-phi2))
            Pt12 = np.square(parts[ipart1].Py) + np.square(parts[ipart1].Pz)
            Pt22 = np.square(parts[ipart2].Py) + np.square(parts[ipart2].Pz)
            dij_temp = min([pow(Pt12,n),pow(Pt22,n)])*delta/R
            if dij_temp<dij:
                dij = dij_temp
                Pnum1 = ipart1
                Pnum2 = ipart2

        #calculate diB
        Pt2 = np.square(parts[ipart1].Py) + np.square(parts[ipart1].Pz)
        diB = pow(Pt2,n)
        
        if dij<diB:
            p_raw.Px = parts[Pnum1].Px+parts[Pnum2].Px
            p_raw.Py = parts[Pnum1].Py+parts[Pnum2].Py
            p_raw.Pz = parts[Pnum1].Pz+parts[Pnum2].Pz
            p_raw.E = parts[Pnum1].E+parts[Pnum2].E
            p_raw.Theta = parts[Pnum1].Theta+parts[Pnum2].Theta
            p_raw.Phi = parts[Pnum1].Phi+parts[Pnum2].Phi
            p_raw.splitable = 0
            parts.append(p_raw)
            parts[Pnum2]=null
    
        else:
            count[irunning]=count[irunning]+1

drawhist(count, 20, "Number of reco_jets", "Number of shower", "jet reconstruction")
drawhist(finalNum, 30, "Number of all_jets", "Number of shower", "jet production")
