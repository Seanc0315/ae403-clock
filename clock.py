# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:03:28 2020

@author: admin
"""


import turtle
import time
import datetime

tur = turtle.Turtle()

tur.speed(100)

def writenumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
    tur.pendown()

tur.seth(90)

for i in range(12):
    tur.right(30)
    writenumber(i + 1)
    
update = True
updateSecond = True

while True:
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    if updateSecond:
        second = turtle.Turtle()
        second.fillcolor(1, 0, 0)
        second.seth(90)
        second.right(s * 6)
        second.forward(200)
        updateSecond = False
        
    if update:
        minute = turtle.Turtle()
        minute.fillcolor(1, 0, 1)
        minute.seth(90)
        minute.right(m * 6)
        minute.forward(150)
        hour = turtle.Turtle()
        hour.fillcolor(0, 0, 1)
        hour.seth(90)
        hour.right(h * 30 + m / 60 * 30)
        hour.forward(100)
        update = False
        
    time.sleep(1)
    now = datetime.datetime.now()
    mNew = now.minute
    sNew = now.second
    
    if mNew != m:
        update = True
        hour.clear()
        hour.reset()
        
        minute.clear()
        minute.reset()
    
    if sNew != s:
        updateSecond = True
        second.clear()
        second.reset()
        
turtle.done()
turtle.exitonclick()