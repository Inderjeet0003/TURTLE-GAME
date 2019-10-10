# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:14:31 2019

@author: inder
"""

from turtle import*
from random import randint
for i in range(10):
  write(i,align='center')
  right(90)
  forward(10)
  pendown()
  forward(180)
  penup()
  backward(190)
  left(90)
  forward(20)


ada=Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-25,-25)
ada.pendown()

  
bob=Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-25,-40)
bob.pendown()

 
tom=Turtle()
tom.color('black')
tom.shape('turtle')
tom.penup()
tom.goto(-25,-55)
tom.pendown()

sam=Turtle()
sam.color('pink')
sam.shape('turtle')
sam.penup()
sam.goto(-25,-70)
sam.pendown()

lily=Turtle()
lily.color('yellow')
lily.shape('turtle')
lily.penup()
lily.goto(-25,-85)
lily.pendown()

for turn in range(80):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  tom.forward(randint(1,5))
  sam.forward(randint(1,5))
  lily.forward(randint(1,5))