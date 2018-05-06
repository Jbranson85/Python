'''
drawface.py

Jonathan Branson, 3/27/17

This program will draw a face that has 2 eyes, nose and a mouth, by using the
tkinter mondule to draw the shapes on a canvas

'''

from tkinter import *



##Builds Frame
root = Tk()

##Creates the Canvas, for shapes to be drawn on
background = Canvas(root, width = 525, height = 525, bg = "yellow")

##Draws the Head using a circle
head = background.create_oval(25,25,500,500, fill="purple")

##Draws the left eye using 2 circles
eye_1 = background.create_oval(125,105,220,200, fill = "white")
innereye_1 = background.create_oval(160,140,180,160, fill = "green")

##Draws the right eye using 2 circles
eye_2 = background.create_oval(285,105,385,200, fill = "white")
innereye_2 = background.create_oval(325,140,345,160, fill = "green")

##Draws the mouth using a arc
mouth = background.create_arc(125,300,385,450, start = 0, extent = -180, fill = "black")

##Draws the nose with 2 lines
nose_1 = background.create_line(250,200,185,325)
nose_2 = background.create_line(185,325,260,325)

##Packs the Canvas
background.pack()

##Loops main program
root.mainloop()


