'''cashregister

    Jonathan Branson, 2-1-2017

        The program acts like a cash register. The user enters the cost of the item, followed by the amount
        tendered. Then, the program calculates the change needed, and what amount of each (dollar, quarter, dime,
        nickel, and penny) that is need for the correct change. 


'''

import math


##User inputs price of item and tendered amount
itemPrice = input('Price of Item - $')
amtTendered =  input('Tendered amount - $')

##Start for Report 
print('==============')
print('----REPORT----')
print('==============')

##Print itemPrice
print('Purchase Price: $', itemPrice)

##Convert Tendered ammount to float and Print Tendered ammount
amtTendered = float(amtTendered)
amtTendered = amtTendered * 1
amtTendered = round(amtTendered, 2)
print('Amount Tendered: $', '%.2f' % amtTendered, '\n')

##Converting itemPrice and Tendered ammount to ints
itemPrice = float(itemPrice)
itemPrice = itemPrice * 100
itemPrice = round(itemPrice, 2)
itemPrice = int(itemPrice)
amtTendered = amtTendered * 100
amtTendered = int(amtTendered)

##Calculate change and convert to float print change amount
change = amtTendered - itemPrice
change = float(change)
change = change * .01
print('Change: $', '%.2f' % change)

##Calculate ammount of Dollar bill needed for change and print ammount of dollars to return
dollars = int(change / 1)
print(dollars, '- One-Dollar bill(s)')

##Convert dollars to float and subtract from change
dollars = float(dollars) 
dollars = dollars * 1
change = change - dollars
change = round(change, 2)

##Calculate ammount of quarters needed for change and print ammount of quarters to return
quarters = int(change / .25)
print(quarters, '- Quarter(s)')

##Convert quarters to float and subtract from change
quarters = float(quarters)
quarters = quarters * .25
change = change - quarters
change = round(change, 2)

##Calculate ammount of dimes needed for change and print ammount of dimes to return
dimes = int(change / .10)
print(dimes, '- Dime(s)')

##Convert dimes to float and subtract from change
dimes = float(dimes)
dimes = dimes * .10
change = change - dimes
change = round(change, 2)

##Calculate ammount of nickles needed for change and print ammount of nickles to return
nickles = int(change / .05)
print(nickles, '- Nickles(s)')

##Convert nickles to float and subtract from change
nickles = float(nickles)
nickles = nickles * .05
change = change - nickles
change = round(change, 2)

##Calculate ammount of pennys needed for change and print ammount of pennys to return
pennys = int(change / .01)
print(pennys, '- Penny(s)')

##Convert pennys to float and subtract from change
pennys = float(pennys)
pennys = pennys * .01
change = change - pennys
change = round(change, 2)
