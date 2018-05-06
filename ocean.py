'''

Jonathan Branson - ocean.py

Adapted from programs written by Dr. Melissa Stange - 01-01-2017 

This program will show a ocean, with fish swimming around and bubbles
rising to the top of the water. (Bubbles program is currently not working)
The program will have a random number of fish and random color and will bounce
back and forth across the screen.

This program uses 2 other program bubbles.py and fish.py, which are imported in.


'''

from graphics import *
import time
from random import randint
from fish import *
from bubbles import *

#Main program
def main():

   #Creats window
   winHeight = 300
   winWidth = 500
   win = GraphWin('Ocean', winWidth, winHeight)
   win.setBackground('blue')

   #For loop to creat bubbles(not currently working)
   bubs = []
   for b in range(randint(1,1)):
      x_1 = randint(0,winWidth)
      y_1 = 100
      radius_1 = randint(10,20)
      velocity_1 = randint(-10,10)

      #Send varibles to bubble program
      bubble_1= Bubbles(x_1, y_1, radius_1,velocity_1)
      bubble_1.draw(win)
      bubs.append(bubble_1)
      
   # For loop to create 8 - 15 fish
   fishys= []
   for i in range(randint(8,15)):
      x = randint(0,winWidth)
      y = randint(0,winHeight)
      radius = randint(10,50)
      color = color_rgb(randint(0,255), randint(0,255), randint(0,255))
      velocity = randint(1,2)

      #Sends varibles to Fish_2 program
      fish_1= Fish_2(x, y, radius, color, velocity)
      fish_1.draw(win)
      fishys.append(fish_1)

   #Loop to for animations to contine moving well program is running
   while True:
      
      for fish_1 in fishys:
         fish_1.step()
         bubble_1.step()

      ##Quit program when you click on the screen
      if win.checkMouse():
         quit()
         
        
      

main()
