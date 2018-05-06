'''

Jonathan Branson -  blackjack.py - Black Jack game

Its the game of blackjack with gambleing. The user will try to bet the house. User will will go first and only see one card that the dealer is holding.
User will have the choice to hit(take another card and increase amount) or stay(stay at current amount). Limited to a total of 5 cards in hand. Once user
stays, computer will then try to beat user and get closer to 21. If both hold the same dealer will break tie and try to beat player.

User will be able to place bets of 100 500 and 1000 chips, game end when player out of chips or player wants to cash out.


'''

import tkinter
from tkinter.constants import *
import random
from tkinter import *
import math
import textwrap
import sys
import os

##Restart Game
def restart_Game():
    python = sys.executable
    os.execl(python,python, * sys.argv)

##Builds the frame for the GUI and sets size, background image
tk = tkinter.Tk()
tk.geometry('525x525')
frame = tkinter.Frame(tk)
frame.place(height=525, width=525)
tk.resizable(0,0)

##Imports the background image
photo = PhotoImage(file='Untitled1.png')
labl_Main= Label(frame, image=photo)
labl_Main.pack()

count = 0
count2 = 0
user_H2 = 0
dealer_H1 = 0
dealer_H2 = 0
dealer_show = 0
chips = 1000
bet = 0

def cards():
    
    ##Random numbers to used to make up the cards
    ##Card 1
    Random_1  = random.randint(1,13) 
    Random_2 = random.randint(1,4)
    ##Card 2
    Random_3  = random.randint(1,13) 
    Random_4 = random.randint(1,4)
    ##Card 3
    Random_5  = random.randint(1,13)
    Random_6 = random.randint(1,4)
    ##Card 4
    Random_7  = random.randint(1,13)
    Random_8 = random.randint(1,4)
    ##Card 5
    Random_9  = random.randint(1,13)
    Random_10 = random.randint(1,4)
    ##Card 6
    Random_11  = random.randint(1,13)
    Random_12 = random.randint(1,4)
    ##Card 7
    Random_13  = random.randint(1,13)
    Random_14 = random.randint(1,4)
    ##Card 8
    Random_15  = random.randint(1,13)  
    Random_16 = random.randint(1,4)
    ##Card 9
    Random_17  = random.randint(1,13) 
    Random_18 = random.randint(1,4)
    ##Card 10
    Random_19  = random.randint(1,13)
    Random_20 = random.randint(1,4)
    
    
    ##A dictionary used to determine what what that value of the card will be
    card_Num = {1 : '2' , 2 : '3' , 3 : '4' , 4 : '5' , 5 : '6' , 6 : '7' , 7 : '8' , 8 : '9' , 9 : '10' , 10 : 'J' , 11 : 'Q' , 12 : 'K' , 13 : 'A'}

    ##A dictionary used to determine if card is a heart, diamond, spade, club, coverts the number into the unicode values to show a heart, diamond, spade and club
    type_Card = { 1 : (u"\u2661") , 2 : (u"\u2666") , 3 : (u"\u2660") , 4 : (u"\u2663")}

    ##Cards 1-10
    card_1 = (card_Num[Random_1],type_Card[Random_2])
    card_2 = (card_Num[Random_3],type_Card[Random_4])
    card_3 = (card_Num[Random_5],type_Card[Random_6])
    card_4 = (card_Num[Random_7],type_Card[Random_8])
    card_5 = (card_Num[Random_9],type_Card[Random_10])
    card_6 = (card_Num[Random_11],type_Card[Random_12])
    card_7 = (card_Num[Random_13],type_Card[Random_14])
    card_8 = (card_Num[Random_15],type_Card[Random_16])
    card_9 = (card_Num[Random_17],type_Card[Random_18])
    card_10 = (card_Num[Random_19],type_Card[Random_20])

    ##This loop test each card so that repeating cards to not appear in the same turn or hand
    while card_1 == card_2 or card_1 == card_3  or card_1 == card_4  or card_1 == card_5  or card_1 == card_6  or card_1 == card_7  or card_1 == card_8  or card_1 == card_9  or card_1 == card_10 or \
        card_2 == card_1 or card_2 ==  card_3  or card_2 ==  card_4  or card_2 ==  card_5  or card_2 ==  card_6  or card_2 ==  card_7  or card_2 ==  card_8  or card_2 ==  card_9  or card_2 ==  card_10 or \
        card_3 == card_2 or card_3 ==  card_1  or card_3 ==  card_4  or card_3 ==  card_5  or card_3 ==  card_6  or card_3 ==  card_7  or card_3 ==  card_8  or card_3 ==  card_9  or card_3 ==  card_10 or \
        card_4 == card_2 or card_4 ==  card_3  or card_4 ==  card_1  or card_4 ==  card_5  or card_4 ==  card_6  or card_4 ==  card_7  or card_4 ==  card_8  or card_4 ==  card_9  or card_4 ==  card_10 or \
        card_5 == card_2 or card_5 ==  card_3  or card_5 ==  card_4  or card_5 ==  card_1  or card_5 ==  card_6  or card_5 ==  card_7  or card_5 ==  card_8  or card_5 ==  card_9  or card_5 ==  card_10 or \
        card_6 == card_2 or card_6 ==  card_3  or card_6 ==  card_4  or card_6 ==  card_5  or card_6 ==  card_1  or card_6 ==  card_7  or card_6 ==  card_8  or card_6 ==  card_9  or card_6 ==  card_10 or \
        card_7 == card_2 or card_7 ==  card_3  or card_7 ==  card_4  or card_7 ==  card_5  or card_7 ==  card_6  or card_7 ==  card_1  or card_7 ==  card_8  or card_7 ==  card_9  or card_7 ==  card_10 or \
        card_8 == card_2 or card_8 ==  card_3  or  card_8 == card_4  or card_8 ==  card_5  or card_8 ==  card_6  or card_8 ==  card_7  or card_8 ==  card_1  or card_8 ==  card_9  or card_8 ==  card_10 or \
        card_9 == card_2 or card_9 ==  card_3  or card_9 ==  card_4  or card_9 ==  card_5  or card_9 ==  card_6  or card_9 ==  card_7  or card_9 ==  card_8  or card_9 ==  card_1  or card_9 ==  card_10 or \
        card_10 == card_2 or card_10 ==  card_3  or card_10 ==  card_4  or card_10 ==  card_5  or card_10 ==  card_6  or card_10 ==  card_7  or card_10 ==  card_8  or card_10 ==  card_9  or card_10 ==  card_1:

        ##List of condtions that will change any card that has already be drawn to become rerolled and retest until call cards are different, once again keep repeating card from appearing
        if card_1 == card_2 or card_1 == card_3  or card_1 == card_4  or card_1 == card_5  or card_1 == card_6  or card_1 == card_7  or card_1 == card_8  or card_1 == card_9  or card_1 == card_10 :
            Random_1  = random.randint(1,13)
            card_1 = (card_Num[Random_1],type_Card[Random_2])
        
        if card_2 == card_1 or card_2 ==  card_3  or card_2 ==  card_4  or card_2 ==  card_5  or card_2 ==  card_6  or card_2 ==  card_7  or card_2 ==  card_8  or card_2 ==  card_9  or card_2 ==  card_10 :
            Random_3  = random.randint(1,13)
            card_2 = (card_Num[Random_3],type_Card[Random_4])
        
        if card_3 == card_2 or card_3 ==  card_1  or card_3 ==  card_4  or card_3 ==  card_5  or card_3 ==  card_6  or card_3 ==  card_7  or card_3 ==  card_8  or card_3 ==  card_9  or card_3 ==  card_10 :
            Random_5 = random.randint(1,13)
            card_3 = (card_Num[Random_5],type_Card[Random_6])
    
        if card_4 == card_2 or card_4 ==  card_3  or card_4 ==  card_1  or card_4 ==  card_5  or card_4 ==  card_6  or card_4 ==  card_7  or card_4 ==  card_8  or card_4 ==  card_9  or card_4 ==  card_10 :
            Random_7  = random.randint(1,13)
            card_4 = (card_Num[Random_7],type_Card[Random_8])

        if card_5 == card_2 or card_5 ==  card_3  or card_5 ==  card_4  or card_5 ==  card_1  or card_5 ==  card_6  or card_5 ==  card_7  or card_5 ==  card_8  or card_5 ==  card_9  or card_5 ==  card_10 :
            Random_9  = random.randint(1,13)
            card_5 = (card_Num[Random_9],type_Card[Random_10])

        if card_6 == card_2 or card_6 ==  card_3  or card_6 ==  card_4  or card_6 ==  card_5  or card_6 ==  card_1  or card_6 ==  card_7  or card_6 ==  card_8  or card_6 ==  card_9  or card_6 ==  card_10 :
            Random_11  = random.randint(1,13)
            card_6 = (card_Num[Random_11],type_Card[Random_12])

        if card_7 == card_2 or card_7 ==  card_3  or card_7 ==  card_4  or card_7 ==  card_5  or card_7 ==  card_6  or card_7 ==  card_1  or card_7 ==  card_8  or card_7 ==  card_9  or card_7 ==  card_10 :
            Random_13  = random.randint(1,13)
            card_7 = (card_Num[Random_13],type_Card[Random_14])

        if card_8 == card_2 or card_8 ==  card_3  or  card_8 == card_4  or card_8 ==  card_5  or card_8 ==  card_6  or card_8 ==  card_7  or card_8 ==  card_1  or card_8 ==  card_9  or card_8 ==  card_10 :
            Random_15  = random.randint(1,13)
            card_8 = (card_Num[Random_15],type_Card[Random_16])

        if card_9 == card_2 or card_9 ==  card_3  or card_9 ==  card_4  or card_9 ==  card_5  or card_9 ==  card_6  or card_9 ==  card_7  or card_9 ==  card_8  or card_9 ==  card_1  or card_9 ==  card_10 :
            Random_17  = random.randint(1,13)
            card_9 = (card_Num[Random_17],type_Card[Random_18])

        if card_10 == card_2 or card_10 ==  card_3  or card_10 ==  card_4  or card_10 ==  card_5  or card_10 ==  card_6  or card_10 ==  card_7  or card_10 ==  card_8  or card_10 ==  card_9  or card_10 ==  card_1 :
            Random_19  = random.randint(1,13)
            card_10 = (card_Num[Random_19],type_Card[Random_20])


    return card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10


##Labels for all ten cards, used for styles of labels 
def card_Labels(card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10):

    global label_Card1
    label_Card1 = tkinter.Label(frame, text= card_1, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2661" in s for s in card_1) or any (u"\u2666" in s for s in card_1) :
        label_Card1.config(fg = 'red')
        
    global label_Card2
    label_Card2 = tkinter.Label(frame, text= card_2, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_2) or any (u"\u2661" in s for s in card_2):
        label_Card2.config(fg = 'red')

    global label_Card3   
    label_Card3 = tkinter.Label(frame, text= card_3, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_3) or any (u"\u2661" in s for s in card_3):
        label_Card3.config(fg = 'red')
        
    global label_Card4 
    label_Card4 = tkinter.Label(frame, text= card_4, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_4) or any (u"\u2661" in s for s in card_4):
        label_Card4.config(fg = 'red')

    global label_Card5
    label_Card5 = tkinter.Label(frame, text= card_5, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_5) or any (u"\u2661" in s for s in card_5):
        label_Card5.config(fg = 'red')

    global label_Card6
    label_Card6 = tkinter.Label(frame, text= card_6, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_6) or any (u"\u2661" in s for s in card_6):
        label_Card6.config(fg = 'red')

    global label_Card7
    label_Card7 = tkinter.Label(frame, text= card_7, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_7) or any (u"\u2661" in s for s in card_7):
        label_Card7.config(fg = 'red')
        
    global label_Card8
    label_Card8 = tkinter.Label(frame, text= card_8, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_8) or any (u"\u2661" in s for s in card_8):
        label_Card8.config(fg = 'red')

    global label_Card9
    label_Card9 = tkinter.Label(frame, text= card_9, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_9) or any (u"\u2661" in s for s in card_9):
        label_Card9.config(fg = 'red')

    global label_Card10
    label_Card10 = tkinter.Label(frame, text= card_10, relief= "solid", font=("Fixedsys", 24), bg = "white")
    if any (u"\u2666" in s for s in card_10) or any (u"\u2661" in s for s in card_10):
        label_Card10.config(fg = 'red')
  
##Label to show and style what dealer is holding
def dealerHolding():
    global label_Dshow
    label_Dshow = tkinter.Label(frame, text= dealer_show, font=("Fixedsys", 24), bg = '#0f3d0f', fg = "white")
##Label to show and style what player is holding 
def playerHolding():
    global label_Ushow
    label_Ushow = tkinter.Label(frame, text= user_Show, font=("Fixedsys", 24), bg = '#0f3d0f', fg = "white")

##Calculations used to show what the dealer is holding
def dealerShow(card_1, card_2):

    game_Labels()
    game_Labels_2(bet,chips)
    
    ##label_Chips.place(x =100, y = 490)
    ##label_Bet.place(x = 100, y = 450)

    ##Dealer Card 1
    if any ('K'or 'Q' or 'J' or '10'  in s for s in card_1):
        dealer_H1 = 10
    if any ('A' in s for s in card_1):
        dealer_H1 = 11 
    if any ('9' in s for s in card_1):
       dealer_H1 = 9
    if any ('8' in s for s in card_1):
       dealer_H1 = 8
    if any ('7' in s for s in card_1):
        dealer_H1 = 7
    if any ('6' in s for s in card_1):
        dealer_H1 = 6
    if any ('5' in s for s in card_1):
        dealer_H1 = 5
    if any ('4' in s for s in card_1):
        dealer_H1 = 4
    if any ('3' in s for s in card_1):
        dealer_H1 = 3
    if any ('2' in s for s in card_1):
        dealer_H1 = 2

    global dealer_show
    dealer_show = 'Dealer Is Showing: {}'.format(dealer_H1)
    dealerHolding()
    label_Dshow.config(text= dealer_show)
    label_Dshow.place(x = 100,y = 100)
        
    ##Dealer Card 2   
    if any ('K'in s for s in card_2):
        dealer_H2 = 10
    if any ('Q'in s for s in card_2):
        dealer_H2 = 10
    if any ('J'in s for s in card_2):
        dealer_H2 = 10
    if any ('10'in s for s in card_2):
        dealer_H2 = 10
    if any ('A' in s for s in card_2):
        dealer_H2 = 11
        if any ('A' in s for s in card_1):
            dealer_H2 = 1 
    if any ('9' in s for s in card_2):
        dealer_H2 = 9
    if any ('8' in s for s in card_2):
        dealer_H2 = 8
    if any ('7' in s for s in card_2):
        dealer_H2 = 7
    if any ('6' in s for s in card_2):
        dealer_H2 = 6
    if any ('5' in s for s in card_2):
        dealer_H2 = 5
    if any ('4' in s for s in card_2):
        dealer_H2 = 4
    if any ('3' in s for s in card_2):
        dealer_H2 = 3
    if any ('2' in s for s in card_2):
        dealer_H2 = 2

    ##Total for what dealer is holding
    dealer_H2 = dealer_H2 + dealer_H1
    ##Show dealers first cards only
    label_Card1.place(x = 115,y = 150)

    ##Returning both since only one of the dealers cards will be shown at first, but will need total for end game
    return dealer_H1,dealer_H2

##Calculations for determine what player is holding
def userShow(card_3, card_4):

    global user_H2

    ##Player Card 1
    if any ('K' or 'Q' or 'J' or '10' in s for s in card_3):
        user_H2 = 10
    if any ('A' in s for s in card_3):
        user_H2 = 11 
    if any ('9' in s for s in card_3):
        user_H2 = 9
    if any ('8' in s for s in card_3):
        user_H2 = 8
    if any ('7' in s for s in card_3):
        user_H2 = 7
    if any ('6' in s for s in card_3):
        user_H2 = 6
    if any ('5' in s for s in card_3):
        user_H2 = 5
    if any ('4' in s for s in card_3):
        user_H2 = 4
    if any ('3' in s for s in card_3):
        user_H2 = 3
    if any ('2' in s for s in card_3):
        user_H2 = 2
    
    ##Player Card 2
    if any ('K' in s for s in card_4):
        user_H2 += 10
    if any ('Q' in s for s in card_4):
        user_H2 += 10
    if any ('J' in s for s in card_4):
        user_H2 += 10
    if any ('10' in s for s in card_4):
        user_H2 += 10
    if any ('A' in s for s in card_4):
        user_H2 += 11
        if any ('A' in s for s in card_3):
            user_H2 -= 10          
    if any ('9' in s for s in card_4):
        user_H2 += 9
    if any ('8' in s for s in card_4):
        user_H2 += 8
    if any ('7' in s for s in card_4):
        user_H2 += 7
    if any ('6' in s for s in card_4):
        user_H2 += 6
    if any ('5' in s for s in card_4):
        user_H2 += 5
    if any ('4' in s for s in card_4):
        user_H2 += 4
    if any ('3' in s for s in card_4):
        user_H2 += 3
    if any ('2' in s for s in card_4):
        user_H2 += 2

    ##Show players first two cards
    label_Card3.place(x = 115,y = 300)
    label_Card4.place(x = 230,y = 300)

    global user_Show
    user_Show = 'Player Is Showing: {}'.format(user_H2)
    playerHolding()
    label_Ushow.config(text= user_Show)
    label_Ushow.place(x = 90,y = 350)
    
    ##Return players total hand
    return user_H2
    
##Hit button command
def hit(card_5, card_6, card_7, card_3, card_4,dealer_H2):

     global count
     global user_H2
     
    ##First time hit button is clicked
     if count == 0:
         
         label_Card5.place(x = 345,y = 300)
         if any ('K' in s for s in card_5):
            user_H2 += 10
         if any ('Q' in s for s in card_5):
            user_H2 += 10
         if any ('J' in s for s in card_5):
            user_H2 += 10
         if any ('10' in s for s in card_5):
            user_H2 += 10
         if any ('A' in s for s in card_5):
            user_H2 += 11
            if any ('A' in s for s in card_3) or \
               any ('A' in s for s in card_4):
                user_H2 -= 10 
         if any ('9' in s for s in card_5):
            user_H2 += 9
         if any ('8' in s for s in card_5):
            user_H2 += 8
         if any ('7' in s for s in card_5):
            user_H2 += 7
         if any ('6' in s for s in card_5):
            user_H2 += 6
         if any ('5' in s for s in card_5):
            user_H2 += 5
         if any ('4' in s for s in card_5):
            user_H2 += 4
         if any ('3' in s for s in card_5):
            user_H2 += 3
         if any ('2' in s for s in card_5):
            user_H2 += 2

    ##Second time hit button is clicked
     if count == 1:
         
        label_Card6.place(x = 5,y = 300)
        if any ('K' in s for s in card_6):
           user_H2 += 10
        if any ('Q' in s for s in card_6):
            user_H2 += 10
        if any ('J' in s for s in card_6):
            user_H2 += 10
        if any ('10' in s for s in card_6):
            user_H2 += 10
        if any ('A' in s for s in card_6):
            user_H2 += 11
            if any ('A' in s for s in card_3) or \
               any ('A' in s for s in card_4) or \
               any ('A' in s for s in card_5):
                user_H2 -= 10 
        if any ('9' in s for s in card_6):
            user_H2 += 9
        if any ('8' in s for s in card_6):
            user_H2 += 8
        if any ('7' in s for s in card_6):
            user_H2 += 7
        if any ('6' in s for s in card_6):
            user_H2 += 6
        if any ('5' in s for s in card_6):
            user_H2 += 5
        if any ('4' in s for s in card_6):
            user_H2 += 4
        if any ('3' in s for s in card_6):
            user_H2 += 3
        if any ('2' in s for s in card_6):
            user_H2 += 2

    ##Last time button can be clicked player will then be a max card limit  
     if count == 2:
         
        label_Card7.place(x = 440,y = 300)
        if any ('K' in s for s in card_7):
            user_H2 += 10
        if any ('Q' in s for s in card_7):
            user_H2 += 10
        if any ('J' in s for s in card_7):
            user_H2 += 10
        if any ('10' in s for s in card_7):
            user_H2 += 10
        if any ('A' in s for s in card_7):
            user_H2 += 11
            if any ('A' in s for s in card_3) or \
               any ('A' in s for s in card_4) or \
               any ('A' in s for s in card_5) or \
               any ('A' in s for s in card_6):
                user_H2 -= 10 
        if any ('9' in s for s in card_7):
            user_H2 += 9
        if any ('8' in s for s in card_7):
            user_H2 += 8
        if any ('7' in s for s in card_7):
            user_H2 += 7
        if any ('6' in s for s in card_7):
            user_H2 += 6
        if any ('5' in s for s in card_7):
            user_H2 += 5
        if any ('4' in s for s in card_7):
            user_H2 += 4
        if any ('3' in s for s in card_7):
            user_H2 += 3
        if any ('2' in s for s in card_7):
            user_H2 += 2


     user_Show = 'You Are Showing: {}'.format(user_H2)
     label_Ushow.config(text= user_Show)
     
     ##Adding one for counter
     count += 1
     
     ##Checks for user over 21 and will end game
     if user_H2 > 21:

         endgameDealer(dealer_H2, user_H2)
     
     return user_H2,count
     
            
##Hit button function 
def  hitButton(card_5, card_6, card_7, card_3, card_4,dealer_H2):

    button2 = tkinter.Button(frame,text="!HIT!", command= lambda : hit(card_5, card_6, card_7, card_3, card_4,dealer_H2), font=("Fixedsys", 18), bg = "green", cursor = "hand2")
    button2.place(x=280,y=225)
    
##Stay command function
def stay(card_8, card_9, card_10,dealer_H2):

    ##Two globals that will be used and updated in this function
    global count2
    global user_H2
    
    ##Display and up date cards and what deal is showing
    label_Card2.place(x = 225,y = 150)
    dealer_show = 'Dealer Is Showing: {}'.format(dealer_H2)
    label_Dshow.config(text= dealer_show)

    ##Checks for dealer holding 21 before drawing a card
    if dealer_H2 == 21:
        endgameDealer(dealer_H2,user_H2)

    ##Loop for AI to determine how to beat player
    while  dealer_H2 < 21 and dealer_H2 <= user_H2 and count2 < 3 or dealer_H2 == user_H2 :

        ##Dealer Card 3
        if count2 == 0:
            
                label_Card8.place(x = 345,y = 150) 
                if any ('K' in s for s in card_8):
                    dealer_H2 += 10
                if any ('Q' in s for s in card_8):
                    dealer_H2 += 10
                if any ('J' in s for s in card_8):
                    dealer_H2 += 10
                if any ('10' in s for s in card_8):
                    dealer_H2 += 10
                if any ('A' in s for s in card_8):
                    dealer_H2 += 11 
                if any ('9' in s for s in card_8):
                    dealer_H2 += 9
                if any ('8' in s for s in card_8):
                    dealer_H2 += 8
                if any ('7' in s for s in card_8):
                    dealer_H2 += 7
                if any ('6' in s for s in card_8):
                    dealer_H2 += 6
                if any ('5' in s for s in card_8):
                    dealer_H2 += 5
                if any ('4' in s for s in card_8):
                    dealer_H2 += 4
                if any ('3' in s for s in card_8):
                    dealer_H2 += 3
                if any ('2' in s for s in card_8):
                    dealer_H2 += 2
                    
        ##Dealer Card 4   
        if count2 == 1:
            
                label_Card9.place(x = 5,y = 150)
                if any ('K' in s for s in card_9):
                    dealer_H2 += 10
                if any ('Q' in s for s in card_9):
                    dealer_H2 += 10
                if any ('J' in s for s in card_9):
                    dealer_H2 += 10
                if any ('10' in s for s in card_9):
                    dealer_H2 += 10
                if any ('A' in s for s in card_9):
                    dealer_H2 += 11 
                if any ('9' in s for s in card_9):
                    dealer_H2 += 9
                if any ('8' in s for s in card_9):
                    dealer_H2 += 8
                if any ('7' in s for s in card_9):
                    dealer_H2 += 7
                if any ('6' in s for s in card_9):
                    dealer_H2 += 6
                if any ('5' in s for s in card_9):
                    dealer_H2 += 5
                if any ('4' in s for s in card_9):
                    dealer_H2 += 4
                if any ('3' in s for s in card_9):
                    dealer_H2 += 3
                if any ('2' in s for s in card_9):
                    dealer_H2 += 2
                    
        ##Dealer Card 5
        if count2 == 2:
            
                label_Card10.place(x = 440,y = 150)
                if any ('K' in s for s in card_10):
                    dealer_H2 += 10
                if any ('Q' in s for s in card_10):
                    dealer_H2 += 10
                if any ('J' in s for s in card_10):
                    dealer_H2 += 10
                if any ('10' in s for s in card_10):
                    dealer_H2 += 10
                if any ('A' in s for s in card_10):
                    dealer_H2 += 11 
                if any ('9' in s for s in card_10):
                    dealer_H2 += 9
                if any ('8' in s for s in card_10):
                    dealer_H2 += 8
                if any ('7' in s for s in card_10):
                    dealer_H2 += 7
                if any ('6' in s for s in card_10):
                    dealer_H2 += 6
                if any ('5' in s for s in card_10):
                    dealer_H2 += 5
                if any ('4' in s for s in card_10):
                    dealer_H2 += 4
                if any ('3' in s for s in card_10):
                    dealer_H2 += 3
                if any ('2' in s for s in card_10):
                    dealer_H2 += 2


        dealer_show = 'Dealer Is Showing: {}'.format(dealer_H2)
        label_Dshow.config(text= dealer_show)           
        ##Counter for loop
        count2 += 1
        
    ##Move to End Game function and determine the winner
    endgameDealer(dealer_H2,user_H2)

##Stay button function
def stayButton(card_8, card_9, card_10,dealer_H2):

    button3 = tkinter.Button(frame,text="STAY", font=("Fixedsys", 18), command = lambda :stay(card_8, card_9, card_10,dealer_H2), bg = "red",  cursor = "hand2")
    button3.place(x=150,y=225)

##Labels for Winner or Loser Message
def game_Labels():

    global label_houseWin
    label_houseWin = tkinter.Label(frame, text= 'HOUSE WINS!',  font=("Fixedsys", 34), bg = "#0f3d0f", fg = "red")

    global label_Uwin
    label_Uwin = tkinter.Label(frame, text= '!!!WINNER!!!!',  font=("Fixedsys", 37), bg = "#0f3d0f", fg = "yellow")

##Labels for Chips and Bet
def game_Labels_2(bet, chips):
    
    global label_Chips
    chip_Count = 'Chip Count: {}'.format(chips)
    label_Chips = tkinter.Label(frame, text = chip_Count, font=("Fixedsys", 24), bg = "#0f3d0f", fg = "yellow")
    label_Chips.place(x =120, y = 490)

    global label_Bet
    user_Bet = 'Your Bet: {}'.format(bet)
    label_Bet = tkinter.Label(frame, text = user_Bet, font=("Fixedsys", 24), bg = "#0f3d0f", fg = "orange")
    label_Bet.place(x = 140, y = 425)

##End Game function, will check multi cond. and determine the winner
def endgameDealer(dealer_H2,user_H2):

    ##Load game Label function and return house win and user win messages
    game_Labels()
    label_Bet.place_forget()

    if dealer_H2 == 21 and count2 == 0:
        house_Win()
       
    elif dealer_H2 > user_H2 and dealer_H2 <= 21:
        house_Win()
       
    elif user_H2 > 21 and dealer_H2 <= 21:
        house_Win()
        
    elif dealer_H2 > 21 and user_H2 <= 21:
        user_Win(bet)
        
    elif user_H2 <= 21 and user_H2 > dealer_H2:
        user_Win(bet)
        
    ##Display next Deal/bet buttons
    bet_buttons(chips)

##Function for determine what bets are allow depending on chips, includes if user is out of chips
def bet_buttons(chips):

    button_Cashout.place(x=195,y=460)

    if chips >= 1000:
        
        button_bet100.place(x=60,y=400)
        button_bet500.place(x=200,y=400)
        button_bet1000.place(x=340,y=400)

    elif chips < 1000 and chips >= 500:
        
        button_bet100.place(x=60,y=400)
        button_bet500.place(x=200,y=400)

    elif chips < 500 and chips >= 100:

        button_bet100.place(x=60,y=400)

    else:

        end_Game(chips)
        
        
##Reset function, hides labels
def reset():
    
    label_Card1.place_forget()
    label_Card2.place_forget()
    label_Card3.place_forget()
    label_Card4.place_forget()
    label_Card5.place_forget()
    label_Card6.place_forget()
    label_Card7.place_forget()
    label_Card8.place_forget()
    label_Card9.place_forget()
    label_Card10.place_forget()
    label_houseWin.place_forget()
    label_Uwin.place_forget()
    label_Ushow.place_forget()
    label_Dshow.place_forget()
    label_Bet.place_forget()
    label_Chips.place_forget()
    button_bet100.place_forget()
    button_bet500.place_forget()
    button_bet1000.place_forget()
    button_Cashout.place_forget()

##Function for the end game to show cash made or lost, depending more amount of chips
def end_Game(chips):

    reset()
    label_Title.place(x = 7,y = 150)
    label_Chips.place(x =75, y = 300)
    house_cred = -1000
    money = 0

    global label_Cred
    house_cred_1 = 'House Credit: {}'.format(house_cred)
    label_Cred = tkinter.Label(frame, text = house_cred_1 , font=("Fixedsys", 24), bg = "#0f3d0f", fg = "yellow")
    label_Cred.place(x = 75, y = 350)
    
    
    global label_End
    chips = chips + house_cred
    final_Chip = 'Final Chip Count: {}'.format(chips)
    label_End = tkinter.Label(frame, text = final_Chip , font=("Fixedsys", 24), bg = "#0f3d0f", fg = "yellow")
    label_End.place(x = 75, y = 400)

    if chips >= 0:

        global label_Cashout
        label_Cashout = tkinter.Label(frame, text = "CASHING OUT!" , font=("Fixedsys", 48), bg = "#0f3d0f", fg = "blue")
        label_Cashout.place(x = 25, y = 215)

    elif chips < 0:

        global label_Gameover
        label_Gameover = tkinter.Label(frame, text = "GAMEOVER!" , font=("Fixedsys", 48), bg = "#0f3d0f", fg = "red")
        label_Gameover.place(x = 75, y = 215)
        

    global label_Money
    money = float(chips) 
    final_money = 'Cash Out: ${}'.format('%.2f'%money)
    label_Money = tkinter.Label(frame, text = final_money , font=("Fixedsys", 20), bg = "#0f3d0f", fg = "white")
    label_Money.place(x = 75, y = 450)

    
    return

##User Win function, adds bet(times 2) to total chip count and updates global chip
def user_Win(bet):
    
    global chips
    label_Uwin.place(x =50, y = 215)
    chips = chips + (bet * 2)
    chip_Count = 'Chip Count: {}'.format(chips)
    label_Chips.config(text = chip_Count)

##Dealer Wins
def house_Win():

    label_houseWin.place(x = 100,y = 225)
    
##Deal next hand and varibles and labels being reset or hidden
def newDeal():
    
    reset()
    global count
    count = 0
    global count2
    count2 = 0
    user_H2 = 0
    user_Show = 'You Are Showing: {}'.format(user_H2)
    label_Ushow.config(text= user_Show)
    dealer_H1 = 0
    dealer_H2 = 0
    dealer_show = 'Dealer Is Showing: {}'.format(dealer_H2)
    label_Dshow.config(text= dealer_show)
    deal()
    
##Deal function, part of the main program controls cards labels, buttons, deal and user labels
def deal ():

    label_Title.place_forget()
    label_Title1.place_forget()
    label_Title2.place_forget()
    button_bet100.place_forget()
    button_bet500.place_forget()
    button_bet1000.place_forget()
    button.place_forget()
    ##button_newHand.place_forget()
    button_Cashout.place_forget()

    card_1,card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10 = cards()
    card_Labels(card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10)
    dealer_H1, dealer_H2 = dealerShow(card_1, card_2)
    user_H2 = userShow(card_3,card_4)
    hitButton(card_5, card_6, card_7, card_3, card_4,dealer_H2)
    stayButton(card_8, card_9, card_10,dealer_H2)

##Bet 100 function, linked to button 100
def bet_100():
    
    global bet
    bet = 100
    user_Bet = 'Your Bet: {}'.format(bet)
    label_Bet.config(text = user_Bet)
    
    global chips
    chips = int(chips - 100)
    chip_Count = 'Chip Count: {}'.format(chips)
    label_Chips.config(text = chip_Count)
    
    newDeal()

##Bet 500 function, linked to button 500
def bet_500():

    global bet
    bet = 500
    user_Bet = 'Your Bet: {}'.format(bet)
    label_Bet.config(text = user_Bet)
   
    global chips
    chips = int(chips - 500)
    chip_Count = 'Chip Count: {}'.format(chips)
    label_Chips.config(text = chip_Count)
    
    newDeal()

##Bet 1000 function, linked to button 1000
def bet_1000():

    global bet
    bet = 1000
    user_Bet = 'Your Bet: {}'.format(bet)
    label_Bet.config(text = user_Bet)
    
    global chips
    chips = int(chips - 1000)
    chip_Count = 'Chip Count: {}'.format(chips)
    label_Chips.config(text = chip_Count)
    
    newDeal()
##Guide for how to play game
def helpWindow():

    win = Toplevel()
    win.resizable(0,0)
   

    instruc =  '''How to Play: 
The game of black jack is a card that involves the player and a card dealer. If you understand
how to play and just want to know how this game works, skip down to Controls & Tips. If this
is your first time playing the object of the card game is to get as close to 21 as you can
without going over 21. You will start with two cards and are a loud to draw up to five cards,
but remember you must stay under 21. If at any point you go over 21, that hand will end and
the dealer wins the hand.Once you have decided that you don’t want to take another card you
will then will chose to stay and the dealer will then try to beat you. If a tie happens the
dealer will break the tie to try and beat the player. The closest one to 21 without going over
will win the hand. \n
Tips:
1.The first hand that player plays is free, after that player is given 1000 chips of house
credit to play with, and it will be deducted at the end of the game. 
2.The dealer’s cards will appear at the top of the game screen. At the start of the game
player is only allowed to see one of the dealer’s cards.
3.Player’s cards will appear at the bottom of the game screen.
4.Both dealer and players total amount of what their cards are worth will be shown, the dealers
is located above where the cards are shown and players will be at the bottom with their cards. 
5.To take a card, player will click the hit button, and one card will be added to player’s hand.
6.To stay, player will click the stay button, and dealer will then take try to beat player. 
7.Once the hand or turn is over three bet buttons will appear (100, 500, and 1000), once one is
clicked a new hand/ turn will begin. If player does not have the amount bet will not appear,
and if player is out of chips game will end. 
8.At the end of every hand / turn cash out button will appear which will end game and cash
player out.
9.Once player is out of chips or chooses to cash out, to play again just click the reset button
to play a new game.\n
Buttons:
DEAL – Starts Game
HELP – Help Menu
QUIT – Exit Game
RESTART – New/Fresh game
HIT - Add card to player’s hand
STAY – Player turn ends, dealer deals cards
BET 100 – Bets 100 chips
BET 500 – Bets 500 chips
BET 1000 – Bets 1000 chips
CASH OUT – End Game, cashes player out'''

    Label(win, text= instruc, bg = "black", fg = "white", font=("Fixedsys"),  justify=LEFT ).pack()
    Button(win, text = 'Close Window', command=win.destroy).pack()
    

def quit_Game():
    quit()


    
##Buttons for game/ main program    
button = tkinter.Button(frame,text="DEAL",command= deal, font=("Fixedsys", 36), fg = "white" , bg = "black", cursor = "hand2")
button.place(x=175,y=300)
button_help = tkinter.Button(frame,text="HELP", font=("Fixedsys", 16), fg = "white" , command= lambda : helpWindow() ,bg = "red", cursor = "question_arrow")
button_help.place(x=55,y=5)
button_quit = tkinter.Button(frame,text="QUIT", font=("Fixedsys", 16), fg = "white" , command= lambda : quit_Game() ,bg = "blue", cursor = "hand2")
button_quit.place(x=5,y=5)
button_restart = tkinter.Button(frame,text="RESTART", font=("Fixedsys", 16), fg = "white" , command= restart_Game ,bg = "Orange", cursor = "hand2")
button_restart.place(x=105,y=5)
button_bet100 = tkinter.Button(frame, text = "Bet 100", font=("Fixedsys", 16), command = lambda : bet_100(), bg = "blue", fg = "white", cursor = "hand2")
button_bet500 = tkinter.Button(frame, text = "Bet 500", font=("Fixedsys", 16), command = lambda : bet_500(), bg = "green", fg = "white", cursor = "hand2")
button_bet1000 = tkinter.Button(frame, text = "Bet 1000", font=("Fixedsys", 16), command = lambda : bet_1000(), bg = "red", fg = "white", cursor = "hand2")
button_Cashout = tkinter.Button(frame, text = "CASH OUT", font=("Fixedsys", 16), command = lambda : end_Game(chips), bg = "yellow", fg = "black", cursor = "hand2")

##Main Screen game labels
global label_Title
label_Title = tkinter.Label(frame, text= "High Stakes BlackJack", font=("Fixedsys", 26), fg = 'white', bg = '#0f3d0f')
label_Title.place(x = 7,y = 215)

global label_Title1
txt_Main = ("A",u"\u2661")
label_Title1 = tkinter.Label(frame, text= txt_Main, relief= "solid", font=("Fixedsys", 48), fg = 'red', bg = 'white')
label_Title1.place(x = 125,y = 100)

global label_Title2
txt_Main2 = ("J",u"\u2660")
label_Title2 = tkinter.Label(frame, text= txt_Main2, relief= "solid", font=("Fixedsys", 48), fg = 'black', bg = 'white')
label_Title2.place(x = 275,y = 100)

tk.mainloop()
