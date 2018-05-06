'''
Jonathan Branson -  blackjack_JBranson.py - Black Jack game
4/23/17

Adapted from programs written by Dr. Melissa Stange
Adapted from programs written / owned by python.org
Adapted from programs written by A.N. Harrington
Adapted from program written by Jonathan Branson

Its the game of blackjack with gambleing. The user will try to bet the house. User will will go first and only see one card that the dealer is holding.
User will have the choice to hit(take another card and increase amount) or stay(stay at current amount). Limited to a total of 5 cards in hand. Once user
stays, computer will then try to beat user and get closer to 21. If both hold the same dealer will break tie and try to beat player.

User will be able to place bets of 100 500 and 1000 chips, game ends when player out of chips or player wants to cash out.

'''
import tkinter
from tkinter.constants import *
import random
from tkinter import *
import math
import textwrap

##Build window and frame
tk = tkinter.Tk()
tk.wm_title("BlackJack")
tk.geometry('525x525')
frame = tkinter.Frame(tk)
frame.place(height=525, width=525)
tk.resizable(0,0)

#Initialize the to global varibles used (1st time)
bet = 0
chips = 1000

##If file not found for background image, then load a green background
try:
    ##Imports the background image
    photo = PhotoImage(file='Blackjack_table.png')
    labl_Main= Label(frame, image=photo)
    labl_Main.pack()
    
except:

    frame.configure(background = "#0f3d0f")

##Random number gens, and change by numbers for ascii code, 
def draw_Cards():

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

    ##Loop to check for doubles of cards, so only one of each card can be used
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
            
    ##Loads the card labels with card that is being useed
    card_Labels(card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10)
    
    ##Returns varibles for cards 1-10 to main function
    return (card_1, card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10)

##Function to load and build cards for the gui
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
        
##Builds and shows total of dealers cards that dealer is showing
def dealer_Holding_Label(dealer_showing):
    
    global label_Dshow  
    label_Dshow = tkinter.Label(frame,text= dealer_showing, font=("Fixedsys", 24), bg = '#0f3d0f', fg = "white")
    label_Dshow.place(x = 100,y = 100)

##Calculates what the dealer is showing from the first two cards, but one shows player one card
def dealer_Show(card_1, card_2):

    ##Dealer Card 1
    if any ('K'or 'Q' or 'J' or '10'  in s for s in card_1):
        dealer_Card1 = 10
    if any ('A' in s for s in card_1):
        dealer_Card1 = 11 
    if any ('9' in s for s in card_1):
       dealer_Card1 = 9
    if any ('8' in s for s in card_1):
       dealer_Card1 = 8
    if any ('7' in s for s in card_1):
        dealer_Card1 = 7
    if any ('6' in s for s in card_1):
        dealer_Card1 = 6
    if any ('5' in s for s in card_1):
        dealer_Card1 = 5
    if any ('4' in s for s in card_1):
        dealer_Card1 = 4
    if any ('3' in s for s in card_1):
        dealer_Card1 = 3
    if any ('2' in s for s in card_1):
        dealer_Card1 = 2

    ##Updates dealer_showing label and sends it to the function for that label
    dealer_showing = 'Dealer Is Showing: {}'.format(dealer_Card1)
    dealer_Holding_Label(dealer_showing)
    
    ##Dealer Card 2
    if any ('K'in s for s in card_2):
        dealer_Card2 = 10
    if any ('Q'in s for s in card_2):
        dealer_Card2 = 10
    if any ('J'in s for s in card_2):
        dealer_Card2 = 10
    if any ('10'in s for s in card_2):
        dealer_Card2 = 10
    if any ('A' in s for s in card_2):
        dealer_Card2 = 11
        if any ('A' in s for s in card_1):
            dealer_Card2 = 1 
    if any ('9' in s for s in card_2):
        dealer_Card2 = 9
    if any ('8' in s for s in card_2):
        dealer_Card2 = 8
    if any ('7' in s for s in card_2):
        dealer_Card2 = 7
    if any ('6' in s for s in card_2):
        dealer_Card2 = 6
    if any ('5' in s for s in card_2):
        dealer_Card2 = 5
    if any ('4' in s for s in card_2):
        dealer_Card2 = 4
    if any ('3' in s for s in card_2):
        dealer_Card2 = 3
    if any ('2' in s for s in card_2):
        dealer_Card2 = 2

    ##Total for what dealer is holding
    dealer_Card2 = dealer_Card2 + dealer_Card1
    ##Show dealers first cards only
    label_Card1.place(x = 115,y = 150)

    ##Returning both since only one of the dealers cards will be shown at first, but will need total for end game
    return dealer_Card1,dealer_Card2

##Builds and shows total of player cards that player is showing
def player_HoldingLabel(player_Cards):
    
    global label_Ushow
    user_Show = 'Player Is Showing: {}'.format(player_Cards)
    label_Ushow = tkinter.Label(frame,text= user_Show, font=("Fixedsys", 24), bg = '#0f3d0f', fg = "white")
    label_Ushow.place(x = 90,y = 350)

##Calculates what the player is showing from the first two cards
def player_Show(card_3, card_4):

    ##Player Card 1
    if any ('K' or 'Q' or 'J' or '10' in s for s in card_3):
        player_Cards = 10
    if any ('A' in s for s in card_3):
        player_Cards = 11 
    if any ('9' in s for s in card_3):
        player_Cards = 9
    if any ('8' in s for s in card_3):
        player_Cards = 8
    if any ('7' in s for s in card_3):
        player_Cards = 7
    if any ('6' in s for s in card_3):
        player_Cards = 6
    if any ('5' in s for s in card_3):
        player_Cards = 5
    if any ('4' in s for s in card_3):
        player_Cards = 4
    if any ('3' in s for s in card_3):
        player_Cards = 3
    if any ('2' in s for s in card_3):
        player_Cards = 2
    
    ##Player Card 2
    if any ('K' in s for s in card_4):
        player_Cards += 10
    if any ('Q' in s for s in card_4):
        player_Cards += 10
    if any ('J' in s for s in card_4):
        player_Cards += 10
    if any ('10' in s for s in card_4):
        player_Cards += 10
    if any ('A' in s for s in card_4):
        player_Cards += 11
        if any ('A' in s for s in card_3):
            player_Cards -= 10          
    if any ('9' in s for s in card_4):
        player_Cards += 9
    if any ('8' in s for s in card_4):
        player_Cards += 8
    if any ('7' in s for s in card_4):
        player_Cards += 7
    if any ('6' in s for s in card_4):
        player_Cards += 6
    if any ('5' in s for s in card_4):
        player_Cards += 5
    if any ('4' in s for s in card_4):
        player_Cards += 4
    if any ('3' in s for s in card_4):
        player_Cards += 3
    if any ('2' in s for s in card_4):
        player_Cards += 2

    ##Show players first two cards
    label_Card3.place(x = 115,y = 300)
    label_Card4.place(x = 230,y = 300)

    ##Set label for what player is currently holding
    player_HoldingLabel(player_Cards)
    
    ##Return players total hand
    return player_Cards

##Hit button command
def hit(card_5, card_6, card_7, card_3, card_4,dealer_Card2,hit_Count,dealer_Count):

     ##Clears player showing label
     label_Ushow.place_forget()
     ##Hides hit button
     button_Hit.place_forget()

     ##Calles the global variable so it can be updated
     global player_Cards
     
     ##First time hit button is clicked
     if hit_Count == 0:
         
         label_Card5.place(x = 345,y = 300)
         if any ('K' in s for s in card_5):
            player_Cards += 10
         if any ('Q' in s for s in card_5):
            player_Cards += 10
         if any ('J' in s for s in card_5):
            player_Cards += 10
         if any ('10' in s for s in card_5):
            player_Cards += 10
         if any ('A' in s for s in card_5):
            player_Cards += 11
            if any ('A' in s for s in card_3) or \
               any ('A' in s for s in card_4):
                player_Cards -= 10 
         if any ('9' in s for s in card_5):
            player_Cards += 9
         if any ('8' in s for s in card_5):
            player_Cards += 8
         if any ('7' in s for s in card_5):
            player_Cards += 7
         if any ('6' in s for s in card_5):
            player_Cards += 6
         if any ('5' in s for s in card_5):
            player_Cards += 5
         if any ('4' in s for s in card_5):
            player_Cards += 4
         if any ('3' in s for s in card_5):
            player_Cards += 3
         if any ('2' in s for s in card_5):
            player_Cards += 2

    ##Second time hit button is clicked
     if hit_Count == 1:
         
        label_Card6.place(x = 5,y = 300)
        if any ('K' in s for s in card_6):
           player_Cards += 10
        if any ('Q' in s for s in card_6):
            player_Cards += 10
        if any ('J' in s for s in card_6):
            player_Cards += 10
        if any ('10' in s for s in card_6):
            player_Cards += 10
        if any ('A' in s for s in card_6):
            player_Cards += 11
            if any ('A' in s for s in card_3) or \
               any ('A' in s for s in card_4) or \
               any ('A' in s for s in card_5):
                player_Cards -= 10 
        if any ('9' in s for s in card_6):
            player_Cards += 9
        if any ('8' in s for s in card_6):
            player_Cards += 8
        if any ('7' in s for s in card_6):
            player_Cards += 7
        if any ('6' in s for s in card_6):
            player_Cards += 6
        if any ('5' in s for s in card_6):
            player_Cards += 5
        if any ('4' in s for s in card_6):
            player_Cards += 4
        if any ('3' in s for s in card_6):
            player_Cards += 3
        if any ('2' in s for s in card_6):
            player_Cards += 2

    ##Last time button can be clicked player will then be a max card limit  
     if hit_Count == 2:
         
        label_Card7.place(x = 440,y = 300)
        if any ('K' in s for s in card_7):
            player_Cards += 10
        if any ('Q' in s for s in card_7):
            player_Cards += 10
        if any ('J' in s for s in card_7):
            player_Cards += 10
        if any ('10' in s for s in card_7):
            player_Cards += 10
        if any ('A' in s for s in card_7):
            player_Cards += 11
            if any ('A' in s for s in card_3) or \
               any ('A' in s for s in card_4) or \
               any ('A' in s for s in card_5) or \
               any ('A' in s for s in card_6):
                player_Cards -= 10 
        if any ('9' in s for s in card_7):
            player_Cards += 9
        if any ('8' in s for s in card_7):
            player_Cards += 8
        if any ('7' in s for s in card_7):
            player_Cards += 7
        if any ('6' in s for s in card_7):
            player_Cards += 6
        if any ('5' in s for s in card_7):
            player_Cards += 5
        if any ('4' in s for s in card_7):
            player_Cards += 4
        if any ('3' in s for s in card_7):
            player_Cards += 3
        if any ('2' in s for s in card_7):
            player_Cards += 2

     ##Adding one for counter
     hit_Count += 1

     ##Update labels to what player is now holding
     player_HoldingLabel(player_Cards)

     ##Return back to Hit button function
     hit_Button(card_5, card_6, card_7, card_3, card_4,dealer_Card2,hit_Count,dealer_Count)

     
     ##Checks for user over 21 and will end game
     if player_Cards > 21:

         endgame(dealer_Card2,player_Cards,dealer_Count)
         
     return player_Cards
    
##Stay button function
def stay(card_8, card_9, card_10, dealer_Card2, dealer_Count):

    ##Turns player_Cards to global, only I could find to get the correct ammount needed(1st)
    global player_Cards
    
    ##Hides what dealer is showing
    label_Dshow.place_forget()
    
    ##Display and up date cards and what deal is showing
    label_Card2.place(x = 225,y = 150)
    
    ##Loop for AI to determine how to beat player
    while  dealer_Card2 < 21 and dealer_Card2 <= player_Cards and dealer_Count < 3 or dealer_Card2 == player_Cards :

        
        ##Dealer Card 3
        if dealer_Count == 0:
            
                label_Card8.place(x = 345,y = 150) 
                if any ('K' in s for s in card_8):
                    dealer_Card2 += 10
                if any ('Q' in s for s in card_8):
                    dealer_Card2 += 10
                if any ('J' in s for s in card_8):
                    dealer_Card2 += 10
                if any ('10' in s for s in card_8):
                    dealer_Card2 += 10
                if any ('A' in s for s in card_8):
                    dealer_Card2 += 11 
                if any ('9' in s for s in card_8):
                    dealer_Card2 += 9
                if any ('8' in s for s in card_8):
                    dealer_Card2 += 8
                if any ('7' in s for s in card_8):
                    dealer_Card2 += 7
                if any ('6' in s for s in card_8):
                    dealer_Card2 += 6
                if any ('5' in s for s in card_8):
                    dealer_Card2 += 5
                if any ('4' in s for s in card_8):
                    dealer_Card2 += 4
                if any ('3' in s for s in card_8):
                    dealer_Card2 += 3
                if any ('2' in s for s in card_8):
                    dealer_Card2 += 2
                    
        ##Dealer Card 4   
        if dealer_Count == 1:
            
                label_Card9.place(x = 5,y = 150)
                if any ('K' in s for s in card_9):
                    dealer_Card2 += 10
                if any ('Q' in s for s in card_9):
                    dealer_Card2 += 10
                if any ('J' in s for s in card_9):
                    dealer_Card2 += 10
                if any ('10' in s for s in card_9):
                    dealer_Card2 += 10
                if any ('A' in s for s in card_9):
                    dealer_Card2 += 11 
                if any ('9' in s for s in card_9):
                    dealer_Card2 += 9
                if any ('8' in s for s in card_9):
                    dealer_Card2 += 8
                if any ('7' in s for s in card_9):
                    dealer_Card2 += 7
                if any ('6' in s for s in card_9):
                    dealer_Card2 += 6
                if any ('5' in s for s in card_9):
                    dealer_Card2 += 5
                if any ('4' in s for s in card_9):
                    dealer_Card2 += 4
                if any ('3' in s for s in card_9):
                    dealer_Card2 += 3
                if any ('2' in s for s in card_9):
                    dealer_Card2 += 2
                    
        ##Dealer Card 5
        if dealer_Count == 2:
            
                label_Card10.place(x = 440,y = 150)
                if any ('K' in s for s in card_10):
                    dealer_Card2 += 10
                if any ('Q' in s for s in card_10):
                    dealer_Card2 += 10
                if any ('J' in s for s in card_10):
                    dealer_Card2 += 10
                if any ('10' in s for s in card_10):
                    dealer_Card2 += 10
                if any ('A' in s for s in card_10):
                    dealer_Card2 += 11 
                if any ('9' in s for s in card_10):
                    dealer_Card2 += 9
                if any ('8' in s for s in card_10):
                    dealer_Card2 += 8
                if any ('7' in s for s in card_10):
                    dealer_Card2 += 7
                if any ('6' in s for s in card_10):
                    dealer_Card2 += 6
                if any ('5' in s for s in card_10):
                    dealer_Card2 += 5
                if any ('4' in s for s in card_10):
                    dealer_Card2 += 4
                if any ('3' in s for s in card_10):
                    dealer_Card2 += 3
                if any ('2' in s for s in card_10):
                    dealer_Card2 += 2

        ##Counter for loop, +1 every loop
        dealer_Count += 1
        
    ##Clear Dshow label after the loop    
    label_Dshow.place_forget()
    ##Update dealer holding after after the loop
    dealer_showing = 'Dealer Is Showing: {}'.format(dealer_Card2)
    dealer_Holding_Label(dealer_showing)
    
    ##Move to End Game function and determine the winner
    endgame(dealer_Card2,player_Cards,dealer_Count)

##End of the hand of the funtion, demands winner and moves to next funtion   
def endgame(dealer_Card2,player_Cards,dealer_Count):

    ##Hides buttons and labels
    button_Hit.place_forget()
    button_Stay.place_forget()
    label_Bet.place_forget()
    
    ##Checks for different conditions and goes to house_win or player_win function
    if dealer_Card2 == 21 and dealer_Count == 0:
        house_Win()
       
    elif dealer_Card2 > player_Cards and dealer_Card2 <= 21:
        house_Win()
       
    elif player_Cards > 21 and dealer_Card2 <= 21:
        house_Win()

    elif player_Cards > 21:
        house_Win()
        
    elif dealer_Card2 > 21 and player_Cards <= 21:
        player_Win()
        
    elif player_Cards <= 21 and player_Cards > dealer_Card2:
        player_Win()

##If the dealer win the hand this funtion displays the house wins, also contain player winner label for reset purposes
def house_Win():

    global label_houseWin
    label_houseWin = tkinter.Label(frame, text= 'HOUSE WINS!',  font=("Fixedsys", 34), bg = "#0f3d0f", fg = "red")
    label_houseWin.place(x = 100,y = 210)

    global label_Uwin
    label_Uwin = tkinter.Label(frame, text= '!!!WINNER!!!!',  font=("Fixedsys", 37), bg = "#0f3d0f", fg = "yellow")

    ##Activates reset and cashout buttons and also run hide button function to hide multi buttons
    reset_Button()
    cashout_Button()
    hide_buttons()
    
##If the player wins the hand this function displays the winner, contains dealer win label for reset purpose
def player_Win():

    ##Updates the chips global(2nd)
    global chips
    
    ##Clear old chip count
    label_Chips.place_forget()
    
    ##Updates chips for player win and displays new chip count
    chips = chips + (bet * 2)
    label_userChips(chips)
    
    global label_Uwin
    label_Uwin = tkinter.Label(frame, text= '!!!WINNER!!!!',  font=("Fixedsys", 37), bg = "#0f3d0f", fg = "yellow")
    label_Uwin.place(x =50, y = 210)

    global label_houseWin
    label_houseWin = tkinter.Label(frame, text= 'HOUSE WINS!',  font=("Fixedsys", 34), bg = "#0f3d0f", fg = "red")

    ##Activates reset and cashout buttons and also run hide button function to hide multi buttons
    reset_Button()
    cashout_Button()
    hide_buttons()

'''Cash out button function, displays labels for cash out screen, clears all labels no used for cash out screen
   , prepares for new game or quit game, calculates the total chip count, and converted to money'''
def cash_Out():
    button_restart.place(x=185,y=75)
    
    button_Cashout.place_forget()
    
    label_Dshow.place_forget()
    label_Ushow.place_forget()
    label_houseWin.place_forget()
    label_Uwin.place_forget()

    label_Bet.place_forget()
    label_Chips.place_forget()
    
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

    button_reset.place_forget()

    label_Title.place(x = 7,y = 150)
    label_Chips.place(x =25, y = 300)

    ##House Credit
    house_cred = -1000
    
    ##Init money for cash conversion
    money = 0

    global label_Cred
    house_cred_1 = 'House Credit: {}'.format(house_cred)
    label_Cred = tkinter.Label(frame, text = house_cred_1 , font=("Fixedsys", 24), bg = "#0f3d0f", fg = "red")
    label_Cred.place(x = 25, y = 350)

    global label_End
    global chips
    chips = chips + house_cred
    final_Chip = 'Final Chip Count: {}'.format(chips)
    label_End = tkinter.Label(frame, text = final_Chip , font=("Fixedsys", 24), bg = "#0f3d0f", fg = "yellow")
    label_End.place(x = 25, y = 400)

    global label_Cashout
    if chips < 0:
        label_Cashout = tkinter.Label(frame, text = "GAME OVER!!" , font=("Fixedsys", 48), bg = "#0f3d0f", fg = "red")
        label_Cashout.place(x = 35, y = 215)
    else:
        label_Cashout = tkinter.Label(frame, text = "CASHING OUT!" , font=("Fixedsys", 48), bg = "#0f3d0f", fg = "blue")
        label_Cashout.place(x = 25, y = 215)

    

    global label_Money
    ##Convert chips to float for money converstion
    money = float(chips) 
    final_money = 'Cash Out: ${}'.format('%.2f'%money)
    label_Money = tkinter.Label(frame, text = final_money , font=("Fixedsys", 24), bg = "#0f3d0f", fg = "white")
    label_Money.place(x = 25, y = 450)

##Hides buttons when player runs out of chips or game ends
def hide_buttons():

    if chips <= 0:
        cash_Out()
        button_Cashout.place_forget()
        button_reset.place_forget()
        
##Bet Label    
def label_userBet(bet):

    global label_Bet
    user_Bet = 'Your Bet: {}'.format(bet)
    label_Bet = tkinter.Label(frame, text = user_Bet, font=("Fixedsys", 24), bg = "#0f3d0f", fg = "orange")
    label_Bet.place(x = 140, y = 425)
    
##Chips Label
def label_userChips(chips):

    global label_Chips
    chip_Count = 'Chip Count: {}'.format(chips)
    label_Chips = tkinter.Label(frame, text = chip_Count, font=("Fixedsys", 24), bg = "#0f3d0f", fg = "yellow")
    label_Chips.place(x =120, y = 490)
    
##Place bet Label
def label_place_Bet():

    global label_placeBet
    label_placeBet = tkinter.Label(frame, text= "Place Your Bet", font=("Fixedsys", 26), fg = 'white', bg = '#0f3d0f')
    label_placeBet.place(x = 90,y = 325)
    
##Resets the game and starts back at main function of the program   
def reset():
    
    button_Cashout.place_forget()
    label_Dshow.place_forget()
    label_Ushow.place_forget()
    label_houseWin.place_forget()
    label_Uwin.place_forget()
    label_Bet.place_forget()
    label_Chips.place_forget()
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
    button_reset.place_forget()
    main()
    
##Hit button function 
def hit_Button(card_5, card_6, card_7, card_3, card_4,dealer_Card2,hit_Count,dealer_Count):

    global button_Hit

    button_Hit = tkinter.Button(frame,text="!HIT!", command= lambda : hit(card_5, card_6, card_7, card_3, card_4,dealer_Card2,hit_Count,dealer_Count),
                                font=("Fixedsys", 18), bg = "green", cursor = "hand2")
    button_Hit.place(x=280,y=210)

##Reset button function 
def reset_Button():

    global button_reset
    
    button_reset = tkinter.Button(frame,text="DEAL", font=("Fixedsys", 18), fg = "white" ,
                                 command=  lambda : reset() ,bg = "red", cursor = "hand2")
    button_reset.place(x=100,y=400)

##Stay button function 
def stay_Button(card_8, card_9, card_10, dealer_Card2, dealer_Count):

    global button_Stay

    button_Stay = tkinter.Button(frame,text="STAY", font=("Fixedsys", 18), command = lambda :stay(card_8, card_9, card_10, dealer_Card2, dealer_Count),
                             bg = "red",  cursor = "hand2")
    button_Stay.place(x=120,y=210)
    
##Cash out button function
def cashout_Button():

    global button_Cashout 
    button_Cashout = tkinter.Button(frame, text = "CASH OUT", font=("Fixedsys", 18), command = lambda : cash_Out(), bg = "yellow",
                                    fg = "black", cursor = "hand2")
    button_Cashout.place(x=275,y=400)
    
##Bet 100 button     
def bet_100():

    #(#2 bet)
    global bet
    bet = 100
    #(#3 chips)
    global chips
    chips = chips - bet
    label_userBet(bet)
    label_Chips.place_forget()
    label_userChips(chips)

    main_2()
    
def bet_500():

    #(#2 bet)
    global bet
    bet = 500
    #(#3 chips)
    global chips
    chips = chips - bet
    label_userBet(bet)
    label_Chips.place_forget()
    label_userChips(chips)
    main_2()

def bet_1000():

    #(#2 bet)
    global bet
    bet = 1000
    #(#3 chips)
    global chips
    chips = chips - bet
    label_userBet(bet)
    label_Chips.place_forget()
    label_userChips(chips)
    main_2()
    
##Once bet is selected this becomes the main program, until next hand
def main_2():

    ##hides buttons and labels
    button_bet100.place_forget()
    button_bet500.place_forget()
    button_bet1000.place_forget()
    label_Title.place_forget()
    label_Title1.place_forget()
    label_Title2.place_forget()
    label_placeBet.place_forget()

    ##Resets the global player cards to zero, global b/c program is losing the varible so where
    global player_Cards
    player_Cards = 0

    ##Reseting varibles for new game
    hit_Count = 0
    
    dealer_Count = 0
    
    dealer_Card1 = 0
    
    dealer_Card2 = 0
    
    card_1,card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10 = draw_Cards()

    dealer_Card1, dealer_Card2 = dealer_Show(card_1, card_2)

    player_Cards = player_Show(card_3, card_4)

    ##Calling buttons function for hit and stay
    hit_Button(card_5, card_6, card_7, card_3, card_4,dealer_Card2,hit_Count,dealer_Count)

    stay_Button(card_8, card_9, card_10, dealer_Card2, dealer_Count)

##Main Screen game labels and buttons
global label_Title
label_Title = tkinter.Label(frame, text= "High Stakes BlackJack", font=("Fixedsys", 26), fg = 'white', bg = '#0f3d0f')
label_Title.place(x = 7,y = 215)

global label_Title1
txt_Main = ("A",u"\u2661")
label_Title1 = tkinter.Label(frame, text= txt_Main, relief= "solid", font=("Fixedsys", 48), fg = 'red', bg = 'white')
label_Title1.place(x = 115,y = 100)

global label_Title2
txt_Main2 = ("J",u"\u2660")
label_Title2 = tkinter.Label(frame, text= txt_Main2, relief= "solid", font=("Fixedsys", 48), fg = 'black', bg = 'white')
label_Title2.place(x = 260,y = 100)

button_help = tkinter.Button(frame,text="HELP", font=("Fixedsys", 16), fg = "white" , command= lambda : helpWindow() ,bg = "red", cursor = "question_arrow")
button_help.place(x=475,y=5)

button_quit = tkinter.Button(frame,text="QUIT", font=("Fixedsys", 16), fg = "white" , command= lambda : quit_Game() ,bg = "blue", cursor = "hand2")
button_quit.place(x=5,y=5)

button_restart = tkinter.Button(frame,text="NEW GAME", font=("Fixedsys", 18), fg = "white" , command= lambda : restart_Game() ,bg = "Orange", cursor = "hand2")

##Reset game when reset button or new Game button pushed
def restart_Game():

    button_Cashout.place_forget()
    label_Dshow.place_forget()
    label_Ushow.place_forget()
    label_houseWin.place_forget()
    label_Uwin.place_forget()

    label_Bet.place_forget()
    label_Chips.place_forget()
    label_placeBet.place_forget()

    label_Cred.place_forget()
    label_End.place_forget()
    label_Cashout.place_forget()
    button_restart.place_forget()
    label_Money.place_forget()
    
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

    button_reset.place_forget()
    #(#3 bet)
    global bet
    bet = 0
    #(#3 chips)
    global chips
    chips = 1000
    main()


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

BET 100 – Bets 100 chips
BET 500 – Bets 500 chips
BET 1000 – Bets 1000 chips
DEAL – Start/Next Game
HELP – Help Menu
QUIT – Exit Game
RESTART – New/Fresh game
HIT - Add card to player’s hand
STAY – Player turn ends, dealer deals cards
CASH OUT – End Game, cashes player out'''

    Label(win, text= instruc, bg = "black", fg = "white", font=("Fixedsys"),  justify=LEFT ).pack()
    Button(win, text = 'Close Window', command=win.destroy).pack()
    
##Quit game function   
def quit_Game():
    quit()

##Main function, the start of the game
def main():
    
    label_userChips(chips)
    
    global button_bet100
    button_bet100 = tkinter.Button(frame, text = "Bet 100", font=("Fixedsys", 18), command = lambda : bet_100(),
                                   bg = "blue", fg = "cyan", cursor = "hand2")
    global button_bet500
    button_bet500 = tkinter.Button(frame, text = "Bet 500", font=("Fixedsys", 18), command = lambda : bet_500(),
                                   bg = "green", fg = "yellow", cursor = "hand2")
    global button_bet1000
    button_bet1000 = tkinter.Button(frame, text = "Bet 1000", font=("Fixedsys", 18), command = lambda : bet_1000(),
                                bg = "red", cursor = "hand2")

    ##Checks for chips so player can only bet if the have enough
    if chips >= 1000:
        
        button_bet100.place(x=20,y=400)
        button_bet500.place(x=187,y=400)
        button_bet1000.place(x=355,y=400)

    elif chips < 1000 and chips >= 500:
        
        button_bet100.place(x=20,y=400)
        button_bet500.place(x=187,y=400)

    elif chips < 500 and chips >= 100:

        button_bet100.place(x=20,y=400)

    label_place_Bet()

main()
tk.mainloop()
