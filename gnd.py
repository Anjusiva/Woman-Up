from turtle import *

def ground():
    pu()
    setposition(-680,0)
    color("#e2c7b7")
    pd()
    begin_fill()
    seth(0)
    fd(1360)
    seth(90)
    right(180)
    fd(345)
    seth(90)
    left(90)
    fd(1360)
    setposition(-680,0)
    end_fill()
