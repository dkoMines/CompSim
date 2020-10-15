import math

file_name = "datafile.dat.mid"
f = open(file_name)
mj = []
f_mj = []
mult_mj_f = 0
for num in [line.split() for line in f]:
    mj.append(float(num[0]))
    f_mj.append(float(num[1]))
    mult_mj_f += float(num[0])*float(num[1])

mult_mj_f = mult_mj_f

print("x_bar = ", mult_mj_f)
t = 0
for i in range(len(mj)):
    t += ((mj[i] - mult_mj_f)**2)*f_mj[i]
print("s = ", math.sqrt(t))
