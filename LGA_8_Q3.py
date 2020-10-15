import random
import matplotlib.pyplot as plt

def calcMean(l):
    return sum(l)/len(l)
def calcSD(l):
    total = 0
    u = calcMean(l)
    for num in l:
        total += (num-u)**2
    return (total/len(r))**.5
        
def generateOneDataSet():
    r = [random.random()*2]
    a = [r[0]]
    for j in range(10):
        for i in range(1,1000):
            r.append(random.random()*2)
            a.append(a[i-1]+r[i])
    return [r,a]

def generateCDF(r,a):
    k = []
    r.sort()
    a.sort()
    for i in range(len(r)):
        k.append(i/len(r))
    plt.plot(r,k,'ro')
    plt.title("CDF of r")
    plt.show()

    plt.title("CDF of a")
    plt.plot(a,k,'bo')
    plt.show()
        
x = generateOneDataSet()
r = x[0]
a = x[1]

print("Mean: ",calcMean(r)," Standard Deviation: ",calcSD(r))
generateCDF(r,a)

