"""
Script to read poker hands from poker stars and add statistics to table
"""

import os
import sqlite3


path = os.path.join(os.path.expanduser('~'), 'Desktop', 'PokerStars.UK', 'HandHistory','harveylewis6')#path to hand folder


gamesPlayed = 0
gamesWon = 0   #initiate count
totalHandsDealt = 0
totalHandsWon =0


for filename in os.listdir(path):
	handsDealt = 0 #initiate hands dealt
	handsWon = 0

	tournamentTypeStartIndex = filename.find('Tournament #')
	tourneyCode = str(filename[12:23])

	amountStartIndex = filename.find('$')
	amountEndIndex = (filename.find('$', int(amountStartIndex + 1))) + 5
	tourneyType = str(filename[amountStartIndex:amountEndIndex])

	gamesPlayed +=1

	newPath = os.path.join(path, filename)

	open(newPath)

	tourney = open(newPath) #Opens tourney
	print

	for line in tourney.readlines(): #reads each line of tourney
		if 'Dealt to harveylewis6' in line: #Checks whether user was dealt in hand
			handsDealt +=1 #adds one to count
			totalHandsDealt+=1

		elif 'harveylewis6' and 'and won' in line: #checks if hand was won by user
			handsWon +=1 #adds to count if won
			totalHandsWon+=1

		elif 'harveylewis6 wins the tournament' in line:
			gamesWon+=1


	percentageOfHandsWon = (float(handsWon) / float(handsDealt)) * 100 #calculates percentage of hands won
	percentageOfHandsWon = round(percentageOfHandsWon, 2) #rounds percentage to 2 decimal places.

	print tourneyType
	print tourneyCode
	print str(handsDealt) + ' Hands dealt'
	print str(handsWon) + ' Hands won'
	print str(percentageOfHandsWon) + '% of hands won' + '\n \n'





totalPercentageOfHandsWon = (float(totalHandsWon) / float(totalHandsDealt)) * 100 #calculates percentage of hands won
totalPercentageOfHandsWon = round(percentageOfHandsWon, 2) #rounds percentage to 2 decimal places.


print str(gamesPlayed) + ' Tournaments Played'
print str(gamesWon) + ' Tournaments won in total'
print str(totalHandsDealt) + ' Hands dealt'
print str(totalHandsWon) + ' Hands won'
print str(totalPercentageOfHandsWon) + '% of hands won'



"""
To do###

sort out tourney codes
- buy ins
- rewards
ADD tourney codes as a column
Decide on column headers
no duplicates


"""
