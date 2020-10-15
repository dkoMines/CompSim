import random
import turtle
import math

def drawPoint(scale, t):
    # pick r and theta
    r = random.random()*scale*100
    theta = random.random()*math.pi*2-math.pi
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    # print("R=",r," Theta=",theta," Coords: (",x,",",y,")")
    t.penup()
    t.goto(x,y)
    t.pendown()
    for x in range(1):
        t.forward(0.1)
        t.left(60)
        


def circleGuesser():
    # Set up circle
    scale = 3
    t = turtle.Turtle()
    t.speed(10)
    t.color("white","black")
    t.goto(0,-100*scale)
    t.color("black","black")
    for x in range(100):
        t.forward(628.318531*scale/100)
        t.left(3.6)
    t.goto(0,100*scale)
    t.color("white","black")
    t.goto(-99*scale,0)
    t.color("black","black")
    t.goto(101*scale,0)
    for x in range(20000):
        t.pensize(3)
        t.color("red","black")
        drawPoint(scale,t)

    




    

circleGuesser()
