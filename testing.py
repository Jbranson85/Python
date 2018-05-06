import statistics
import math


file = open('msp-temperatures.txt', 'r')
temps = file.readlines()

##print("High temperature data (Fahrenheit)\n")
##print("Year", "   Mean  ", "  Std Dev  ")

year_list = []
mean_list = []
dev_list = []

for i in range(0,76):
    temps1 = temps[i]
    year = temps1.split(',', 1)[0]
    year_list.append(year)
    temps1 = temps1.split(',',1)[1]
    

    temp_ints = map(int, temps1.split(','))
    temps2 = statistics.mean(temp_ints)
    mean_list.append("{0:.2f}".format(temps2))
    dev1 = statistics.stdev(map(int, temps1.split(',')))
    dev_list.append("{0:.2f}".format(dev1))
    print(year, "   {0:.2f}  ".format(temps2), "  {0:.2f}  ".format(dev1))


x2 = (mean_list.index(max(mean_list)))
print('\nHighest mean temperature:',(max(mean_list)), "--",year_list[x2])
x3 = (mean_list.index(min(mean_list)))
print('Lowest mean temperature:',(min(mean_list)), "--",year_list[x3])
x4 = (dev_list.index(max(dev_list)))
print('Highest standard deviation:',(max(dev_list)), "--",year_list[x4])
x5 = (dev_list.index(min(dev_list)))
print('Lowest standard deviation:',(min(dev_list)), "--",year_list[x5])

temp_list = []
temp_lowList = []


for z in range(0,76):

    temps3 = temps[z]
    temps3 = temps3.split(',',1)[1]
    temp_ints2 = map(int, temps3.split(','))
    high = (max(temp_ints2))
    temp_list.append(high)

    temp_ints3 = map(int, temps3.split(','))
    low = (min(temp_ints3))
    temp_lowList.append(low)
    
   
x6 = (temp_list.index(max(temp_list)))
print ('Highest temperature:', (max(temp_list)), "--", year_list[x6])
x7 = (temp_lowList.index(min(temp_lowList)))
print ('Lowest temperature:', (min(temp_lowList)), "--", year_list[x7])

    



##print (mean_list.index(max(mean_list)))
##print (max(mean_list))
##print(year_list)




