import math

data = open("dataset1.dat")
# pretending this is sys.argv[1] ;)
sumVar = 0
count = 0
for line in data:
    count += 1
    sumVar += float(line)
data.close()

tpAverage = sumVar/count

data = open("dataset1.dat")
sumSD = 0
for line in data:
    sumSD += (tpAverage - float(line))**2
data.close()

tpSd = math.sqrt(sumSD / count)

print("two-pass  ",tpAverage,"    ",tpSd)

# 1 pass
sum1 = 0
sum2 = 0
count = 0
data = open("dataset1.dat")
for line in data:
    count += 1
    sum2 += float(line)**2
    sum1 += float(line)
data.close()

opAverage = sum1 / count
opSd = math.sqrt(sum2 / count - opAverage**2)

print("one-pass  ",opAverage,"    ",opSd)
