import random
from math import cos
from math import sin
import math
from matplotlib import pyplot as plt
import numpy as np  
import imageio

# Place Class
class Place:
    def __init__(self, name,latitude,longitude):
        self.Name = name
        self.Latitude = latitude
        self.Longitude = longitude

# Points Class
class Person:
    # 建構式
    def __init__(self): 
        self.Latitude = -1
        self.Longitude = -1
        self.Distance = -1
        self.ThetaP = -1
        self.StepLen = -1 
        self.Theta = random.uniform(0,math.pi*2) 
        self.Probability = -1
        self.StayTime = random.randint(0,30)
    
    def SetPoint(self, latitude, longitude , R) :
        self.Distance = random.uniform(0,R) 
        self.ThetaP = random.uniform(0,math.pi*2) 
        self.Latitude = latitude + self.Distance*sin(self.ThetaP)
        self.Longitude = longitude + self.Distance*cos(self.ThetaP)
        
    def ReNewPoint(self, latitude, longitude , steplen) :
        self.Latitude = latitude + steplen*sin(self.Theta)
        self.Longitude = longitude + steplen*cos(self.Theta)
        
    def NormalDistribation(self,lenn,index) :
        if index < lenn*0.004 :
           self.Theta = self.Theta + math.pi
           return 0
        elif index < lenn*0.042 :
           self.Theta = self.Theta + (-1)**random.randint(1,2)*random.uniform(0.5237,1.57)
           return 1
        elif index < lenn*0.272 :
           self.Theta = self.Theta + (-1)**random.randint(1,2)*random.uniform(0,0.5236) 
           return 2  
        else:
           return 3

    def NextStep(self,lenn,index) :
        self.StepLen = random.uniform(0,0.01)
        self.NormalDistribation(lenn,index)
        self.ReNewPoint(self.Latitude,self.Longitude,self.StepLen)

def Rad(d):
    return d * math.pi / 180.0
    
def GetDistance(lat1_txt, lng1_txt, lat2_txt, lng2_txt):
    lat1 = float(lat1_txt)
    lng1 = float(lng1_txt)
    lat2 = float(lat2_txt)
    lng2 = float(lng2_txt)
    EARTH_REDIUS = 6378.137
    radLat1 = Rad(lat1)
    radLat2 = Rad(lat2)
    a = radLat1 - radLat2
    b = Rad(lng1) - Rad(lng2)
    s = 2 * math.asin(math.sqrt(math.pow(sin(a/2), 2) + cos(radLat1) * cos(radLat2) * math.pow(sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

def SetAllPoints(lenn) :
    for i in range(lenn) :
        p1 = Person()
        p1.SetPoint(place.Latitude,place.Longitude,R1)
        people.append(p1)
        x.append(p1.Longitude)
        y.append(p1.Latitude)

def ShowPic(num,r1,r2) :
    # plot
    fig1,ax1 = plt.subplots()

    # Place
    ax1.plot(place.Longitude,place.Latitude,'ko',color='red',alpha=1)
    ax1.plot(x[0],y[0],'ko',color='green',alpha=1)
    ax1.plot(x[27],y[27],'ko',color='green',alpha=1)
    ax1.plot(x[99],y[99],'ko',color='green',alpha=1)
    # People
    ax1.scatter(x,y,color='black',marker='x')

    DrawCircle(ax1,r1)
    DrawCircle(ax1,r2)
    ax1.set_ylabel('Latitude', color='tab:green')
    ax1.set_xlabel('Lontitude', color='tab:pink')  
    plt.xlim(place.Longitude-R2-0.05,place.Longitude+R2+0.05)
    plt.ylim(place.Latitude-R2-0.05,place.Latitude+R2+0.05)
    plt.title("Taipei 101 People Flow") 
    plt.savefig(str(num)+'.png')
    #plt.show()
    ax1.clear()

def DrawCircle(ax,R) :
    # Circle
    theta_circle = np.arange(0,2*np.pi,0.01)
    x_circle = place.Longitude + R*np.cos(theta_circle)
    y_circle = place.Latitude + R*np.sin(theta_circle)
    ax.plot(x_circle,y_circle,color='purple')

def GetAllPoints() :
    x.clear()
    y.clear()
    for p in people :
        x.append(p.Longitude)
        y.append(p.Latitude)
        #print(p.Longitude,p.Latitude)

# main program
place = Place("Taipei 101",25.033841970321756,121.56455420754622)
people = []
x = []
y = []

lenn = 100
R1 = 0.1
R2 = 0.12

SetAllPoints(lenn)
ShowPic(0,R1,R2)

times = 1
frame_len = 30

while times < (frame_len+1) :
    index = 0
    for p in people :
        p.NextStep(lenn,index)
        index = index + 1
    GetAllPoints()
    ShowPic(times,R1,R2)
    times = times + 1

gif_images = []
for i in range(0, (frame_len+1)):
    gif_images.append(imageio.imread(str(i)+".png"))   
imageio.mimsave("hello.gif", gif_images, fps=2)   

print("finish")
    
