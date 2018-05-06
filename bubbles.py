'''
Jonathan Branson - bubbles.py

Adapted from programs written by Dr. Melissa Stange - 01-01-2017

This program creates and should move the bubbles up the screen and make them
disappear when they reach top of the screen. Currently not working. 

'''

from graphics import *
import time
from random import randint

##Not working got bubbles to show up but couldnt get them to move
class Bubbles:

     def __init__(self, x_1, y_1, radius_1, velocity_1):

         #Store varibales form main program
         self.x = x_1
         self.y = y_1
         self.radius = radius_1
         self.velocity = velocity_1

         #Create bubble
         self.bubble= Circle(Point(self.x, self.y), self.radius/ 1.12)
         self.bubble.setFill('blue')

     #Draws bubble
     def draw(self,window):
         self.win = window 
         self.bubble.draw(window)

     #Removes bubble
     def undraw(self):
         self.bubble.undraw()

     #Moves bubbles(Not working)
     def move(self, dx, dy):
         self.x = self.x + 0
         self.y = self.y + dy
         self.bubble.move(dx, dy)

    #Moves bubble on velocity, and runs undraw() method when y is equal to 0
     def step(self):

         if self.y < 0:
             self.undraw()
             
         self.move(0, self.velocity)
         

    
      
      
       
    
