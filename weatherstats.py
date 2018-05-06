'''
Jonthan Branson - weatherstats.pv
4-9-17

Adapted from programs written by Dr. Melissa Stange
Adapted from programs written by Jonathan Branson
Adapted from codes written/owned by www.python.org


This program will read the file msp-temperatures.txt, however it will only work currently if the txt file is in the same
location or folder as the python program. The file itself contains weather temperatures from the daily high temps recored
from 1939 to 2014 at the St. Paul airport. The program will read the lines of the file and remove all the years, and the
temperatures that go along with those years. It then will calculate the mean value of all the temperatures for each year,
then will calculate the standard deviation for each year. Next the program will determine the highest mean temperature,
lowest mean temperature, highest standard deviation, and Lowest standard deviation out of all the years combined and will
display temperature or deviation and the year it was recorded. Lastly,the program will find the highest and lowest temperatures
every recorded and display them with the year in which it happened.

Has not been tested on apple or mac computer, the way they read files seems to be a little different then windows.
'''

#Imports used for program
import statistics
import math

#Function used to read the file
def loadWeatherData(file):

    #reads files and places data in a varible
    listOfNumbers = file.readlines()
    
    #Moves data collected form file to mean and standard deviation function
    mean(listOfNumbers)

#The mean and standard deviation function
def mean(listOfNumbers):

    #List to store all the years, mean values, and standard deviation values
    year_list = []
    mean_list = []
    dev_list = []

    #Loop to with throught all the years from 1939 to 2014, does one year per loop
    for i in range(0,76):
        
        listOfNumbers_1 = listOfNumbers[i]
        
        #Used to split the year off of each line 
        year = listOfNumbers_1.split(',', 1)[0]
        
        #Add year into a list
        year_list.append(year)

        #Used to split off the temperatures and not include the years
        listOfNumbers_1 = listOfNumbers_1.split(',',1)[1]
        
        #Convert temperatures into ints
        temp_ints = map(int, listOfNumbers_1.split(','))
        
        #Calculate the mean temperatures per year
        temps2 = statistics.mean(temp_ints)

        #Add tempertures into a list
        mean_list.append("{0:.2f}".format(temps2))

        #Calculate the standard deviation
        dev1 = statistics.stdev(map(int, listOfNumbers_1.split(',')))

        #Add the standard deviation into a list
        dev_list.append("{0:.2f}".format(dev1))
        
        #Prints out the year, the mean and standard deviation for each year
        print(year, "   {0:.2f}  ".format(temps2), "  {0:.2f}  ".format(dev1))

    #Calls the print out function and sends colected data to the print out function
    print_out(listOfNumbers,year_list, mean_list, dev_list,temps2,listOfNumbers_1)

##Function for find the highest and lowest temperature ever record from years 1939 to 2014
def highLow(listOfNumbers):

    #List to store all temps first for high, second for low 
    temp_list = []
    temp_lowList = []

    #Loop for find all temps
    for z in range(0,76):

        temps3 = listOfNumbers[z]

        #Used to split off the temperatures and not include the years
        temps3 = temps3.split(',',1)[1]

        #Convert temperatures into ints
        temp_ints2 = map(int, temps3.split(','))
        
        #Find max out of every year and add to list
        high = (max(temp_ints2))
        temp_list.append(high)
        
        #Convert temperatures into ints
        temp_ints3 = map(int, temps3.split(','))

        #Find min out of every year and add to list
        low = (min(temp_ints3))
        temp_lowList.append(low)

    #Return varibles to print_out function
    return (temp_list, temp_lowList)
    
 
##Funcation to first to find Highest and Lowest(mean, standard deviation) compare all the years and print results
def print_out(listOfNumbers,year_list, mean_list, dev_list,temps2,listOfNumbers_1):

    #Used the index numbers of the all the list to compare temps and standard deviation to find the highs and lows, and the year, then print out results
    x2 = (mean_list.index(max(mean_list)))
    print('\nHighest mean temperature:',(max(mean_list)), "--",year_list[x2])
    
    x3 = (mean_list.index(min(mean_list)))
    print('Lowest mean temperature:',(min(mean_list)), "--",year_list[x3])
    
    x4 = (dev_list.index(max(dev_list)))
    print('Highest standard deviation:',(max(dev_list)), "--",year_list[x4])
    
    x5 = (dev_list.index(min(dev_list)))
    print('Lowest standard deviation:',(min(dev_list)), "--",year_list[x5])
    
    #Calls the highlow function to get the 2 varibles need for next lines of code
    temp_list, temp_lowList = highLow(listOfNumbers)

    #Used the index numbers of the all the list to compare temps to find the high and lowest and the year, then print out results
    x6 = (temp_list.index(max(temp_list)))
    print ('Highest temperature:', (max(temp_list)), "--", year_list[x6])
    
    x7 = (temp_lowList.index(min(temp_lowList)))
    print ('Lowest temperature:', (min(temp_lowList)), "--", year_list[x7])


#Main program
def main():
    print("High temperature data (Fahrenheit)\n")
    print("Year", "   Mean  ", "  Std Dev  ")
    print("----", "   ----  ", "  -------  ")

    #Open file for weather data
    file = open('msp-temperatures.txt', 'r')

    ##Send file to load weather data function
    loadWeatherData(file)

    ##Closes the file
    file.close()

    #To close the program
    quit_P = input('\nWould you like to exit program? y / n\n')

    if quit_P == "y" or quit_P == 'Y':
        quit()
        
#Run Main function at start of program
main()



    
