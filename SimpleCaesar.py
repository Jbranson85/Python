##Jonathan Branson-SimpleCaesar.py

##This program creates a secert message using a simple encryption algorithm
##called a Csesar cipher, which shifts each letter ahead by 3 places.
##The program can also decode an encoded message using the opposite algorithm

##Sample log of execution:
##Your message to encode? Attack the zombies at dawn!
##The encoded messafe is dwwdfn wkh crpelhv dw gdzq!

##A helper that can perform either encryption or decryption, shifting every
##letter by the given number of places, wrapping around as necessary

def helper(message, shift):
    message = message.lower()
    print(message)
    secret = ""
    
    for c in message:
        
        if c in "abcdefghijklmnopqrstuvwxyz":
            num = ord(c)
            num += shift
    
            
            if num > ord("z"): ##wrap if necessary
                num -= 26
               
            elif num < ord("a"):
                num += 26
            secret = secret + chr(num)
        else:
            ##dont modify any non-letters in the message; just add
            secret = secret + c
                
       
    return secret

##Encrypts the given string using a Caesar cipher and return the result.
def encrypt(message):
    return helper(message,shift)

def decrypt(message):
    return helper(message, -shift)
    
##main program
msg = input("Your message to encode?")
shift = int(input("Number of shifts"))
if len(msg) > 0 and shift >= 0:
    secret = encrypt(msg)
    print("The encoded message is:" , secret)
else:
    ##empty message: wants to decrypt
    secret = input("Your message to decode? ")

if len(secret) > 0:
    msg = decrypt(secret)
    print("This decode message is: " , msg)
