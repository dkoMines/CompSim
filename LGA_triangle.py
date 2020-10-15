import random
import matplotlib.pyplot as plt
import math

def area(x1, y1, x2, y2, x3, y3): 
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0)

def checkInside(x1,x2,x3,y1,y2,y3,x,y):
    A = area (x1, y1, x2, y2, x3, y3) 
    A1 = area (x, y, x2, y2, x3, y3) 
    A2 = area (x1, y1, x, y, x3, y3) 
    A3 = area (x1, y1, x2, y2, x, y) 
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False

def doAll(x1,y1,x2,y2,x3,y3):
    width = max(x1,x2,x3) - min(x1,x2,x3)
    height = max(y1,y2,y3)-min(y1,y2,y3)
    x_l = []
    y_l = []
    for i in range(5000):
        while True:
            x = random.random()*width+min(x1,x2,x3)
            y = random.random()*height+min(y1,y2,y3)
            if (checkInside(x1,x2,x3,y1,y2,y3,x,y)):
                x_l.append(x)
                y_l.append(y)
                break
    plt.plot(x_l, y_l,'ro')
    plt.show()

# doAll(random.random()*10,random.random()*10,random.random()*10,random.random()*10,random.random()*10,random.random()*10)
doAll(1,1,11,1,6,10)

