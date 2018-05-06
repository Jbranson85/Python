'''
StringTest_Jonathan_Branson.py

Jonathan Branson 3/19/17

Adapted from a program written by Prof. Stange, 2017-01-01
Adapted from a program witten by Jonathan Branson 2017-03-08

This program ask the user for a string, once the string is enter a menu will appear. The user will then
have 6 options to choose from. Each of the 6 options have there own funtion. The options will allow user to count
the number of chars in the string, count the number of letters in the string, count vowels, check to see if string
is palindrome, do a caesar cipher with a 3 letter shift, and a quit program option.
'''

##Print screen for Menu options
def menu():
    
    print('\nA. How many characters are in the string?')
    print('B. How many letters are in the string?')
    print('C. How many vowels are in the string?')
    print('D. Is the string a palindrome?')
    print('E. What is the Caesar Cipher (shift 3) of the string?')
    print('Q. Quit \n')
    
##Choice A function, counts total number of characters, including spaces
def choice_A():

    total_Chars = len(user_String)
    print("Total number of Chars: " , total_Chars)

    ##Return to menu function so user can choose another option for their string
    menu()
    user_Choice = input("Your choice: ")
    operations(user_Choice, user_String)

##Choice B fuction, counts total number of letters, not including spaces
def choice_B():

    ##Find total number oo characters and subtact from the total number of spaces
    total_Chars2 = len(user_String)
    print("Total number of letters: " , total_Chars2 - user_String.count(" "))

    ##Return to menu function so user can choose another option for their string
    menu()
    user_Choice = input("Your choice: ")
    operations(user_Choice, user_String)

##Choice C function, count total number of vowles
def choice_C():

    total_Vowles = 0

    ##Loop for finding all vowles in string
    for char in user_String:
        if char in "AEIOUaeiou":
            ##counter
            total_Vowles += 1

    print("Total number of Vowles: " , total_Vowles)

    ##Return to menu function so user can choose another option for their string
    menu()
    user_Choice = input("Your choice: ")
    operations(user_Choice, user_String)

##Choice D function, finding the palindrome of the string
def choice_D():

    ##Flips string in reverse order
    user_Palindrome = user_String[::-1]

    ##Checks to see if the palindrome is equal to the users string or not equal to users string
    if user_Palindrome == user_String:

        print("\nYour string is Palindrome")
        print("User string = " ,user_String)
        print("Palindrom string = " ,user_Palindrome)

    else:
        
        print("Your string is not Palindrome")
        print("User string = " ,user_String)
        print("Palindrom string = " ,user_Palindrome)

    ##Return to menu function so user can choose another option for their string
    menu()
    user_Choice = input("Your choice: ")
    operations(user_Choice, user_String)

##Choice_E function, used for creating the 3 letter shift caesar cipher to the string
def choice_E():

    user_String2 = ""
    ##Number of shifts
    num_Shift = 3

    ##Loop for all the characters of the string so it can be chanaged with the shift of 3
    for ch in user_String:

        ##Checks for lower case
        if ch in "abcdefghijklmnopqrstuvwxyz":

            num_1 = (ord(ch) + num_Shift)

            if num_1 > ord("z"):
                num_1 -= 26
            elif num_1 < ord("a"):
                num_1 += 26

            user_String2 = user_String2 + chr(num_1)
            
        ##Check for upper case
        elif ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            num_1 = (ord(ch) + num_Shift)

            if num_1 > ord("Z"):
                num_1 -= 26
            elif num_1 < ord("A"):
                num_1 += 26

            user_String2 = user_String2 + chr(num_1)
            
        ##Incease either condtion is meet
        else:
            plain_Text2 = plain_Text2 + ch

    ##print cipher text
    print("Your string ciphered is: " , user_String2)

    ##Return to menu function so user can choose another option for their string
    menu()
    user_Choice = input("Your choice: ")
    operations(user_Choice, user_String)

    
##Function for quitting the program
def choice_Q():
    quit()

##Funtion used for the users input for there choice
def operations(user_Choice, user_String):

    ##Conditions for users choice, user choice will take user to function for the choice that they have choosen
    if user_Choice == 'A' or user_Choice == 'a':
        choice_A()

    elif user_Choice == 'B' or user_Choice == 'b':
        choice_B()

    elif user_Choice == 'C' or user_Choice == 'c':
        choice_C()

    elif user_Choice == 'D' or user_Choice == 'd':
        choice_D()

    elif user_Choice == 'E' or user_Choice == 'e':
        choice_E()

    elif user_Choice == 'Q' or user_Choice == 'q':
        choice_Q()

    ##If user choice is not one of the 6 choices
    else:
        print('Please choose either letters A-E or Q. \n')
        menu()
        user_Choice = input("Your choice: ")
        operations(user_Choice, user_String)
        
    

##Main program
user_String = input("Please enter a sting.")
menu()
user_Choice = input("Your choice: ")
operations(user_Choice, user_String)
    



