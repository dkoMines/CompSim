import random
import matplotlib.pyplot as plt
import math

def doAll():
    x_l = []
    y_l = []
    for i in range(5000):
        x = random.random()*2*math.pi
        y = random.random()*math.sin(x)
        x_l.append(x)
        y_l.append(y)
    plt.plot(x_l, y_l,'ro')
    plt.show()

doAll()

