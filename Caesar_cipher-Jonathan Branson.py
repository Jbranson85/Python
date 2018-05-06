'''
Jonthan Branson-Caesar_cipher

Adapted from a programs written by Dr. Melissa Stange(simplecipher.py, string2.py)

In this program allows the user to enter in a message, and will then be asked
how many shifts they would like. The message will then be encoded and returned
to the user.

At this point in time only letters can be used in the message, however the message
can contain lower case and upper case letters.

'''

##This funtion takes the imput of the message and shirt number calculates and returns encoded message
def caesar(plain_Text, num_Shift):
    
    ##Empty string for future encoded message
    plain_Text2 = ""

    ##Loops though the message(plain_Text), loop will run for every chr or space in the message
    for ch in plain_Text:

        ##Condition 1,  by uses the ord function which will change the ch into its unicode number and add it to the shift amount
        if ch in "abcdefghijklmnopqrstuvwxyz":

            num_1 = (ord(ch) + num_Shift)

            if num_1 > ord("z"):
                num_1 -= 26
            elif num_1 < ord("a"):
                num_1 += 26

            plain_Text2 = plain_Text2 + chr(num_1)
            
        ##Condition 2,  by uses the ord function which will change the ch into its unicode number and add it to the shift amount
        elif ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

            num_1 = (ord(ch) + num_Shift)

            if num_1 > ord("Z"):
                num_1 -= 26
            elif num_1 < ord("A"):
                num_1 += 26

            plain_Text2 = plain_Text2 + chr(num_1)
        ##Condition 3, used for anything that does not meet the requirements for Condition 1 and Condition 2
        else:
            plain_Text2 = plain_Text2 + ch

    ##Returns encoded message
    return plain_Text2

##Main function
def main():
    ##Inputs
    plain_Text = input("What is you plaintext?")
    num_Shift = int(input("What shift do you want to use?"))
    
    ##Call function caesar using the message and shift amount and returning encoded message
    plain_Text2 = caesar(plain_Text,num_Shift)

    ##Print encoded message
    print("Your ciphertext is: ", plain_Text2)
    
main()
