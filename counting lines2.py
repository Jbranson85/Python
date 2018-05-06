'''counter.py

   Dr. Stange, 01-01-2017

   Adapted to Python 3 from a program written by Jeff Ondich, 9/9/09

   This program counts the number of lines in a file specified by the user.
   It also counts the number of lines at least 80 characters long.

   To test this program, create a text file (called, say, testdata.txt)
   with a bunch of lines, plus at least one line that's longer than
   80 characters.  Then run

      python3 counter.py
      File name, please: testdata.txt
      ...

   to see how many lines and how many long (>= 80) lines are in the file.
'''

fileName = ("testdata.txt")
file = open(fileName)

numberOfLines = 0
numberOfLongLines = 0
numberOfShortLines = 0
picklesOfLines = 0

for line in file:
    numberOfLines = numberOfLines + 1
    #If lines are greater than 80
    if len(line) >= 80:
        numberOfLongLines = numberOfLongLines + 1
    if len(line)<=80:
        numberOfShortLines = numberOfShortLines + 1
        #If lines are less than 80
    if  "Pickles" in str(line):
        picklesOfLines = picklesOfLines + 1
        #If lines are containing "Pickles"
file.close()

print('The number of lines in', fileName, 'is', numberOfLines)
print('The number of long lines (80 chars or more) is', numberOfLongLines)
print('The number of short lines(80 chars or less) is', numberOfShortLines)
print('The number of lines containing "pickles" is ', picklesOfLines)
