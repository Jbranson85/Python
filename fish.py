'''

Jonathan Branson - fish.py

Adapted from programs written by Dr. Melissa Stange - 01-01-2017 

This program creates the fish, and gives them their animation.
'''

from graphics import *
from random import randint


class Fish_2:

   def __init__(self, x, y, radius, color, velocity):
      
      #Stores the varibles received from the main program
      self.x = x
      self.y = y
      self.radius = radius
      self.color = color
      self.velocity = velocity

      self.head = None
      self.tail= None

      #Moves to the building of the fish function
      self.build_fish()

   #Create the fish function
   def build_fish(self):
      

      ##Tail if moving right
      if self.velocity < 0: 
         self.tail= Polygon(
            Point(self.x, self.y),
            Point(self.x + self.radius, self.y + self.radius ),
            Point(self.x + self.radius, self.y - self.radius))
      #Tail if moving left
      else:
         self.tail= Polygon(
            Point(self.x, self.y),
            Point(self.x - self.radius, self.y + self.radius),
            Point(self.x - self.radius, self.y - self.radius))
      
      self.tail.setFill(self.color)
      self.tail.setOutline(self.color)
      
      # Head
      self.head = Circle(Point(self.x, self.y), self.radius/ 1.12)
      self.head.setFill(self.color)

   #Draws head and tail
   def draw(self, window):
      
      self.win = window 
      self.head.draw(window)
      self.tail.draw(window)
      
   #Undraws head and tail   
   def undraw(self):
      
      self.head.undraw()
      self.tail.undraw()

   #Moves the parts of the fish
   def move(self, dx, dy):
      
      self.x = self.x + dx
      self.y = self.y + dy
      self.head.move(dx, dy)
      
      self.tail.move(dx, dy)

   ##Keeps the fish from going off the screen
   def step(self):

      ##Right side of the screen
      if self.x > self.win.getWidth():
         self.reverse()

      ##Left side of the screen
      if self.x < 0   :
         self.reverse()
         
      self.move(self.velocity, 0)

   ##Reverse function to make the fish change directions
   def reverse(self):
      
      self.undraw()
      ## Change velocity to a negitive
      self.velocity = -self.velocity 
      self.build_fish()
      self.draw(self.win)


