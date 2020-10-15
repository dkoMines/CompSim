import math
import matplotlib.pyplot as plt

def getAvSd(fileName, index):
    # 1 pass
    sum1 = 0
    sum2 = 0
    count = 0
    data = open(fileName)
    for line in data:
        line = line.split()[index]
        count += 1
        sum2 += float(line)**2
        sum1 += float(line)
    data.close()

    opAverage = sum1 / count
    opSd = math.sqrt(sum2 / count - opAverage**2)

    # print("one-pass  ",opAverage,"    ",opSd)
    return opAverage, opSd

def getC(file,x_u,x_v):
    data = open(file)
    u = []
    v = []
    t = 0
    i = 0
    for line in data:
        u.append(float(line.split()[0]))
        v.append(float(line.split()[1]))
        #plt.plot(line.split()[0],line.split()[1],'ro')
    for i in range(len(u)):
        t += u[i]*v[i]
    t = t/(i+1) - x_u*x_v
    return t


file = "msod-vs-lr.dat"
file = "lr-vs-msod.dat"
x_u, s_u = getAvSd(file,0)
x_v, s_v = getAvSd(file,1)
c_uv = getC(file,x_u,x_v)

#mean square othagonal distance line of best fit angle
# u axis ~ x axis
theta = .5*math.atan2( s_u**2 - s_v**2, 2*c_uv)
print(theta)

m = 1*s_v/s_u
b=x_v - m*x_u

data = open(file)
for line in data:
    plt.plot(line.split()[0],line.split()[1],'ro')
for i in range(20):
    plt.plot(i,m*i+b,'r--')
    print("U = ",i," V = ",m*i+b)
plt.show()
