import random

def largestDie():
    c_1 = [0,0,0,0,0,0]
    total = 0
    for j in range(6):
        seed = int (random.random()*10000+1)
        random.seed(seed)
        print("Using seed: ", seed)
        for i in range(1000000):
            die_1 = int ((random.random()*6+1) // 1)
            die_2 = int ((random.random()*6+1) // 1)
            die_3 = int ((random.random()*6+1) // 1)
            largest = max(die_1,die_2,die_3)
            c_1[largest-1] += 1
            total += 1
    for x in range(6):
        print(x+1," Count: ", c_1[x], " Prob: ",float(c_1[x])/total*100,"%")

largestDie()
